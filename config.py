import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'my.env'))

class Config(object):
	# Flask-WTF extension uses this to protect web forms agains CSRF
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	# config for flask-sqlalchemy
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# email settings
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['your-email@example.com']

	POSTS_PER_PAGE = 5

	LANGUAGES=['en', 'zh_CN']

	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

	REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'