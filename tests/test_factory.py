from repositories.user_repository import UserRepository
from repositories.repository_factory import RepositoryFactory

def test_factory_creates_user_repo():
    repo = RepositoryFactory.get_repository("user")
    
    assert isinstance(repo, UserRepository)

def test_factory_invalid_input():
    try:
        RepositoryFactory.get_repository("pizza")
        assert False
    except ValueError:
        assert True