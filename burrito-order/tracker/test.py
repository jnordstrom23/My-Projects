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
    sql = 'DROP TABLE IF EXISTS `tracker`.`Orders`;'
    crsr.execute(sql)
    sql = 'DROP TABLE IF EXISTS `tracker`.`Users`;'
    crsr.execute(sql)
    sql = 'DROP TABLE IF EXISTS `tracker`.`Customer_Data`;'
    crsr.execute(sql)
   
    sql = 'CREATE TABLE `tracker`.`Users` (`id` INT NOT NULL AUTO_INCREMENT,`Username` VARCHAR(255) NULL,`Password` VARCHAR(255) NULL, PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`Orders` (`id` INT NOT NULL AUTO_INCREMENT,`first_name` VARCHAR(255) NULL,`last_name` VARCHAR(255) NULL,`Email` VARCHAR(255) NULL, `beef_burritos` VARCHAR(255) NULL, `chicken_burritos` VARCHAR(255) NULL,`bean_burritos` VARCHAR(255) NULL, `pork_burritos` VARCHAR(255) NULL, `tax` VARCHAR(255) NULL, `total_sale` VARCHAR(255) NULL,  PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`Customer_Data` (`id` INT NOT NULL AUTO_INCREMENT,`first_name` VARCHAR(255) NULL,`last_name` VARCHAR(255) NULL,`credit_card` VARCHAR(255) NULL,`CVV` VARCHAR(255) NULL,`ExpDate` VARCHAR(255) NULL,`Address` VARCHAR(255) NULL,`City` VARCHAR(255) NULL,`state` VARCHAR(255) NULL,`zipcode` VARCHAR(255) NULL,`Email` VARCHAR(255) NULL,  PRIMARY KEY (`id`));'
    crsr.execute(sql)
    
   

    return 'Reset Successful'

@app.route('/login',methods = ['POST', 'GET'])
def login():
    connstr = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=tracker; UID=root; PASSWORD=bumblebee;'
    conn = pyodbc.connect(connstr)
    crsr = conn.cursor()

    if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      print(username)
      print(password)
      
      crsr.execute('insert into Users (Username,Password) values (\'' + username + '\',\'' + password + '\' )' )
      
      conn.commit()
      crsr.close()
      return redirect ("http://127.0.0.1:3000/")


@app.route('/orders',methods = ['POST', 'GET'])
def orders():
    connstr = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=tracker; UID=root; PASSWORD=bumblebee;'
    conn = pyodbc.connect(connstr)
    crsr = conn.cursor()

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
       #start from here and then address execute
        credit_card = request.form['credit_card']
        CVV = request.form['CVV']
        ExpDate = request.form['ExpDate']
        Address = request.form['Address']
        City = request.form['City']
        state= request.form['state']
        zipcode = request.form['zipcode']
        Email = request.form['Email']
        beef_burritos = request.form['beef']
        chicken_burritos = request.form['chix']
        bean_burritos = request.form['bean']
        pork_burritos = request.form['pork']
        tax = request.form['tax']
        total_sale=request.form['total_sale']
      
  
      
        crsr.execute('insert into Orders (first_name, last_name,Email,beef_burritos, chicken_burritos, bean_burritos, pork_burritos,tax, total_sale) values (\'' + first_name + '\',\'' + last_name + '\',\'' + Email + '\',\'' + beef_burritos + '\',\'' + chicken_burritos + '\',\'' + bean_burritos + '\',\'' + pork_burritos + '\',\'' + tax + '\',\'' + total_sale + '\' )' )
        conn.commit()
        crsr.execute('insert into Customer_Data (first_name, last_name,credit_card,CVV,ExpDate,Address,City,state,zipcode,Email) values (\'' + first_name + '\',\'' + last_name + '\',\'' + credit_card + '\',\'' + CVV + '\',\'' + ExpDate + '\',\'' + Address + '\',\'' + City + '\',\'' + state + '\',\'' + zipcode + '\',\'' + Email + '\' )' )
        conn.commit()
        crsr.close()
        return redirect ("http://127.0.0.1:3000/Complete")

      
   

if __name__ == '__main__':
   app.run(debug = True)
