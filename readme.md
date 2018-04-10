This project so far is an almost copy of The Flask Mega Tutorial

### how to run

`export FLASK_APP=microBlog.py`

`pip install -r requirement.txt`

`flask run`

### Modules used in this project

* Flask-WTF

* flask-sqlalchemy

* flask-migrate

* flask-login

* flask-mail

* pyjwt

* flask-bootstrap

* flask-moment

* flask-babel

* guess-language_spirit

* python-dotenv

### known bugs

1. translate to chinese is not working properly.

	* because g.locale() returns 'zh_Hans_CN' instead of 'zh_CN', it brings a lot of trouble to the logic. Here I am not going to fix it, because it is just a educational project.
