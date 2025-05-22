command = ""

while True:
    command = input("Enter command: ")
    if command == "start":
        print("starting")
    elif command == "stop":
        print("stopping")
    elif command == "help":
        print("""start - to start the command
stop - to stop the command
help - to show this help""")
    elif command == "quit":
        print("quitting")
        break
    else:
        print("Invalid command")



