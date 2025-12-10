# models/user.py

class User:
    def __init__(self, username, email, password, role="student"):
        self.username = username
        self.email = email
        self.password = password   
        self.role = role

