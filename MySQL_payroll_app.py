import PySimpleGUI as sg
from tkinter import CENTER, UNDERLINE
from tkinter.font import BOLD, ITALIC
from tkinter import *
import pyodbc

connect = 'DRIVER=/usr/local/mysql-connector-odbc-8.0.29-macos12-x86-64bit/lib/libmyodbc8a.so; SERVER=localhost; PORT=3306;DATABASE=Burrito Builder; UID=root; PASSWORD=bumblebee;'

sg.theme("DARKTEAL7")


layout = [  
            [sg.Text("THE PAYROLLER", font=("Ariel",40,[ITALIC,BOLD]),text_color="white",size=30)],
            [sg.Text()],
            [[sg.Text('LAST NAME:'), sg.Input(key='-LNAME-')]],
            [[sg.Text('FIRST NAME:'),sg.Input(key='-FNAME-')]],
            [[sg.Button('Search'), sg.Button('Cancel') ]],
            [[sg.Text(size=(40,1),key='-OUTPUT1-')]],
            [[sg.Text('ADD HOURS:'),sg.Input(key='-HOURS-')]],
            [[sg.Button('Submit'), sg.Button('Exit') ]]

        ]



#Creating the Window with layout insert #sg.Titlebar disables resize but add color
window = sg.Window(' KEEPING YO BUSINESS ROLLING BY PAYING YO PEOPLE ', layout,font=(BOLD),element_justification='c',text_justification="center", resizable=True,finalize=True)
window.TKroot.minsize(475,300)
window.TKroot.maxsize(1600,1100)

db = pyodbc.connect(connect)
while True:            
    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == 'EXIT' or event =='Cancel' or event == 'Exit':
        break

   
    if event == 'Search':
        lname=values.get('-LNAME-') 
        fname=values.get('-FNAME-')
        hoursworked=values.get('-HOURS-')
        
        sql = "select * from employees where `last name`='"+lname+"' and `first name`='"+fname+"'"
        crsr1 = db.cursor()
        result = crsr1.execute(sql)
        #Checking for current hours worked for inputted Employee Name
        for row in result:
            s=(row.__getattribute__('First Name') + ' ' + row.__getattribute__('Last Name') + " you have worked: " + row.__getattribute__('Hours') + ' hours')
            print(s)
            window['-OUTPUT1-'].update(s)
            
        crsr1.close()
       

    if event == 'Submit':
        lname=values.get('-LNAME-') 
        fname=values.get('-FNAME-')
        hoursworked=values.get('-HOURS-')


        #Logging/ Updating hours worked for the inputted Employee
        
        sql = "UPDATE employees SET Hours = hours + '"+hoursworked+"'WHERE `last name`='"+lname+"' and `first name`='"+fname+"'"
        crsr2 = db.cursor()
        result2= crsr2.execute(sql)
        db.commit()

        #Update total pay
        sql = "UPDATE Employees SET `Total Pay`= (Hours * Wage) WHERE `last name`='"+lname+"' and `first name`='"+fname+"'"
        crsr3 = db.cursor()
        result3= crsr3.execute(sql)
        db.commit()

        #Display of Employees hours worked and total pay
        sql = "select * from employees where `last name`='"+lname+"' and `first name`='"+fname+"'"
        crsr4 = db.cursor()
        result4= crsr4.execute(sql)

        for row in result4:
            print(row.__getattribute__('First Name') + ' ' + row.__getattribute__('Last Name') + " you have now worked: " + row.__getattribute__('Hours') + ' hours and your paycheck will be $' + row.__getattribute__('Total Pay'))

       
        crsr2.close()
        crsr3.close()
        crsr4.close()

db.close()