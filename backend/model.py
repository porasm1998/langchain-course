from typing import List, Dict

class Students:
    def __init__(self, name: str, roll_no: str, subjects: List[str], marks: Dict[str, str]):
        self.name = name
        self.roll_no = roll_no
        self.subjects = subjects
        self.marks = marks

s1 = Students("Poras", "001", ["Math", "Science"], {"Math": "90", "Science": "95"})
print(s1.name)