"""
The main script. Runs the algorithm to produce seating arrangement.
"""
import argparse
from Family import Family
from utils import read_csv
from Hall import Hall, HallFullException


def sit_families(families: [Family], hall: Hall) -> bool:
    """
    Attempts to seat all families in the given `hall`.
    Returns true is successful, raises HallFullException otherwise.
    """
    for fam in families:
        print(f'Seating {fam}')
        hall.sit(fam)
    return True


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows_path', required=True)
    parser.add_argument('--families_path', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    families = read_csv(args.families_path, Family)
    families.sort(key=lambda f: f.size, reverse=True)
    hall = Hall(args.rows_path)
    print('Found the following families:')
    print(*families, '\n', sep='\n')
    print(hall)

    families_are_sitting = False
    while not families_are_sitting:
        try:
            if sit_families(families, hall):
                families_are_sitting = True
        except HallFullException as e:
            print(e)
            hall.reset()

    hall.to_csv('output.csv')
