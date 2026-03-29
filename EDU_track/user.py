class User:
    def __init__(self, email, data):
        self.email = email
        self.name = data["name"]
        self.program = data["program"]
        self.courses = data["courses"]
