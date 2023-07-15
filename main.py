import smtplib
from flask import Flask, render_template,request, redirect
from info import sender, password

app = Flask(__name__)

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email, 'Тест!')
        server.quit()
    except Exception as e:
        return f'An error occurred "{e}"'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        send_email()
        return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    global email
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    email = request.form.get('email')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html)


if __name__ == '__main__':
    app.run(debug=True)
