from dataclasses import dataclass,field

@dataclass
class Signal:
    id: str
    category: str
    weight: int
    reason: str

@dataclass
class Facts:
    verdict: str = "could not verify"
    score: int = 0
    signals: list = field(default_factory=list)