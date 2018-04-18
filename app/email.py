# The threading and multiprocessing modules can both do this. 
# Starting a background thread for email being sent is much less 
# resource intensive than starting a brand new process
from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_mail(app, msg):
	with app.app_context():
		mail.send(msg)


# but know that there are two types of contexts, 
# the application context and the request context. 
# In most cases, these contexts are automatically managed by the framework, 
# but when the application starts custom threads, 
# contexts for those threads may need to be manually created.
def send_mail(subject, sender, recipients, text_body, html_body, attachments=None, sync=False):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	if attachments:
		# the attachment could have several tuples inside
		# that is why use '*'
		for attachment in attachments:
			msg.attach(*attachment)
	if sync:
		mail.send(msg)
	else:
		Thread(target=send_async_mail, args=(current_app._get_current_object(), msg)).start()