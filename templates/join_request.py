# models/join_request.py
import uuid
from datetime import datetime
from typing import Dict

class JoinRequest:
    """
    Simple model for a join request.
    Fields:
      - id: unique string id (UUID)
      - student: student id or name
      - club: club id or name
      - status: 'pending' | 'approved' | 'rejected'
      - created_at: ISO timestamp when created
    """
    def __init__(self, student: str, club: str, status: str = 'pending',
                 id: str = None, created_at: str = None):
        # generate id and timestamp if not provided
        self.id = id or str(uuid.uuid4())
        self.student = student
        self.club = club
        self.status = status
        self.created_at = created_at or datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, str]:
        """Convert model to dict for CSV storage."""
        return {
            'id': self.id,
            'student': self.student,
            'club': self.club,
            'status': self.status,
            'created_at': self.created_at
        }

    @staticmethod
    def from_dict(d: Dict[str, str]) -> "JoinRequest":
        """Create a JoinRequest from a dict (e.g., read from CSV)."""
        return JoinRequest(
            student=d.get('student', ''),
            club=d.get('club', ''),
            status=d.get('status', 'pending'),
            id=d.get('id'),
            created_at=d.get('created_at')
        )