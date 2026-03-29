from util import now

class Activity:

    @staticmethod
    def menu(user, cname):
        while True:
            print("\nActivities")
            print("1. Log Activity")
            print("2. View Activities")
            print("0. Back")

            ch = input("Choose: ")

            if ch == "1":
                name = input("Activity: ")
                lang = input("Language: ")

                user.courses[cname]["activities"].append({
                    "name": name,
                    "lang": lang,
                    "time": now()
                })

                print("Activity added!")

            elif ch == "2":
                for a in user.courses[cname]["activities"]:
                    print("-", a["name"], "|", a["lang"])

            elif ch == "0":
                break
