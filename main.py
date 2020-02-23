"""
The main script. Runs the algorithm to produce seating arrangement.
"""
import csv
from Family import Family


def load_families(path: str) -> [Family]:
    """
    Reads the families csv located at `path` and returns a list
    of Family objects.
    """
    fams = []
    with open(path) as f:
        reader = csv.DictReader(f)



if __name__ == "__main__":
    families = load_families('families.csv')
    families.sort(key=lambda f: f.size, reverse=True)
