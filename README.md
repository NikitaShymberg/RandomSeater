# RandomSeater

Input:
    - csv containing seating layout
    - csv containing family info

Output:
    - csv containing seats per fam

Objects:
    - Family
        - Name
        - Number
    - Row
        - Name
        - Total number of spots
        - Number of free spots
        - Occupants
    - Hall
        - Rows
        - Number of max free spots
        - Row with max free spots

Algorithm:
    fams = sort(fams from biggest to smallest)
    for fam in fams:
        while fam.is_not_seated():
            if fam.size > hall.max_row_size:
                restart
            row = hall.choose_rand_row()
            if row.free_spots < fam.size:
                row.sit(fam)