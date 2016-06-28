from werkzeug import secure_filename
import MySQLdb
import hashlib
import os

#def allowed_file(filename):
    #return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
	
'''def login(username,password):
	h = hashlib.md5(password.encode())
	list = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
	cursor = db.cursor()
	try:
		cursor.execute("select * from admin where user='"+username+"' and pswd='"+h.hexdigest()+"'") #menjalankan perintah sql
		results = cursor.fetchall()
		for row in results:
			id_admin = str(row[0])
			user = row[1]
			status = row[3]
		list = [id_admin,user,status]
	except:
		print "Error: unable to fecth data"
	db.close()
	return list'''
	
def add(username,password,ja,jk,filename):
	hasil = False
	h = hashlib.md5(password.encode())
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
	cursor = db.cursor()
	try:
		cursor.execute("insert into admin(user,pswd,status,jk,photo)values('"+username+"','"+h.hexdigest()+"','"+ja+"','"+jk+"','"+filename+"')") #menjalankan perintah sql
		results = cursor.fetchall()
		db.commit()
		hasil = True
	except:
		print "Error: unable to fecth data"
	db.close()
	return hasil

def view():
	list = []
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
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
			list.append(
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
	db.close()
	return list

def delete(id):
	hasil = False
	db = MySQLdb.connect("127.0.0.1","root","","latihanwebpython1" )
	cursor = db.cursor()
	try:
		cursor.execute("delete from admin where id_admin = '"+id+"'")
		results = cursor.fetchall()
		db.commit()
	except:
		print "Error: unable to fecth data"
	db.close()
	return hasil