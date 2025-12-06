import csv
from typing import List, Dict, Optional
from core.file_manager import FileManager
from models.club import Club, Office, Member

class ClubRepository:
    def __init__(self, data_dir: str = "data"):
        self.fm = FileManager()
        self.clubs_file = f"{data_dir}/clubs.csv"
        self.offices_file = f"{data_dir}/offices.csv"
        self.members_file = f"{data_dir}/members.csv"

    def _next_id(self, rows: List[Dict[str,str]]) -> int:
        ids = [int(r["id"]) for r in rows if r.get("id")]
        return max(ids) + 1 if ids else 1

    def list_clubs(self) -> List[Club]:
        rows = self.fm.read_csv(self.clubs_file) or []
        members = self._load_members()
        result = []
        for r in rows:
            cid = int(r["id"])
            club_members = [Member(name=m["name"], email=m["email"], role=m["role"]) for m in members if m["entity"]=="club" and int(m["entity_id"])==cid]
            c = Club(id=cid, name=r.get("name",""), description=r.get("description",""), category=r.get("category",""), members=club_members)
            result.append(c)
        return result

    def get_club(self, club_id: int) -> Optional[Club]:
        rows = self.fm.read_csv(self.clubs_file) or []
        for r in rows:
            if int(r["id"]) == club_id:
                members = self._load_members()
                club_members = [Member(name=m["name"], email=m["email"], role=m["role"]) for m in members if m["entity"]=="club" and int(m["entity_id"])==club_id]
                return Club(id=club_id, name=r.get("name",""), description=r.get("description",""), category=r.get("category",""), members=club_members)
        return None

    def create_club(self, name: str, description: str = "", category: str = "") -> Club:
        rows = self.fm.read_csv(self.clubs_file) or []
        nid = self._next_id(rows)
        data = {"id": nid, "name": name, "description": description, "category": category}
        self.fm.append_csv(self.clubs_file, data, ["id","name","description","category"])
        return Club(id=nid, name=name, description=description, category=category)

    def update_club(self, club_id: int, name: str, description: str, category: str) -> bool:
        rows = self.fm.read_csv(self.clubs_file) or []
        changed = False
        for r in rows:
            if int(r["id"]) == club_id:
                r["name"] = name
                r["description"] = description
                r["category"] = category
                changed = True
        if changed:
            self._write_csv(self.clubs_file, rows, ["id","name","description","category"])
        return changed

    def delete_club(self, club_id: int) -> bool:
        rows = self.fm.read_csv(self.clubs_file) or []
        new = [r for r in rows if int(r["id"]) != club_id]
        if len(new) == len(rows):
            return False
        self._write_csv(self.clubs_file, new, ["id","name","description","category"])
        members = self._load_members()
        members = [m for m in members if not (m["entity"]=="club" and int(m["entity_id"])==club_id)]
        self._write_csv(self.members_file, members, ["entity","entity_id","name","email","role"])
        return True

    def list_offices(self) -> List[Office]:
        rows = self.fm.read_csv(self.offices_file) or []
        members = self._load_members()
        result = []
        for r in rows:
            oid = int(r["id"])
            office_members = [Member(name=m["name"], email=m["email"], role=m["role"]) for m in members if m["entity"]=="office" and int(m["entity_id"])==oid]
            o = Office(id=oid, name=r.get("name",""), description=r.get("description",""), members=office_members)
            result.append(o)
        return result

    def get_office(self, office_id: int) -> Optional[Office]:
        rows = self.fm.read_csv(self.offices_file) or []
        for r in rows:
            if int(r["id"]) == office_id:
                members = self._load_members()
                office_members = [Member(name=m["name"], email=m["email"], role=m["role"]) for m in members if m["entity"]=="office" and int(m["entity_id"])==office_id]
                return Office(id=office_id, name=r.get("name",""), description=r.get("description",""), members=office_members)
        return None

    def create_office(self, name: str, description: str = "") -> Office:
        rows = self.fm.read_csv(self.offices_file) or []
        nid = self._next_id(rows)
        data = {"id": nid, "name": name, "description": description}
        self.fm.append_csv(self.offices_file, data, ["id","name","description"])
        return Office(id=nid, name=name, description=description)

    def update_office(self, office_id: int, name: str, description: str) -> bool:
        rows = self.fm.read_csv(self.offices_file) or []
        changed = False
        for r in rows:
            if int(r["id"]) == office_id:
                r["name"] = name
                r["description"] = description
                changed = True
        if changed:
            self._write_csv(self.offices_file, rows, ["id","name","description"])
        return changed

    def delete_office(self, office_id: int) -> bool:
        rows = self.fm.read_csv(self.offices_file) or []
        new = [r for r in rows if int(r["id"]) != office_id]
        if len(new) == len(rows):
            return False
        self._write_csv(self.offices_file, new, ["id","name","description"])
        members = self._load_members()
        members = [m for m in members if not (m["entity"]=="office" and int(m["entity_id"])==office_id)]
        self._write_csv(self.members_file, members, ["entity","entity_id","name","email","role"])
        return True

    def add_member(self, entity: str, entity_id: int, name: str, email: str, role: str = "Member") -> bool:
        data = {"entity": entity, "entity_id": entity_id, "name": name, "email": email, "role": role}
        self.fm.append_csv(self.members_file, data, ["entity","entity_id","name","email","role"])
        return True

    def assign_role(self, entity: str, entity_id: int, email: str, new_role: str) -> bool:
        members = self._load_members()
        changed = False
        for m in members:
            if m["entity"] == entity and int(m["entity_id"]) == entity_id and m["email"] == email:
                m["role"] = new_role
                changed = True
        if changed:
            self._write_csv(self.members_file, members, ["entity","entity_id","name","email","role"])
        return changed

    def _load_members(self) -> List[Dict[str,str]]:
        rows = self.fm.read_csv(self.members_file) or []
        return rows

    def _write_csv(self, path: str, rows: List[Dict[str,str]], fieldnames: List[str]):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow({k: r.get(k,"") for k in fieldnames})
