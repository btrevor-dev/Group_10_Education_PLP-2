from user import User
from store import load, save

class Auth:

    def signup(self):
        data = load()

        print("\n-- Sign Up --")
        email = input("Email: ")

        if email in data:
            print("User already exists!")
            return

        name = input("Name: ")
        password = input("Password: ")
        program = input("Program: ")

        data[email] = {
            "name": name,
            "password": password,
            "program": program,
            "courses": {}
        }

        save(data)
        print("Account created!")

    def login(self):
        data = load()

        print("\n-- Login --")
        email = input("Email: ")
        password = input("Password: ")

        if email in data and data[email]["password"] == password:
            print("Login successful!")
            return User(email, data[email])

        print("Invalid credentials")
        return None
