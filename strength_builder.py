#The primary goal of this program is to be a workout tracker.
#Tracking will be based off a novice-intermediate level linear weight lifting program.
#The name of this program will be "Strength Builder"

#Function(s):
def yes_workout():
    print ("Great! Let's start you on your path to getting stronger!""\n""This program was designed to track alternating full body barbell workouts: 'Workout A' and 'Workout B':""\n")
    print ("\t","Workout A exercises are: The Squat, Bench Press, and The Row.")
    print ("\t","Workout B exercises are: The Squat, Overhead Press, and The Deadlift.""\n")
    print ("All exercises require 3 sets with a repitition goal of 5, except for The Deadlift which is done as 1 set.")
    print ("Again, these workouts work best when done in alternating fashion.")
    print ("For best results do these workouts no more than 3 times per week, with 1-2 days rest in between.")
    print ("If you are new to barbell workouts, it is recommended that you start with just the bar (45 lbs), that way you have time to learn technique as you gain strength.")

def workoutA():
    print ("Summary of today's workout:")
    print ("You Squatted",squatA_weight, "lbs for:")
    print ("\t","Set 1:",squatA_set1, "/5")
    print ("\t","Set 2:",squatA_set2, "/5")
    print ("\t","Set 3:",squatA_set3,"/5")
    
    print ("You Benched",bench_weight, "lbs for:")
    print ("\t","Set 1:",bench_set1, "/5")
    print ("\t","Set 2:",bench_set2, "/5")
    print ("\t","Set 3:",bench_set3,"/5")

    print ("You Rowed",row_weight, "lbs for:")
    print ("\t","Set 1:",row_set1, "/5")
    print ("\t","Set 2:",row_set2, "/5")
    print ("\t","Set 3:",row_set3,"/5")

def workout_B():
    print ("Summary of today's workout:")
    print ("You Squatted",squatA_weight, "lbs for:")
    print ("\t","Set 1:",squatA_set1, "/5")
    print ("\t","Set 2:",squatA_set2, "/5")
    print ("\t","Set 3:",squatA_set3,"/5")

    print ("You Pressed",press_weight, "lbs for:")
    print ("\t","Set 1:",press_set1, "/5")
    print ("\t","Set 2:",press_set2, "/5")
    print ("\t","Set 3:",press_set3,"/5")

    print ("You Deadlifted",dead_weight, "lbs for:")
    print ("\t","Set 1:",dead_set1, "/5")


#Welcoming the User

print("Welcome to Strength Builder.")
print("Whether it's everyday tasks like carrying your groceries or becoming a better athlete, the Strength Builder program can help you do that!")
name= input("To get started, please type in your name:")
while name.isnumeric():
    print("That is not a valid name.")
    name= input("To get started, please type in your name: ")
new_name=name.strip()
new_name=name.capitalize()
confirm=input ("\t" + "Hey " + new_name + ", do you want to get stronger? Type 'yes' to become a member or 'no' to stay weak.")

#opening membership file
f = open('finalproject.txt', 'a')
membership=[]

answer=["yes","no"]

while confirm not in answer:
    print ("Not a valid answer.")
    confirm=input ("\t" + "Hey " + new_name + ", do you want to get stronger? (yes/no)")

if confirm == "no":
    print ("Sorry to hear that! We will be here when you are ready.")


#Introduction to Workouts
if confirm == "yes":
    yes_workout() #function found at top of code
    membership.append(new_name) #adding to membership file for log
    for m in membership:
        f.write(m+'\n')
    
        f.close()

#User selects workout A or B as defined in Introduction and workout tracker is generated with the rep goal of 5
    workouts=["A","B"] 
    workout=input("\t"+ "Alright " + new_name + " what workout do you want to do? (A/B)")
    while workout not in workouts:
        print ("Not a valid answer.")
        workout=input("\t"+ "Alright " + new_name + " what workout do you want to do? (A/B)")
    
    rep_goal=5 #rep goal is set to 5 for this workout program. 
    #For user customizable approach could be rep_goal=[]

#Workout A and exercises:
    if workout=="A":
        print("Workout A")
        print("Exercise A1: The Squat")
        squatA_weight=int(input("What weight will you be lifting for The Squat? "))
        print ("Ok, your working sets for The Squat are " + str(squatA_weight) + " lbs:")
    
        squatA_set1=int(input ("\t" + "Set 1: "))
        if squatA_set1 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if squatA_set1 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        squatA_set2=int(input("\t" + "Set 2: "))
        if squatA_set2 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if squatA_set2 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        squatA_set3=int(input("\t" + "Set 3: "))
        if squatA_set3 ==rep_goal:
            print ("Good job! Next exercise is Bench Press")
        if squatA_set3 <rep_goal:
            print ("Nice try! Next exercise is Bench Press")
   
        print ("Exercise A2: Bench Press")
        bench_weight=int(input("What weight will you be lifting for Bench Press? "))
        print ("Ok, your working sets for Bench Press are " + str(bench_weight) + " lbs:")

        bench_set1=int(input ("\t" + "Set 1: "))
        if bench_set1 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if bench_set1 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        bench_set2=int(input("\t" + "Set 2: "))
        if bench_set2 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if bench_set2 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        bench_set3=int(input("\t" + "Set 3: "))
        if bench_set3 ==rep_goal:
            print ("Good job! Next exercise is The Row")
        if bench_set3 <rep_goal:
            print ("Nice try! Next exercise is The Row")

        print ("Exercise A3: The Row")
        row_weight=int(input("What weight will you be lifting for The Row? "))
        print ("Ok, your working sets for The Row are " + str(row_weight) + " lbs:")

        row_set1=int(input ("\t" + "Set 1: "))
        if row_set1 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if row_set1 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        row_set2=int(input("\t" + "Set 2: "))
        if row_set2 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if row_set2 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        row_set3=int(input("\t" + "Set 3: "))
        if row_set3 ==rep_goal:
            print ("Good job! You have completed your workout")
        if row_set3 <rep_goal:
            print ("Nice try! You have completed your workout")

#Summary of Workout A
    
        workoutA() #function found at top of code
        
        
        

#Next workout Recommendations   
        
        squat_allsets=(squatA_set1+squatA_set2+squatA_set3)
      

        plate=5
        if squat_allsets==15:
            squatA_weight=squatA_weight+plate
            print ("Good work! Your next workout you will Squat:",squatA_weight, "lbs.")
        if squat_allsets<15:
            print ("Keep on Grinding! Repeat",squatA_weight,"lbs. for your next Squat workout.")

        bench_allsets=(bench_set1+bench_set2+bench_set3)
        if bench_allsets==15:
            bench_weight=bench_weight+plate
            print ("Good work! Your next workout you will Bench :",bench_weight, "lbs.")
        if bench_allsets<15:
            print ("Keep on Grinding! Repeat",bench_weight,"lbs. for your next Bench workout.")

        row_allsets=(row_set1+row_set2+row_set3)
        if row_allsets==15:
            row_weight=row_weight+plate
            print ("Good work! Your next workout you will Row:",row_weight, "lbs.")
        if row_allsets<15:
            print ("Keep on Grinding! Repeat",row_weight,"lbs. for your next Row workout.")
    

    #Workout B and exercises:
    if workout=="B":
        print("Workout B")
        print("Exercise B1: The Squat")
        squatA_weight=int(input("What weight will you be lifting for The Squat? "))
        print ("Ok, your working sets for The Squat are " + str(squatA_weight) + " lbs:")
    
    
        squatA_set1=int(input ("\t" + "Set 1: "))
        if squatA_set1 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if squatA_set1 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        squatA_set2=int(input("\t" + "Set 2: "))
        if squatA_set2 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if squatA_set2 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        squatA_set3=int(input("\t" + "Set 3: "))
        if squatA_set3 ==rep_goal:
            print ("Good job! Next exercise is the Overhead Press")
        if squatA_set3 <rep_goal:
            print ("Nice try! Next exercise is the Overhead Press")
   
        print ("Exercise B2: Overhead Press")
        press_weight=int(input("What weight will you be lifting for Overhead Press? "))
        print ("Ok, your working sets for Overhead Press are " + str(press_weight) + " lbs:")

        press_set1=int(input ("\t" + "Set 1: "))
        if press_set1 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if press_set1 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        press_set2=int(input("\t" + "Set 2: "))
        if press_set2 ==rep_goal:
            print ("Good job! Rest 2 minutes before next set.")
        if press_set2 <rep_goal:
            print ("Nice try! Rest 3 minutes before next set.")
        press_set3=int(input("\t" + "Set 3: "))
        if press_set3 ==rep_goal:
            print ("Good job! Next exercise is The Deadlift")
        if press_set3 <rep_goal:
            print ("Nice try! Next exercise is The Deadlift")

        print ("Exercise B3: The Deadlift")
        dead_weight=int(input("What weight will you be lifting for The Deadlift? "))
        print ("Ok, your working sets for The Deadlift are " + str(dead_weight) + " lbs:")

        dead_set1=int(input ("\t" + "Set 1: "))
        if dead_set1 ==rep_goal:
            print ("Good job! You have completed your workout!.")
        if dead_set1 <rep_goal:
            print ("Maybe next time. Good job completing your workout!")
        

#Summary of Workout B
        workout_B() #function found at top of code
        
#Next workout Recommendations   
        plate=5
        squat_allsets=(squatA_set1+squatA_set2+squatA_set3)
        if squat_allsets==15:
            squatA_weight=squatA_weight+plate
            print ("Good work! Your next workout you will Squat:",squatA_weight, "lbs.")
        if squat_allsets<15:
            print ("Keep on Grinding! Repeat",squatA_weight,"lbs. for your next Squat workout.")

        press_allsets=(press_set1+press_set2+press_set3)
        if press_allsets==15:
            press_weight=press_weight+plate
            print ("Good work! Your next workout you will Overhead Press :",press_weight, "lbs.")
        if press_allsets<15:
            print ("Keep on Grinding! Repeat",press_weight,"lbs. for your next Overhead Press workout.")

        dead_allsets=(dead_set1)
        if dead_allsets==5:
            dead_weight=dead_weight+plate+plate
            print ("Good work! Your next workout you will Deadlift:",dead_weight, "lbs.")
        if dead_allsets<5:
            print ("Keep on Grinding! Repeat",dead_weight,"lbs. for your next Deadlift workout.")