print("Hi there! I'd like to get to know you")

def get_name():
    name = input("First thing's first. What's your name? ")
    if name:
        if name == "*":
            print("Come on, your real name\n")
            get_dob()
        else:
            return name
    else:
        print("Come on, please tell me your name\n")
        get_name()

def get_dob():
    dob = input("What's your date of birth? ")
    if dob:
        return dob
    else:
        print("It's no fun if you don't answer\n")
        get_dob()

def get_address():
    address = input("Where do you live? ")
    if address:
        return address
    else:
        print("I promise I'm not a stalker\n")
        get_address()

def get_goal():
    goal = input("What's your personal goal? ")
    if goal:
        return goal
    else:
        print("I promise I won't tell anyone")
        get_goal()

def biography():
    print(f'\nName: {get_name()}\nDate of birth: {get_dob()}\nAddress: {get_address()}\nPersonal goals: {get_goal()}')

biography()