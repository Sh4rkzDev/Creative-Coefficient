def triangle(row: str) -> str:
    '''
    Returns the color resulting from the combinations of the given row.
    '''
    while len(row) > 1:
        next_row = ""
        for idx in range(len(row)-1):
            next_row += get_color(row[idx], row[idx+1])
        row = next_row
    return row

def get_color(a: str, b:str) -> str:
    if a == "R":
        if b == "R": return "R"
        if b == "G": return "B"
        if b == "B": return "G"
    if a == "B":
        if b == "R": return "G"
        if b == "G": return "R"
        if b == "B": return "B"
    if a == "G":
        if b == "R": return "B"
        if b == "G": return "G"
        if b == "B": return "R"
    raise ValueError("The color is not valid")
