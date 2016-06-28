from flask import Flask #import library Flask 'f'

app = Flask(__name__) #cara menjalankan apps
app.config.from_object('config')
from app import views #kita panggil file view