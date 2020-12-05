def get_row_column(ticket):
    row = [0, 127]
    column = [0, 7]
    for letter in ticket:
        if letter == 'F':
            row[1] = (row[0] + row[1]) // 2
        elif letter == 'B':
            row[0] = (row[0] + row[1] + 1) // 2
        elif letter == 'L':
            column[1] = (column[0] + column[1]) // 2
        elif letter == 'R':
            column[0] = (column[0] + column[1] + 1) // 2
    return row[0], column[0]
    

if __name__ == "__main__":
    ticket_ids = []
    with open('day_5/input.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            ### ALWAYS STRIP THE LINE!!!!!
            row, column = get_row_column(line.strip())
            ticket_ids.append(row * 8 + column)
        print(max(ticket_ids))
        print(len(ticket_ids))

        for seat in set(ticket_ids):
            if seat + 2 in ticket_ids and not seat + 1 in ticket_ids:
                print(seat+1)
