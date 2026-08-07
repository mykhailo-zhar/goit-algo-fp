from typing import Self


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Self | None = None

    def __repr__(self) -> str:
        return f"Node({self.data.__repr__()})"
