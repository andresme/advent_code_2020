def get_occupied_for_position(layout, pos):
    x, y = pos
    count = 0
    while x > 0:
        x -= 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while x < len(layout)-1:
        x += 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while y > 0:
        y -= 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while y < len(layout[x])-1:
        y += 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while x > 0 and y > 0:
        x -= 1
        y -= 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while x > 0 and y < len(layout[x])-1:
        x -= 1
        y += 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while x < len(layout)-1 and y > 0:
        x += 1
        y -= 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    x, y = pos
    while x < len(layout)-1 and y < len(layout[x])-1:
        x += 1
        y += 1
        if layout[x][y] == '#':
            count += 1
            break
        elif layout[x][y] == 'L':
            break
    return count



def get_adjacent_occupied_count_v1(layout, pos):
    x, y = pos
    x_min = max(0, x-1)
    x_max = min(x + 2, len(layout))
    y_min = max(0, y-1)
    y_max = min(y + 2, len(layout[x]))
    count = 0
    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if i == pos[0] and j == pos[1]:
                continue
            if layout[i][j] == '#':
                count += 1
    return count

def count_occupied_total(layout):
    occupied_count = 0
    for i in layout:
        for j in i:
            if j == '#':
                occupied_count += 1
    return occupied_count

def update_layout(layout, count_occupied_func, adjacent_count_rule):
    next_layout = layout.copy()
    changed = False
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            adjacent_count = count_occupied_func(layout, (i,j))
            if layout[i][j] == 'L' and adjacent_count == 0:
                changed = True
                next_layout[i] = next_layout[i][:j] + '#' + next_layout[i][j+1:]
            elif layout[i][j] == '#' and adjacent_count >= adjacent_count_rule:
                changed = True
                next_layout[i] = next_layout[i][:j] + 'L' + next_layout[i][j+1:]
    return next_layout, changed

if __name__ == "__main__":
    with open('day_11/input.txt', 'r') as inputFile:
        original_layout = inputFile.read().split('\n')
    
    
    layout = original_layout.copy()
    while True:
        layout, changed = update_layout(layout, get_adjacent_occupied_count_v1, 4)
        if not changed:
            break

    print(count_occupied_total(layout))

    layout = original_layout.copy()
    while True:
        layout, changed = update_layout(layout, get_occupied_for_position, 5)
        if not changed:
            break
    
    print(count_occupied_total(layout))
