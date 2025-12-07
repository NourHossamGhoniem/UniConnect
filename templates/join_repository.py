# repositories/join_repository.py
import os
import csv
from typing import List, Optional
from core.file_manager import FileManager
from models.join_request import JoinRequest

class JoinRequestRepository:
    """
    Repository for join requests. Uses the shared FileManager to read/append CSV.
    Updates are performed by rewriting the CSV file (simple and clear for beginners).
    """
    FIELDNAMES = ['id', 'student', 'club', 'status', 'created_at']

    def __init__(self):
        self.fm = FileManager()
        # Build path: project_root/data/join_requests.csv
        repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        data_dir = os.path.join(repo_dir, 'data')
        os.makedirs(data_dir, exist_ok=True)
        self.filename = os.path.join(data_dir, 'join_requests.csv')

    def get_all(self) -> List[JoinRequest]:
        """Return all join requests from CSV as model instances."""
        rows = self.fm.read_csv(self.filename) or []
        return [JoinRequest.from_dict(r) for r in rows]

    def get_by_club(self, club_id: str) -> List[JoinRequest]:
        """Return requests filtered by club id/name."""
        return [r for r in self.get_all() if r.club == club_id]

    def get_by_student(self, student_id: str) -> List[JoinRequest]:
        """Return requests filtered by student id/name."""
        return [r for r in self.get_all() if r.student == student_id]

    def add(self, jr: JoinRequest) -> None:
        """Append a new join request to the CSV."""
        # Ensure the directory exists (defensive)
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.fm.append_csv(self.filename, jr.to_dict(), self.FIELDNAMES)

    def update_status(self, request_id: str, new_status: str) -> bool:
        """
        Update the status of a request.
        Returns True if a row was updated, False if not found.
        """
        rows = self.fm.read_csv(self.filename) or []
        updated = False
        for row in rows:
            if row.get('id') == request_id:
                row['status'] = new_status
                updated = True

        if not updated:
            return False

        # Rewrite the entire CSV with updated rows (clear and easy to understand)
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            for row in rows:
                # Make sure each row has the expected keys
                writer.writerow({k: row.get(k, '') for k in self.FIELDNAMES})
        return True