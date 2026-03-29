from note import Note
from goal import Goal
from act import Activity
from datetime import datetime

class Course:

    @staticmethod
    def notes(user, cname):
        Note.menu(user, cname)

    @staticmethod
    def goals(user, cname):
        Goal.menu(user, cname)

    @staticmethod
    def activities(user, cname):
        Activity.menu(user, cname)

    @staticmethod
    def timeline(user, cname):
        print("\n=== Timeline ===")

        notes = user.courses[cname].get("notes", [])

        if not notes:
            print("No notes yet.")
            return

        now_time = datetime.now()

        for n in notes:
            try:
                t = datetime.strptime(n["time"], "%Y-%m-%d %H:%M")
                diff = (now_time - t).days

                if 0 <= diff <= 7:
                    print("[This Week]", n["text"])
                elif 7 < diff <= 14:
                    print("[Last Week]", n["text"])
                else:
                    print("[Older]", n["text"])

            except Exception as e:
                print("Error:", e)
