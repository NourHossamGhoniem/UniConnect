from unittest.mock import patch, MagicMock
from repositories.user_repository import UserRepository

@patch("core.file_manager.FileManager.read_csv")
def test_get_user_by_email(mock_read_csv):
    mock_read_csv.return_value = [
        {"username": "Nour", "email": "nour@test.com", "password": "123", "role": "student"},
        {"username": "Admin", "email": "admin@test.com", "password": "pass", "role": "admin"}
    ]

    repo = UserRepository()
    user = repo.get_user_by_email("nour@test.com")

    assert user is not None
    assert user.username == "Nour"
    assert user.email == "nour@test.com"