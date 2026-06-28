import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('ecom.html')
@app.route('/send-email', methods=['POST'])
def send_email():
    name= request.form['name']
    phone= request.form['phone']
    need= request.form['need']
    email= request.form['email']
    message= request.form['message']

    body= f"Name: {name}\nPhone: {phone}\nNeed: {need}\nEmail: {email}\nMessage: {message}"
    msg= Message(
        subject= 'New Quote Request',
        sender= app.config['MAIL_USERNAME'],
        recipients= [app.config['MAIL_USERNAME']],
        body= body
    )
    msg.body = body
    mail.send(msg)
    return 'Email sent successfully!'



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)