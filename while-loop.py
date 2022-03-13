print('Please enter the command : ')
command = ""
started = False

while True:
    command = input('> ').lower().strip()
    if command == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car is starting....')
    elif command == 'stop':
        if not started:
            print('Car is already Stopped')
        else:
            started = False
            print('Car has stopped')
    elif command == 'help':
        print("""
start -- to start the car. 
stop-- to stop the car.
help: get the help 
        """)
    elif command == 'quit':
        break;
    else:
        print("Invalid command, please type 'help'.")
