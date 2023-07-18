from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Book:
    title: str
    authors: field(default_factory=list)
    publication_date: datetime
