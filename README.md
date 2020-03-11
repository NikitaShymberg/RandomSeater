# RandomSeater

## Description
Some highschools host graduation ceremonies annually. One of the challenges of this is seating all attendees in the hall. It is unfair to do this task manually as some families will have better seats than others, and parents will notice this and complain - for pretty good reason. This is where this program comes in - as input, it takes the seating layout of the hall and the families attending the ceremony. It then randomly assigns seats to each family in the hall such that every family sits all together in one row. This program output the assigned seats for each family.

## Usage
- Command line
    - python main.py --rows_path=PATH_TO_ROWS.CSV --families_path=PATH_TO_FAMILIES.CSV --output_path=PATH_TO_OUTPUT.CSV --use_gui=False
- GUI
    - python main.py --use_gui=True
    - _OR_
    - python RandomSeaterGUI.py
- Prebuilt executable
    - On Mac OS just double click RandomSeater.tbz

## Input format
- Rows.csv
    - Two columns: row name and number of seats in the row. Row headings are not important but must exist.
    - Note that a row is defined as a set of seats wherein a family may be seated, so if a hall has a column of seats missing, the rows on either side of the missing column are not the same. See example (Rn is row n, X is a missing seat):

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1  | R1  | R1  | X   | X   | R2  | R2  | R2  |
| R3  | R3  | R3  | X   | X   | R4  | R4  | R4  |
| R5  | R5  | R5  | X   | X   | R6  | R6  | R6  |
    
- Families.csv
    - Two columns: family name and number of family members. Row headings are not important but must exist.

---

### Difficulties / New things learned
- First time building a python application!
- Building for mac - had to be done on a mac os machine.
  - I don't own a mac so I had to remote desktop into my parents' and build in there.
- Finding a way to make it executable just by double clicking
  - Ended up making a stack overflow post. Turned out I just needed to compress the executable into a .tbz archive.
- First time using the csv module.