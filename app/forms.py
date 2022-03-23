from flask_wtf import FlaskForm#从flask_wtf包中导入FlaskForm类
from wtforms import StringField,PasswordField,BooleanField,SubmitField#导入这些类
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()]) #用户名
	password = PasswordField('Password', validators=[DataRequired()]) #密码
	remember_me = BooleanField('Remember Me Please')  # 复选框
	submit = SubmitField('Sign In')

