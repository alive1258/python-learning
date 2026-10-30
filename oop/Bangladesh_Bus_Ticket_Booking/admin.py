
class Admin:
    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True

        return False
