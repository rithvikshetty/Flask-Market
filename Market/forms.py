from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired

class Register_Form(FlaskForm):
    username = StringField(label='User Name :', validators = [Length(min=6,max=30),DataRequired()])
    email_add = StringField(label='E-mail Address :', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Enter the Password :', validators = [Length(min=6), DataRequired()])
    password2 = PasswordField(label='Re-Enter the Password :', validators = [EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')