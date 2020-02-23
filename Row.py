"""
This file contains the Row class
"""
from Family import Family


class RowFullException(Exception):
    """
    Indicates that a row doesn't have enough empty seats.
    """
    pass


class Row():
    """
    The Family class. Each row has a length, a name,
    the number of free spots, and the seated families.
    """
    def __init__(self, name: str, max_length: int):
        self.name = name
        self.max_length = max_length
        self.fams = []
        self.free_spots = max_length

    def sit(self, fam: Family) -> None:
        """
        Asssigns a family into the row. Doesn't yet allocate seats.
        """
        if self.free_spots < fam.size:
            raise RowFullException(f'Error: attempted to sit family {fam.name}'
                                   f' with {fam.size} people into a row with '
                                   f'{self.free_spots} free spots'
                                   )

        self.fams.append(fam)
        self.free_spots -= fam.size

    def assign_seats(self):
        """
        Assigns seat numbers to all the families in this row.
        """
        ...  # TODO: write

    def __str__(self):
        string = f'Row: {self.name}, '
        string += f'Max: {self.max_length}, '
        string += f'Remaining: {self.free_spots}'
        return string
