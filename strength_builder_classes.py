#workouts:
def workoutA():
    squat.do_exercise()
    bench.do_exercise()
    row.do_exercise()

def workoutB():
    squat.do_exercise()
    press.do_exercise()
    deadlift.do_deadlift()

#program welcome:
print('Welcome to the Strength Builder workout program!')
welcome=input('Is this your first time using the program? (yes/no)')
if welcome =='yes':
        print('This program is comprised of two alternating workout programs: Workout A and Workout B')
        print('\t','You will be performing 3 sets of 5 reps for every compound exercise except for the Deadlift, which will be 1 set of 5')
if welcome =='no':
        print("Welcome back!")

class compound_exercises:
    def __init__(self,ID='', exercise='', sets='',rep='',reps=''):
        self.ID=ID
        self.exercise=exercise
        self.sets=sets
        self.rep=rep
        self.reps=reps

    def do_exercise(self):
        weight=int(input('What is your working weight for the ' + self.exercise + ' ?'))
        total=int(input('How many reps did you do on the ' + self.exercise + ' ?'))
        print('You performed the ' + self.exercise + ' for ' + self.sets + ' set of ' + str(total) + ' reps.')  
        print('Set Summary:' + str(total) + '/' + self.reps)

        total2=int(input('How many reps did you do on the ' + self.exercise + ' ?'))
        print('You performed the ' + self.exercise + ' for ' + self.sets + ' set of ' + str(total2) + ' reps.')  
        print('Set Summary:' + str(total2) + '/' + self.reps)
       
        total3=int(input('How many reps did you do on the ' + self.exercise + ' ?'))
        print('You performed the ' + self.exercise + ' for ' + self.sets + ' set of ' + str(total3) + ' reps.')  
        print('Set Summary:' + str(total3) + '/' + self.reps)

        if self.exercise == 'squat':
            squat_total=(total+total2+total3)
            if squat_total < 15:
                print('Because you missed one or more reps, your next ' + self.exercise + ' workout will be at ' + str(weight)+ ' lbs.')
            if squat_total >= 15:
                weight=weight+5
                print('Good work! You completed all your reps for this workout. Your next ' + self.exercise + ' workout will be ' + str(weight) + ' lbs.')

        if self.exercise == 'bench press':
            bench_total=(total+total2+total3)
            if bench_total < 15:
                print('Because you missed one or more reps, your next ' + self.exercise + ' workout will be at ' + str(weight)+ ' lbs.')
            if bench_total >= 15:
                weight=weight+5
                print('Good work! You completed all your reps for this workout. Your next ' + self.exercise + ' workout will be ' + str(weight) + ' lbs.')

        if self.exercise == 'barbell row':
            row_total=(total+total2+total3)
            if row_total < 15:
                print('Because you missed one or more reps, your next ' + self.exercise + ' workout will be at ' + str(weight)+ ' lbs.')
            if row_total >= 15:
                weight=weight+5
                print('Good work! You completed all your reps for this workout. Your next ' + self.exercise + ' workout will be ' + str(weight) + ' lbs.')

        if self.exercise == 'overhead press':
            press_total=(total+total2+total3)
            if press_total < 15:
                print('Because you missed one or more reps, your next ' + self.exercise + ' workout will be at ' + str(weight)+ ' lbs.')
            if press_total >= 15:
                weight=weight+5
                print('Good work! You completed all your reps for this workout. Your next ' + self.exercise + ' workout will be ' + str(weight) + ' lbs.')

    def do_deadlift(self):
        weight=int(input('What is your working weight for the ' + self.exercise + ' ?'))
        total=int(input('How many reps did you do on the ' + self.exercise + ' ?'))
        print('You performed the ' + self.exercise + ' for ' + self.sets + ' set of ' + str(total) + ' reps.')  
        print('Set Summary:' + str(total) + '/' + self.reps)

        if self.exercise == 'deadlift':
            deadlift_total=(total)
            if deadlift_total < 5:
                print('Because you missed one or more reps, your next ' + self.exercise + ' workout will be at ' + str(weight)+ ' lbs.')
            if deadlift_total >= 5:
                weight=weight+5
                print('Good work! You completed all your reps for this workout. Your next ' + self.exercise + ' workout will be ' + str(weight) + ' lbs.')
            
#exercises:
squat = compound_exercises('1', 'squat', '1', 1, '5')
bench= compound_exercises('2', 'bench press', '1', 1,'5')
row= compound_exercises('3','barbell row', '1', 1,'5')
press= compound_exercises('4', 'overhead press','1',1,'5')
deadlift= compound_exercises('5', 'deadlift','1',1,'5')

#selection of workouts
select_workout=input('What workout are you doing this session? (A/B)')
if select_workout == 'A':
    workoutA()
        
if select_workout == 'B':
    workoutB()