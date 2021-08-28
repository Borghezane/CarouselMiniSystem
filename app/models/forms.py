from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, FileField, TextField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])

	def isFilled(self):
		if( self.username.data != None and self.password.data != None):
			return True
		else:
			return False
        



class NewUserForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	role	 = SelectField("role", validators=[DataRequired()], choices=["client","admin"])
	def isFilled(self):
		if( self.username.data != None and self.password.data != None and self.role.data != None):
			return True
		else:
			return False
        


class NewCarouselForm(FlaskForm):
	name	 = StringField("name", validators=[DataRequired()])
	def isFilled(self):
		if( self.name.data != None ):
			return True
		else:
			return False

class NewImageForm(FlaskForm):
	filename    = FileField("filename", validators=[DataRequired()])
	description = TextField("description", validators=[DataRequired()])
	def isFilled(self):
		if( self.filename.data != None and self.description.data != None ):
			return True
		else:
			return False

