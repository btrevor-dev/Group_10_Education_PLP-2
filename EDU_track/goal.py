from util import now, get_date

class Goal:

    @staticmethod
    def menu(user, cname):
        while True:
            print("\nGoals")
            print("1. New Goal")
            print("2. Ongoing Goals")
            print("3. Completed Goals")
            print("4. Mark Complete")
            print("0. Back")

            ch = input("Choose: ")

            if ch == "1":
                name = input("Goal name: ")
                start = get_date("Start date: ")
                end = get_date("End date: ")

                user.courses[cname]["goals"].append({
                    "name": name,
                    "start": start,
                    "end": end,
                    "progress": 0,
                    "completed": False,
                    "done_date": None
                })

                print("Goal added!")

            elif ch == "2":
                for g in user.courses[cname]["goals"]:
                    if not g["completed"]:
                        print("-", g["name"], "|", g["progress"], "%")

            elif ch == "3":
                for g in user.courses[cname]["goals"]:
                    if g["completed"]:
                        print("-", g["name"], "| Done:", g["done_date"])

            elif ch == "4":
                name = input("Goal name: ")
                for g in user.courses[cname]["goals"]:
                    if g["name"] == name:
                        g["completed"] = True
                        g["done_date"] = now()
                        print("Completed!")

            elif ch == "0":
                break
