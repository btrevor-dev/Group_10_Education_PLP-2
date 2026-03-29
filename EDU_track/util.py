from datetime import datetime

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def get_date(msg):
    while True:
        d = input(msg)
        try:
            datetime.strptime(d, "%Y-%m-%d")
            return d
        except:
            print("Use format YYYY-MM-DD")
