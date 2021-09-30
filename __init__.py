from flask import Flask, render_template, request, redirect
from email.message import Message
import smtplib

app = Flask(__name__)


def mail(from_address, to_address, password, subject, message, priority):   #it send the mail,  only gmails without two factor authentication are supported
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        m = Message()
        m['From'] = from_address
        m['To'] = to_address
        m['X-Priority'] = str(priority)
        m['Subject'] = subject
        m.set_payload(message)
        smtp.login(from_address, password)
        smtp.sendmail(from_address, to_address, m.as_string())
    return None


@app.route('/')
def index():
    return render_template('pricing.html')


@app.route('/api/api_key')
def api_key():
    mail('mail.orderbywhatsapp@gmail.com', 'laminkutty@gmail.com', 'eqeonnmmthttrhka', 'Mail From Cron', 'the test mail from cron is working fine.', 2)
    return ''


@app.route('/upi', methods=['GET', 'POST'])
def upi():
    if request.method == 'POST':
        param = request.form['input']
        return f"<script>window.location = '{param}'</script>"
    return """
    <form method='post'>
    <input type='text' name='input'>
    <input type='submit'>
    </form>
    """


if __name__ == '__main__':
    app.run()
