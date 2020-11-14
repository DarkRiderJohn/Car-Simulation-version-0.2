# first read the read me file 

from playsound import playsound
'''
This is the second improve version of car simulation
'''
print('Car version: 0.2')
print('Since it is the second version it is the second  worst version')
print()
print()

print('Well come to car simulation')
print("if you are new here enter 'help'")
start = False
while True:
    user_input = str.lower(input('>>'))

    if user_input == 'help':
        print('''
commands:   uses
help    :   shows the list of commands
start   :   Starts the car engines
run     :   runs the car
horn    :   Cmmon you know it
stop    :   stops the car only when car is running
quit    :   closes the program
    ''')
    elif user_input == 'start' and start == True:
        playsound('E:\ALL 2077\DarkRider\sounds\if car was started.mp3') # change here

    elif user_input == 'start':
        playsound('E:\ALL 2077\DarkRider\sounds\carstartgarage.mp3') # change here
        start = True

    elif user_input == 'run' and start != True:
        print('atlest check whether engines has been started or not!')
    elif user_input == 'run' and start == True:
        playsound('E:\ALL 2077\DarkRider\sounds\Drive off squealing tires.wav') # change here
        print("Car started running but we don't have steering")

    elif user_input == 'horn' and start != True:
        print('atlest check whether engines has been started or not!')
    elif user_input == 'horn' and start == True:
        playsound('E:\ALL 2077\DarkRider\sounds\car+horn+x.mp3') # change here


    elif user_input == 'stop' and start == True:
        playsound('E:\ALL 2077\DarkRider\sounds\car_brake_crash-Cam_Martinez.mp3') # change here
        print('Holyshit! close call')
        start = False


    elif user_input == 'quit' and start == True:
        print("Can't quit when the engine is running")
    elif user_input == 'quit' and start == False:
        print('Okay exiting program now...')
        break


    else:
        print("Invalid commands")

print()
print('New version will come soon even worst that this hahaha')
print("Damn! enimnem rocks")
