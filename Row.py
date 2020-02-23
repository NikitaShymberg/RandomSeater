"""
This file contains the Row class
"""
import random
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
        self.families = []
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

        self.families.append(fam)
        self.free_spots -= fam.size

    def _create_seat_number(self, seat_number: int) -> str:
        """
        Returns a string in the format 'self.name seat_number' (no space).
        """
        return f'{self.name}{seat_number}'

    def assign_seats(self) -> None:
        """
        Assigns random adjacent seat numbers to all the families in this row.
        """
        random.shuffle(self.families)
        seats = [self._create_seat_number(i) for i in range(self.max_length)]
        seat_num = 0
        for fam in self.families:
            cur_seats = seats[seat_num:seat_num + fam.size]
            fam.assign_seats(cur_seats)
            seat_num += fam.size

    def __repr__(self):
        string = f'Row: {self.name}, '
        string += f'Max: {self.max_length}, '
        string += f'Remaining: {self.free_spots}'
        return string
