from flask.ext.wtf import Form #library wtf -> ambil Form
from wtforms import StringField, BooleanField, PasswordField, FileField,SelectField   #stringfield untuk input string, booleanfield untuk input boolean
from wtforms.validators import DataRequired #ini validator, untuk menjalankan validasi tiap data yg di submit


class Add(Form): #class SignUp untuk signup
	username = StringField('Username', validators = [DataRequired()])
	file = FileField()

class Setting(Form): #class SignUp untuk signup
	username = StringField('Username', validators = [DataRequired()])
	file = FileField()
	
#class Input(Form): #class SignUp untuk signup
	#nama = StringField('Nama', validators = [DataRequired()])
	
#class Ubah(Form): #class SignUp untuk signup
	#id = StringField('Id', validators = [DataRequired()])
	#nama = StringField('Nama', validators = [DataRequired()])