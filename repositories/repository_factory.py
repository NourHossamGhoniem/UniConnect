from repositories.user_repository import UserRepository
from repositories.club_repository import ClubRepository
from repositories.message_repository import MessageRepository
from repositories.join_repository import JoinRequestRepository

class RepositoryFactory:
    @staticmethod
    def get_repository(repo_type):
        """
        Factory method to return the correct repository instance
        based on the 'repo_type' string.
        """
        if repo_type == "user":
            return UserRepository()
        elif repo_type == "club":
            return ClubRepository()
        elif repo_type == "message":
            return MessageRepository()
        elif repo_type == "join":
            return JoinRequestRepository()
        else:
            raise ValueError(f"Unknown repository type: {repo_type}")