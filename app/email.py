# The threading and multiprocessing modules can both do this. 
# Starting a background thread for email being sent is much less 
# resource intensive than starting a brand new process
from threading import Thread
from flask_mail import Message
from flask import render_template
from app import app, mail

def send_async_mail(app, msg):
	with app.app_context():
		mail.send(msg)


# but know that there are two types of contexts, 
# the application context and the request context. 
# In most cases, these contexts are automatically managed by the framework, 
# but when the application starts custom threads, 
# contexts for those threads may need to be manually created.
def send_mail(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	Thread(target=send_async_mail, args=(app, msg)).start()

def send_password_reset_email(user):
	token = user.get_reset_password_token()
	send_mail('[Microblog] Reset your Password', sender=app.config['ADMINS'][0], recipients=[user.email],text_body = render_template('email/reset_password.txt', user = user, token=token), html_body = render_template('email/reset_password.html', user=user, token=token))