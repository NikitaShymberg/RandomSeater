"""
This file contains the Family class
"""


class Family():
    """
    The Family class. Each family has a name, the number of members,
    and their spots.
    """
    def __init__(self, name: str, num_members: int):
        self.name = name
        self.size = num_members
        self.row = None