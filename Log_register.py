"""Check if passwords match"""


def confirm(new_password):
    while True:
        confirm_password = input("Confirm new password: ")
        if confirm_password != new_password:
            print("Passwords do not match, please try again. ")
        else:
            return confirm_password


username_password = {}


def main():
    with open("user.txt", "r") as in_file:
        for line in in_file:
            username, password = line.strip().split(";")
            username_password[username] = password

    while True:
        choice = input("Would you like to log in(1) or register user(2)? ")
        if choice == "1":
            log_in()
        elif choice == "2":
            register_user()
        else:
            raise ValueError("Invalid choice. Please, enter '1' or '2'. ")


"""Log in"""


def log_in():
    global username_password
    logged_in = False
    while not logged_in:
        print("\n\33[1mLOG IN\33[0m")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")

        if curr_user in username_password.keys() and username_password[curr_user] == curr_pass:
            print("Login Successful!")
            logged_in = True
        else:
            print("Login Failed! Try again.")


""" Register new user """


def register_user():
    global username_password
    print("\n\33[1mREGISTER USER\33[0m")
    new_username = input("New username:")

    while new_username in username_password.keys():
        print("User already exists. Please enter a different user name.")
        new_username = input("New username:")

    new_password = input("New password: ")
    confirm_password = confirm(new_password)

    if confirm_password == new_password:
        print("New user added! ")
        username_password[new_username] = new_password

        with open("user.txt", "a") as out_file:
            out_file.write(f"{new_username};{new_password}\n")


action = main()

"""Tic Tac Toe"""
