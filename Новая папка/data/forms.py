from flask_wtf import FlaskForm
import wtforms




class SignUpform(FlaskForm):
    first_name =  wtforms.StringField("введить свой имя")
    last_name =  wtforms.StringField("введить свой фамилия")
    email = wtforms.EmailField("Email", validators=[wtforms.validators.Email(), wtforms.validators.data_required()])
    password = wtforms.PasswordField("введит парол",validators=[wtforms.validators.length(8)])



class Loginform(FlaskForm):
    email = wtforms.EmailField("Email", validators=[wtforms.validators.Email(), wtforms.validators.data_required()])
    password = wtforms.PasswordField("введит парол",validators=[wtforms.validators.length(8)])























































































