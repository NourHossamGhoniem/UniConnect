# repositories/user_repository.py

from core.file_manager import FileManager
from models.user import User

class UserRepository:
    FILENAME = "users.csv"

    def __init__(self):
        self.fm = FileManager()

    def get_all_users(self):
        data = self.fm.read_csv(self.FILENAME)
        return [
            User(
                row["username"],
                row["email"],
                row["password"],
                row.get("role", "student")
            )
            for row in data
        ]

    def get_user_by_email(self, email):
        for user in self.get_all_users():
            if user.email == email:
                return user
        return None

    def add_user(self, user: User):
        self.fm.append_csv(
            self.FILENAME,
            {
                "username": user.username,
                "email": user.email,
                "password": user.password,
                "role": user.role
            },
            fieldnames=["username", "email", "password", "role"]
        )
    
    def update_user(self, user: User):
        all_users = self.get_all_users()
        updated = False
        for u in all_users:
            if u.email == user.email:
                u.username = user.username
                updated = True
        if updated:
            # Use write_csv from FileManager
            self.fm.write_csv(
                self.FILENAME,
                [u.__dict__ for u in all_users],
                fieldnames=["username", "email", "password", "role"]
            )
