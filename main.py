from Prototype.functions import Functions

logged = False
while True:
    print("\nC.A.P.T.I.O.S.U.S\n")
    print("1. Register ")
    print("2. Login ")
    print("3. To Do List Functions")
    print("4. Exit\n")
    while True:
        try:
            reply1 = int(input("Choose (1\\2): "))
            break
        except:
            print("Given value is not a valid option please choose again. ")

    print()
    if reply1 == 1:
        print("Fill the following information to register: \n")
        while True:
            username = input("Enter Username: ")
            if Functions.check_username(username=username):
                break
            else:
                print("Username already taken. ")

        name = input("Enter Name: ")
        while True:
            password = input("Enter Password: ")
            re_password = input("Re-Enter Password: ")
            if password == re_password:
                break
            else:
                print("\nThe password is not the same.\nPlease re-do it again")
        Functions.register(password=password, username=username, name=name)

    elif reply1 == 2:
        print("Fill the following information to Login: \n")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        credentials = Functions.check_creds_for_login(username=username, password=password)
        if credentials:
            logged = Functions.get_user(username=username)
            print("\nLogin Successful")
        else:
            print("\nIncorrect Username or Password")

    elif reply1 == 3:
        if logged:
            while True:
                print("\nTO.DO.LIST Functions\n")
                print("Choose from the following options: \n")
                print("1. View list")
                print("2. Append a task")
                print("3. Choose a task")
                print("4. Remove a task")
                print("5. Exit\n")
                try:
                    reply2 = int(input("Choose (1\\2): "))
                    break
                except:
                    print("Given value is not a valid option please choose again. ")
            if reply2 == 1:
                print()
                if len(logged["tdList"]) == 0:
                    print("List is empty")
                else:
                    print("\nMy To Do List")
                for i in logged["tdList"]:
                    print(f"{logged['tdList'][i]['id']}.", i)
        else:
            print("Log in first.")

    elif reply1 == 4:
        print("\nExiting the loop...")
        break
