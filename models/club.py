from dataclasses import dataclass, field
from typing import List

@dataclass
class Member:
    name: str
    email: str
    role: str = "Member"

@dataclass
class Club:
    id: int
    name: str
    description: str = ""
    category: str = ""
    members: List[Member] = field(default_factory=list)

@dataclass
class Office:
    id: int
    name: str
    description: str = ""
    members: List[Member] = field(default_factory=list)
