from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

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
    sql = 'CREATE TABLE `tracker`.`user` (`id` INT NOT NULL AUTO_INCREMENT,`login` VARCHAR(255) NULL, PRIMARY KEY (`id`));'
    crsr.execute(sql)
    sql = 'CREATE TABLE `tracker`.`login` (`id` INT NOT NULL AUTO_INCREMENT,`userid` INT NULL,`date` DATETIME, PRIMARY KEY (`id`), FOREIGN KEY (userid) REFERENCES `user`(id));'
    crsr.execute(sql)

    return 'Reset Successful'

# <user> allow us to put values in the web request, in this case, the user's login
@app.route('/login/<user>')
def login(user):
    connstr = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=tracker; UID=root; PASSWORD=bumblebee;'
    conn = pyodbc.connect(connstr)
    crsr = conn.cursor()

    # First, check if this user already exists
    sql = 'select id from user where login=\'' + user + '\''
    crsr.execute(sql)
    print('returned ' + str(crsr.rowcount) + ' rows')
    if crsr.rowcount == 0:
        print('adding ' + user)
        crsr.execute('insert into user (login) values (\'' + user + '\')')
        print('adding ' + str(crsr.rowcount) + ' user')
        print('re-executing ' + sql)
        crsr.execute(sql)
    res = crsr.fetchone()
    userid = res.id
    # Adding Login Info
    # TimeStamp
    sql = 'insert into login (userid,`date`) values (?, CURRENT_TIMESTAMP)'
    crsr.execute(sql, (userid))

    conn.commit()

    # Finally, get the user's login count and the total login count
    sql = 'select count(*) as logins from login where userid=?'
    crsr.execute(sql, (userid))
    res = crsr.fetchone()
    usercount = res.logins
    sql = 'select count(*) as logins from login'
    crsr.execute(sql)
    res = crsr.fetchone()
    totalcount = res.logins

    return jsonify({'user': user, 'user count':usercount, 'total count':totalcount })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)