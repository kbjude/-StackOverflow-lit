class User:
    def __init__(self, args = {}):
        self.username = args["username"] if "username" in args.keys() else ""
        self.password = ""
        self.name = ""
        self.confirm = ""
        self.message = ""

    def save(self):
        pass

    def validate(self):
        pass