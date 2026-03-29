from util import now
from datetime import datetime

class Note:

    @staticmethod
    def menu(user, cname):
        while True:
            print("\n1.Write 2.This Week 3.Last Week 0.Back")
            ch = input("Choose: ")

            if ch == "1":
                print("Write note (:wq to save)")
                lines = []

                while True:
                    line = input()
                    if line.strip() == ":wq":
                        break
                    lines.append(line)

                if lines:
                    user.courses[cname]["notes"].append({
                        "text": "\n".join(lines),
                        "time": now()
                    })
                    print("Note saved!")
                else:
                    print("Empty note not saved.")

            elif ch == "2":
                now_time = datetime.now()
                found = False

                for n in user.courses[cname]["notes"]:
                    t = datetime.strptime(n["time"], "%Y-%m-%d %H:%M")
                    diff = (now_time - t).days

                    if 0 <= diff <= 7:
                        print("-", n["text"])
                        found = True

                if not found:
                    print("No notes for this week")

            elif ch == "3":
                now_time = datetime.now()
                found = False

                for n in user.courses[cname]["notes"]:
                    t = datetime.strptime(n["time"], "%Y-%m-%d %H:%M")
                    diff = (now_time - t).days

                    if 7 < diff <= 14:
                        print("-", n["text"])
                        found = True

                if not found:
                    print("No notes for last week")

            elif ch == "0":
                break
