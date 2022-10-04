from flask import Flask,jsonify
from flask import request, redirect
import pyodbc
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    jsonResp = {'hello': 'world'}
    return jsonify(jsonResp)

@app.route('/resetdb')
def reset():
    # Make sure you modify this connection string to connect to your database, and not mine.
    connstr = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=tracker; UID=root; PASSWORD=bumblebee;'
    conn = pyodbc.connect(connstr)
    crsr = conn.cursor()

    # Drop the tables if they already exist
    sql = 'DROP TABLE IF EXISTS `tracker`.`login`;'
    crsr.execute(sql)
    sql = 'DROP TABLE IF EXISTS `tracker`.`user`;'
    crsr.execute(sql)
    sql = 'DROP TABLE IF EXISTS `tracker`.`data`;'
    crsr.execute(sql)
    sql = 'DROP TABLE IF EXISTS `tracker`.`email`;'
    crsr.execute(sql)
   
    sql = 'DROP TABLE IF EXISTS `tracker`.`burritoSales`;'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`user` (`id` INT NOT NULL AUTO_INCREMENT,`logins` VARCHAR(255) NULL,`password` VARCHAR(255) NULL, PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`login` (`id` INT NOT NULL AUTO_INCREMENT,`userid` INT NULL,`date` DATETIME, PRIMARY KEY (`id`), FOREIGN KEY (userid) REFERENCES `user`(id));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`email` (`id` INT NOT NULL AUTO_INCREMENT,`data` VARCHAR(255) NULL, `beefCount` INT NULL, `chixCount` INT NULL,`beanCount` INT NULL ,`porkCount` INT NULL, PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`data` (`id` INT NOT NULL AUTO_INCREMENT,`emailid` INT NULL,`date` DATETIME, PRIMARY KEY (`id`), FOREIGN KEY (emailid) REFERENCES `email`(id));'
    crsr.execute(sql)

    return 'Reset Successful'




@app.route('/login',methods = ['POST', 'GET'])
def login():
    connstr = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=tracker; UID=root; PASSWORD=bumblebee;'
    conn = pyodbc.connect(connstr)
    crsr = conn.cursor()

    if request.method == 'POST':
      logins = request.form['username']
      password = request.form['password']
      print(logins)
      print(password)
      crsr.execute('insert into user (logins,password) values (\'' + logins + '\',\'' + password + '\')')
      conn.commit()
      crsr.close()
      return redirect ("http://127.0.0.1:3000/")

      
   

if __name__ == '__main__':
   app.run(debug = True)
