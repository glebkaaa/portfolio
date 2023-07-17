import smtplib
from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from info import sender, password

app = Flask(__name__)


def send_email(email, text):
    try:
        # Load template
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('templates/result.html')

        # Render template
        rendered_template = template.render(email=email, text=text)

        # Create message
        msg = MIMEMultipart()
        text = MIMEText(rendered_template, 'html')
        msg['From'] = formataddr(('Sender Name', sender))
        msg['To'] = email
        msg['Subject'] = 'Заявка'
        msg.attach(text)

        # Connect to SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email, msg.as_string())
        server.quit()

        return "Email sent successfully!"
    except Exception as e:
        return f'An error occurred: "{e}"'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    email = request.form.get('email')
    text = request.form.get('text')
    send_email(email, text)
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html)


if __name__ == '__main__':
    app.run(debug=True)
