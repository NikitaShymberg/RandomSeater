"""
This file contains the hall class
"""
from copy import deepcopy
import datetime
import numpy as np
import random
from Family import Family
from Row import Row
from utils import read_csv


class HallFullException(Exception):
    """
    Indicates that the hall doesn't have a row with enough empty
    seats for the family.
    """
    pass


class Hall():
    """
    The Hall class. TODO: doc
    """
    def __init__(self, layout_csv_path: str):
        self.rows = []
        self.rows = read_csv(layout_csv_path, Row)
        self.empty_rows = deepcopy(self.rows)  # Used to reset the hall
        self._update_max_row_info()
        random.seed(datetime.datetime.now())

    def _update_max_row_info(self):
        self.max_row_idx = self.find_max_row_idx()
        self.max_row_size = self.rows[self.max_row_idx].free_spots

    def sit(self, fam: Family, debug=True) -> None:
        """
        Sits the given `fam` in a random available row.
        """
        if fam.size > self.max_row_size:
            raise HallFullException(
                f'Error: the hall is full! '
                f'Max empty row size: {self.max_row_size} '
                f'Current family size: {fam.size}'
            )

        available_rows_idx = [i for i, r in enumerate(self.rows)
                              if r.free_spots >= fam.size]
        row_idx = random.choice(available_rows_idx)
        self.rows[row_idx].sit(fam)

        # Update max_row_size
        if row_idx == self.max_row_idx:
            self._update_max_row_info()

        if debug:
            print('Family sat in row:', self.rows[row_idx].name)
            print(self)

    def find_max_row_idx(self) -> int:
        """
        Returns the index of the row with the most empty seats.
        """
        return np.argmax([r.free_spots for r in self.rows])

    def reset(self):
        """
        Removes all families from all rows.
        """
        self.rows = deepcopy(self.empty_rows)
        self._update_max_row_info()

    def __repr__(self):
        string = ''
        for row in self.rows:
            string += str(row) + '\n'
        return string


if __name__ == "__main__":
    hall = Hall('rows.csv')
    fams = [
        Family('1', 3),
        Family('1', 5),
        Family('1', 2),
        Family('1', 4),
    ]
    print(hall)
    for f in fams:
        hall.sit(f)
        print(hall.max_row_idx, hall.max_row_size)
