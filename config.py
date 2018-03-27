import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	# Flask-WTF extension uses this to protect web forms agains CSRF
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	# config for flask-sqlalchemy
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False