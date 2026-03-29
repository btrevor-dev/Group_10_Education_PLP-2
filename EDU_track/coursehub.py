from course import Course
from store import load, save

class CourseHub:

    def home(self, user):
        while True:
            print(f"\nWelcome {user.name}")
            print("1. Course Hub")
            print("0. Logout")

            ch = input("Choose: ")

            if ch == "1":
                self.hub(user)
            elif ch == "0":
                break

    def hub(self, user):
        while True:
            print("\nCommands: run/add/remove/list/back")
            cmd = input("> ")

            if cmd.startswith("run "):
                cname = cmd[4:]
                if cname in user.courses:
                    self.menu(user, cname)
                else:
                    print("Course not found")

            elif cmd.startswith("add "):
                cname = cmd[4:]
                user.courses[cname] = {
                    "notes": [],
                    "goals": [],
                    "activities": []
                }
                print("Course added!")

            elif cmd.startswith("remove "):
                cname = cmd[7:]
                if cname in user.courses:
                    del user.courses[cname]
                    print("Course removed!")

            elif cmd == "list":
                if not user.courses:
                    print("No courses yet")
                else:
                    for c in user.courses:
                        print("-", c)

            elif cmd == "back":
                break

    def menu(self, user, cname):
        while True:
            print(f"\nCourse: {cname}")
            print("1. Timeline")
            print("2. Notes")
            print("3. Goals")
            print("4. Activities")
            print("0. Back")

            ch = input("Choose: ")

            if ch == "1":
                Course.timeline(user, cname)
            elif ch == "2":
                Course.notes(user, cname)
            elif ch == "3":
                Course.goals(user, cname)
            elif ch == "4":
                Course.activities(user, cname)
            elif ch == "0":
                data = load()
                data[user.email]["courses"] = user.courses
                save(data)
                break
            else:
                print("Invalid choice")
