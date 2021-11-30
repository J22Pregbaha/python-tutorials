# Given two cells on the standard chess board, determine whether they have the same color or not.
def solution(cell1, cell2):
    white = ["A2", "A4", "A6", "A8",
             "B1", "B3", "B5", "B7",
             "C2", "C4", "C6", "C8",
             "D1", "D3", "D5", "D7",
             "E2", "E4", "E6", "E8",
             "F1", "F3", "F5", "F7",
             "G2", "G4", "G6", "G8",
             "H1", "H3", "H5", "H7"]

    if cell1 in white and cell2 in white:
        return True
    elif cell1 not in white and cell2 not in white:
        return True
    return False

print(solution("A1", "C3"))