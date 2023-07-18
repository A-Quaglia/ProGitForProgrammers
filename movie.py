from dataclasses import dataclass, field


@dataclass
class Movie:
    title: str
    authors: field(default_factory=list)
