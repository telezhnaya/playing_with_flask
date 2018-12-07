from flask import Blueprint, current_app
from flask_mail import Message

from app.config import Config
from app.mail import mail

mail_bp = Blueprint('mail_bp', __name__)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@mail_bp.route('/email/<address>')
def time(address):
    msg = Message('my_subject',
                  sender=Config.MAIL_USERNAME,
                  recipients=['olyatelezhnaya@gmail.com'])
    # thr = Thread(target=send_async_email, args=[app, msg])
    # thr.start()
    #app = current_app._get_current_object()
    # with app.app_context():
    #     a = mail.connect()
    #mail.init_app(app)
    mail.send(msg)

    return 'success!'
