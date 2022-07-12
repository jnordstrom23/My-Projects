

from tkinter import CENTER, UNDERLINE
from tkinter.font import BOLD, ITALIC
from tkinter import *
import PySimpleGUI as sg

# several color themes to play with; "HotDogStand" one of my faves
# 75 lines of code worth of color options
sg.theme("Reddit")

#drop down menu upper left corner (only coded item in menubar so far "EXIT"
menu_def = [['&#', ['HISTORY','MENU', 'NUTRITION','LOCATIONS', "EXIT"]]]

layout = [  
            [sg.MenubarCustom(menu_def)],
            [sg.Text("THE BURRITO BUILDER", font=("Ariel",40,[ITALIC,BOLD]),text_color="grey47",size=30,justification="center"),
            sg.Button('SIGN IN',button_color='orange',font=("Ariel", 18,[ITALIC]),key='signin', bind_return_key=False)],

            
            [sg.HorizontalSeparator(color="black")],
#base selections:
            [sg.Text("MEAT & VEGGIES", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],

            [sg.Radio("BEEF",'meat',key="BEEF"),
            sg.Radio("CHICKEN",'meat',key="CHICKEN"), 
            sg.Radio("PORK","meat",key="PORK"),
            sg.Radio("VEGGIE", "meat",key="VEGGIE")
            ],
#additional options:
            [sg.Text("RICE & BEANS", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],

            [sg.Checkbox("CILANTRO LIME RICE", key='CILANTRO LIME RICE'),
            sg.Checkbox("BROWN RICE", key='BROWN RICE'),
            sg.Checkbox("REFRIED BEANS", key='REFRIED BEANS'),
            sg.Checkbox("BLACK BEANS", key='BLACK BEANS')],

            [sg.Text("VEGGIES", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],
            
            [sg.Checkbox("GRILLED CORN",key='GRILLED CORN'),
            sg.Checkbox("SAUTEED VEGGIES", key= 'SAUTEED VEGGIES'),
            sg.Checkbox("LETTUCE", key= 'VEGGIES')],
            
            [sg.Text("DAIRY", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],

            [sg.Checkbox("CHEESE", key="CHEESE"),
            sg.Checkbox("SOUR CREAM", key='SOUR CREAM')],
            
            [sg.Text("EXTRAS", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],

            [sg.Checkbox("GUACAMOLE", key='GUACAMOLE'),
            sg.Checkbox("PICO DE GALLO", key='PICO DE GALLO'),
            sg.Checkbox("FRESH CILANTRO", key='FRESH CILANTRO')],

            [sg.Text("SAUCES", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],

            [sg.Checkbox("HOT SAUCE", key='HOT SAUCE'),
            sg.Checkbox("MEDIUM SAUCE", key='MEDIUM SAUCE'),
            sg.Checkbox("MILD SAUCE", key='MILD SAUCE'),
            sg.Checkbox("CREAMY CHIPOTLE SAUCE", key='CREAMY CHIPOTLE SAUCE')],
            
        
#additional requests:        
            [sg.Text ("YOUR BURRITO", font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],
            [sg.Output(size=(40,10))],
            [sg.Text ("*To modify burrito fillings, delete ALL items in BURRITO box")],
            [sg.Button('COMPLETE YOUR ORDER',button_color="orange",font=("Ariel", 18,[ITALIC]),key="COMPLETE YOUR ORDER")], 
            [sg.Text()]  
        ]


layout=[[sg.Column(layout,element_justification="center",pad=(0,0))]]


#Creating the Window with layout insert #sg.Titlebar disables resize but add color
window = sg.Window(' BUILDING MILLIONS OF BURRITOS EVERYDAY ', layout,background_color="gray",font=(BOLD),text_justification="center", resizable=True,finalize=True)
window.TKroot.minsize(475,600)
window.TKroot.maxsize(1600,1100)

#Event and Window Interaction
while True:            
    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event != sg.Button or sg.Radio:
            for item in values:
                if values[item] == True:
                    print(item)       
    if event == 'COMPLETE YOUR ORDER':
                event, values = sg.Window('CHECKOUT',
                    [[sg.Text("'COMPLETE' OR 'CANCEL' TO MODIFY",font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],
                    [sg.Button('COMPLETE',button_color="orange",font=("Ariel", 18,[ITALIC])), sg.Button('CANCEL',button_color="orange",font=("Ariel", 18,[ITALIC])) ]],size=(800,200),text_justification='center',element_justification='center').read(close=True)
                if event == 'COMPLETE':
                    event, values = sg.Window('ANOTHER BURRITOFUL CREATION',
                    [[sg.Text("THANK YOU FOR YOUR ORDER!",font=("Comic Sans MS",18,[ITALIC]),text_color="grey47",size=100,justification="center")],
                    [sg.Button('DONE',button_color="orange",font=("Ariel", 18,[ITALIC])),]],size=(800,200),text_justification='center',element_justification='center').read(close=True)
                    if event == 'DONE' or event ==sg.WIN_CLOSED:
                        break
    
    if event == 'signin':
        f = open('burritologin.txt', 'w')
        event, values = sg.Window('Please Login',
                [[sg.Text('Usersname:'), sg.Input(key='-ID-')],
                [sg.Text('Password:'),sg.Input(key='-PASS-')],
                [sg.Button('Submit'), sg.Button('Cancel') ]]).read(close=True)

        f.write(values.get('-ID-')+':'+ values.get('-PASS-'))

        f.close()

     