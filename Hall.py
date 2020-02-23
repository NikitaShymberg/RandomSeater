"""
This file contains the hall class
"""
import csv
import numpy as np
from Family import Family
from Row import Row


class HallFullException(Exception):
    """
    Indicates that the hall doesn't have a row with enough empty
    seats for the family.
    """
    pass


class CSVParseException(Exception):
    """
    Indicates that the provided csv file structure is incorrect.
    """
    pass


class Hall():
    """
    The Hall class. TODO: doc
    """
    def __init__(self, layout_csv_path: str):
        self.rows = []
        self._setup_rows(layout_csv_path)
        self.max_row_idx = np.argmax([r.max_length for r in self.rows])
        self.max_row_size = self.rows[self.max_row_idx].max_length

    def _setup_rows(self, layout_csv_path):
        """
        Reads the row layout from the given `layout_csv_path` and
        arranges the rows in self accordingly.
        """
        with open(layout_csv_path) as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            if len(headers) != 2:
                raise CSVParseException(
                    f'Too many columns in {layout_csv_path}, '
                    'expected 2, found {len(headers)}'
                )

            row_name = headers[0]
            row_size = headers[1]
            for csv_row in reader:
                try:
                    row = Row(csv_row[row_name], int(csv_row[row_size]))
                except ValueError:
                    raise CSVParseException(
                        f'Invalid row format in {layout_csv_path} '
                        'found row {csv_row}'
                    )
                self.rows.append(row)

    def sit(self, fam: Family):
        """
        Sits the given `fam` in a random available row.
        """
        if fam.size > self.max_row_size:
            raise HallFullException(
                f'Error: the hall is full! '
                'Max empty row size: {self.max_row_size} '
                'Current family size: {fam.size}'
            )


if __name__ == "__main__":
    hall = Hall('rows.csv')
    print(hall.max_row_idx)
    print(hall.max_row_size)
