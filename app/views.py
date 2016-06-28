from flask import render_template, flash, redirect, request, url_for, send_from_directory,session
from app import app
from .forms import Setting
from .forms import Add
from werkzeug import secure_filename
import os
import time
import random
import MySQLdb
import hashlib
import models_admin
from random import randint
#from splinter import Browser

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
	
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
@app.route('/lihatadmin', methods=['GET', 'POST'])
def lihatadmin():
	list = []
	list = models_admin.view()
	return render_template('lihatadmin.html',posts=list)

@app.route('/setting', methods=['GET', 'POST'])
def setting():
	form = Add()
	list = []
	list = models_admin.view()
	return render_template('setting.html',posts=list,form=form)
	
@app.route('/addadmin', methods=['GET', 'POST'])
def addadmin():
	form = Add()
	list = []
	if form.validate_on_submit():
		username = str(request.form.get('username'))
		password = str(request.form.get('password'))
		ja = str(request.form.get('ja'))
		jk = str(request.form.get('jk'))
		file = request.files['file']
		if file and allowed_file(file.filename):
			uniq = (time.strftime("%d%m%Y%H%M%S")+str(randint(0,10000))) #nama file diambil dari waktu
			filename = secure_filename(file.filename) #nama file lengkap untuk upload
			ekstension = filename.rsplit('.', 1)[1] #extension
			filename = uniq + "." + ekstension #nama file setelah diedit
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			if(models_admin.add(username,password,ja,jk,filename)):
				flash('Data Admin Berhasil Ditambah!')
				return redirect('/addadmin')
		else:
			flash('Jenis Photo Hanya Boleh JPG, JPEG, Dan PNG!')
			return redirect('/addadmin')
	else:
		list = models_admin.view()
		'''for row in list:
			id_admin = list[0]
			user = list[1]
			pswd = list[2]
			status = list[3]
			jk = list[4]
			photo = list[5]
			listData.append(
				{
					'id_admin':id_admin,
					'user':user,
					'pswd':pswd,
					'status':status,
					'jk':jk,
					'photo':photo
				}
			)'''
		'''db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
		cursor = db.cursor()
		try:
			cursor.execute("select * from admin order by id_admin desc") #menjalankan perintah sql
			results = cursor.fetchall()
			for row in results:
				id_admin = str(row[0])
				user = row[1]
				pswd = row[2]
				status = row[3]
				jk = row[4]
				photo = row[5]
				listData.append(
					{
						'id_admin':id_admin,
						'user':user,
						'pswd':pswd,
						'status':status,
						'jk':jk,
						'photo':photo
					}
				)
		except:
			print "Error: unable to fecth data"
	db.close()'''
	return render_template('addadmin.html',form=form,posts=list)

@app.route('/hapus/<id>/<photo>', methods=['GET', 'POST'])
def hapus(id,photo):
	os.remove(os.path.join(app.config['UPLOAD_FOLDER'], photo))
	models_admin.delete(id)
	return redirect('/lihatadmin')
	return render_template('lihatadmin.html')

@app.route('/login', methods=['GET', 'POST'])	
def login(): #panggil procedure login
	'''form = Login()
	if form.validate_on_submit():'''
	username = str(request.form.get('username'))
	password = str(request.form.get('password'))
	h = hashlib.md5(password.encode())
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
	cursor = db.cursor()
	try:
		cursor.execute("select * from admin where user='"+username+"' and pswd='"+h.hexdigest()+"'") #menjalankan perintah sql
		results = cursor.fetchall()
		for row in results:
			id_admin = str(row[0])
			nama = row[1]
			pswd = row[2]
			status = row[3]
			jk = row[4]
			photo = row[5]
			session['id_admin'] = id_admin
			session['nama'] = nama
			session['status'] = status
			session['jk'] = jk
			session['photo'] = photo
			session['state'] = 1
		if nama == username and pswd == password:
			return redirect('/index')
		else:
			return redirect('/login')
	except:
		print "Error: unable to fecth data"
	db.close()
	'''else:
		return redirect('/index')'''
	return render_template('login.html')
	
@app.route('/logout')	
def logout():
	session.clear()
	session['state'] = 0
	'''with Browser() as browser:
        # Visit URL
		url = "login"
		browser.visit(url)
		browser.back()'''
	return redirect('login')
	
