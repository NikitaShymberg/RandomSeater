"""
Contains common functions used across multiple files.
"""
import csv


class CSVParseException(Exception):
    """
    Indicates that the provided csv file structure is incorrect.
    """
    pass


def read_csv(path, class_type):
    """
    Reads the csv file at `path`,
    returns a list of objects of type `class_type`
    initialized using the parameters in the csv file.
    The csv file must have two columns - name and size.
    """
    objects = []
    with open(path) as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        if len(headers) != 2:
            raise CSVParseException(
                f'Too many columns in {path}, '
                'expected 2, found {len(headers)}'
            )

        row_name = headers[0]
        row_size = headers[1]
        for csv_row in reader:
            try:
                obj = class_type(csv_row[row_name], int(csv_row[row_size]))
            except ValueError:
                raise CSVParseException(
                    f'Invalid csv format in {path} '
                    f'found row {csv_row}'
                )
            objects.append(obj)

    return objects
