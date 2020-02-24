"""
The main script. Runs the algorithm to produce seating arrangement.
"""
import argparse
import easygui
from Family import Family
from utils import read_csv
from Hall import Hall, HallFullException

SELECT_ROW_CSV_CHOICE = 'Row Layout'
SELECT_FAM_CSV_CHOICE = 'Families'
READY_CHOICE = 'Start!'
NUM_TRIES_BEFORE_WARN = 100


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
    parser.add_argument('--rows_path')
    parser.add_argument('--families_path')
    parser.add_argument('--output_path')
    parser.add_argument('--use_gui',
                        type=lambda x: True if x.lower() == 'true' else False)
    return parser.parse_args()


def get_csv_paths(args) -> (str, str):
    """
    If args.use_gui is true, shows a gui allowing
    the user to set the paths for the families and rows csv files.
    Otherwise uses args.rows_path and args.families_path.
    Returns a tuple with (families_path, rows_path).
    """
    if args.use_gui:
        rows_csv_path = None
        families_csv_path = None
        ready = False
        while not ready:
            choice = easygui.buttonbox(
                msg='Please choose a csv file with a seating layout and a csv '
                    'file with family information.'
                    '\nThe seating layout csv has two columns: name and length'
                    '\nThe families csv has two columns: name and size'
                    '\n\n\nCurrent selections\n'
                    f'Seating layout: {rows_csv_path}\n'
                    f'Families: {families_csv_path}\n',
                title='Setup hall and families',
                choices=[SELECT_ROW_CSV_CHOICE, SELECT_FAM_CSV_CHOICE,
                         READY_CHOICE]
            )
            if choice is None:
                quit()
            if choice == SELECT_FAM_CSV_CHOICE:
                families_csv_path = easygui.fileopenbox(
                    title='Family csv file',
                    filetypes=['*.csv'],  # FIXME: doesn't work
                )
            if choice == SELECT_ROW_CSV_CHOICE:
                rows_csv_path = easygui.fileopenbox(
                    title='Seating layout csv file',
                    filetypes=['*.csv'],  # FIXME: doesn't work
                )
            if choice == READY_CHOICE:
                if families_csv_path is None or rows_csv_path is None:
                    easygui.msgbox(
                        msg='Please select both a family information csv '
                        'and a seating layout csv.',
                        title='Not all csv files selected'
                    )
                else:
                    ready = True

    else:
        families_csv_path = args.families_path
        rows_csv_path = args.rows_path

    return families_csv_path, rows_csv_path


def get_output_path(args) -> str:
    """
    If args.use_gui is true, shows a gui allowing
    the user to set the path for the output csv.
    Otherwise uses args.output_path.
    Returns the output path to use.
    """
    if args.use_gui:
        easygui.msgbox(
            msg='Done! Everyone is seated. Please save the output csv file.'
        )
        return easygui.filesavebox(
            title='Choose an output csv file'
        )
    else:
        return args.output_path


if __name__ == "__main__":
    # Sort out command line args
    args = parse_args()
    families_csv_path, rows_csv_path = get_csv_paths(args)

    # Read csv files
    families = read_csv(families_csv_path, Family)
    families.sort(key=lambda f: f.size, reverse=True)
    hall = Hall(rows_csv_path)

    print('Found the following families:')
    print(*families, '\n', sep='\n')
    print(hall)

    # Seating loop
    families_are_sitting = False
    try_num = 0
    while not families_are_sitting:
        try_num += 1
        try:
            if sit_families(families, hall):
                families_are_sitting = True
        except HallFullException as e:
            print(e)
            hall.reset()
            if try_num % NUM_TRIES_BEFORE_WARN == 0 and args.use_gui:
                to_continue = easygui.boolbox(
                    msg=f'I wasn\'t able to find a suitable seating '
                    f'arangement in {try_num} tries. This is either '
                    'because I need to try some more times, '
                    'or no possible seating arangements exist.'
                    '\n\n Would you like to continue trying?'
                )
                if not to_continue:
                    quit()

    output_path = get_output_path(args)
    hall.to_csv(output_path)
