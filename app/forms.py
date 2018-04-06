from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User
# find a way to delay the evaluation of the string until it is used
from flask_babel import lazy_gettext as _l
from flask_babel import _

class EditProfileForm(FlaskForm):
	username = StringField(_l('Username'), validators=[DataRequired()])
	about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
	submit = SubmitField(_l('Submit'))

	# overloaded constructor that accepts the original username as an argument. 
	def __init__(self, original_username, *arg, **kwargs):
		super(EditProfileForm, self).__init__(*arg, **kwargs)
		self.original_username = original_username

	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError(_l('Please use a different username'))

class PostForm(FlaskForm):
	post = TextAreaField(_l('Say something'), validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField(_l('Submit'))