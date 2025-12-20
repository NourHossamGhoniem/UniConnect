from models.user import User
from models.message import Message

def test_user_model_logic():
    u = User(username="Nour", email="nour@test.com", password="123", role="student")
    
    assert u.username == "Nour"
    assert u.email == "nour@test.com"
    assert u.role == "student"

def test_message_timestamp():
    msg = Message(messageID=1, sender="nour@test.com", receiver="malak@test.com", content="Hi")
    
    assert msg.time is not None