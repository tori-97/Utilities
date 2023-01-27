from hashlib import sha512
from markupsafe import escape

class PString(str):
    def __init__(self, value: str) -> None:
        super().__init__()
    
    def hash2sha(self, mode: str = "512"):
        if mode == "512":
            return sha512(self.encode()).hexdigest()

        return None

    def escape(self):
        return str(escape(self))