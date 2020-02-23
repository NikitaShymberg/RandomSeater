"""
The main script. Runs the algorithm to produce seating arrangement.
"""
from Family import Family
from utils import read_csv
from Hall import Hall, HallFullException


def sit_families(families: [Family], hall: Hall):
    """
    Attempts to seat all families in the given `hall`.
    Returns true is successful, raises HallFullException otherwise.
    """
    for fam in families:
        print(f'Seating {fam}')
        hall.sit(fam)
    return True


if __name__ == "__main__":
    families = read_csv('families.csv', Family)
    families.sort(key=lambda f: f.size, reverse=True)
    hall = Hall('rows.csv')
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
