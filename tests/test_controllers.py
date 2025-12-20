from unittest.mock import patch
from models.user import User

@patch("repositories.user_repository.UserRepository.get_user_by_email")
def test_profile_page_access(mock_get_user, client):
    fake_user = User(username="Malak", email="malak@test.com", password="123", role="student")
    mock_get_user.return_value = fake_user

    
    with client.session_transaction() as sess:
        sess["user_email"] = "malak@test.com"

    
    response = client.get("/profile")

    
    assert response.status_code == 200
    assert b"Malak" in response.data