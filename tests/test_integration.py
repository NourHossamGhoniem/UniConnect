import os
from unittest.mock import patch

def test_integration_registration(client):
    
    test_filename = "test_integration.csv"
    
    
    real_path = os.path.join("data", test_filename)

    
    if os.path.exists(real_path):
        os.remove(real_path)

    with open(real_path, 'w') as f:
        f.write("username,email,password,role\n")

    with patch("repositories.user_repository.UserRepository.FILENAME", test_filename):
        
        response = client.post("/register", data={
            "username": "IntegrationTest",
            "email": "new@ust.edu.eg",
            "password": "pass"
        }, follow_redirects=True)

        assert response.status_code == 200
        
        with open(real_path, 'r') as f:
            content = f.read()
            assert "IntegrationTest" in content

    if os.path.exists(real_path):
        os.remove(real_path)