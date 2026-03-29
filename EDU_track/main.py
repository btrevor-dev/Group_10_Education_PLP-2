from auth import Auth
from coursehub import CourseHub

def main():
    auth = Auth()
    hub = CourseHub()

    while True:
        print("\n=== EDU-Track ===")
        print("1. Login")
        print("2. Sign Up")
        print("0. Exit")

        ch = input("Choose: ")

        if ch == "1":
            user = auth.login()
            if user:
                hub.home(user)

        elif ch == "2":
            auth.signup()

        elif ch == "0" or ch.lower() == "exit":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
