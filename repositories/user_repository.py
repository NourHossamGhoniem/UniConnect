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
    



    
    def update_user(self, user, original_email):
        all_users = self.get_all_users()
        updated = False

        for u in all_users:
            if u.email == original_email:
                u.username = user.username
                u.password = user.password
                u.email = user.email
                updated = True
                break

        if updated:
            data_to_save = []
            for u in all_users:
                user_dict = {
                    "username": u.username,
                    "email": u.email,
                    "password": u.password,
                    "role": u.role
                }
                data_to_save.append(user_dict)

            self.fm.write_csv(
                self.FILENAME,
                data_to_save,
                fieldnames=["username", "email", "password", "role"]
            )
