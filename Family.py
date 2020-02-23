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
        self.seats = None

    def assign_seats(self, seats: [str]) -> None:
        """
        Assigns this family the seats in `seats`.
        """
        self.seats = seats

    def __repr__(self):
        string = f'Family {self.name} - size {self.size} - seat {self.seats}'
        return string
