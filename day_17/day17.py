def calculate_next_iteration(initial_state, size, current_iter):
    cells_to_check = set(initial_state)
    processed_cells = set()
    new_state = set()
    
    while len(cells_to_check) > 0:
        cell = cells_to_check.pop()

        processed_cells.add(cell)
        neighbours = generate_neighbours(*cell)
        for x, y, z, w in neighbours:
            if (-current_iter <= x <= size[0] + current_iter and
            -current_iter <= y <= size[1] + current_iter and
            -current_iter <= z <= size[2] + current_iter and
            -current_iter <= w <= size[3] + current_iter and
            (x,y,z,w) not in processed_cells):
                cells_to_check.add((x,y,z,w))

        active_neighbours = len(neighbours.intersection(initial_state))
        if (cell in initial_state and 1 < active_neighbours < 4 or
        cell not in initial_state and active_neighbours == 3):
            new_state.add(cell)
    return new_state

def generate_neighbours(x,y,z,w):
    neighbours = set()
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if i != x or j != y or k != z or l != w:
                        neighbours.add((i,j,k,l))
    return neighbours

if __name__ == "__main__":
    with open('day_17/input.txt') as input_file:
        initial_state = input_file.read().split('\n')
    
    active_cells = set()

    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] == '#':
                active_cells.add((i,j,0,0))

    for i in range(1, 7):
        active_cells = calculate_next_iteration(active_cells, (len(initial_state), len(initial_state[0]),0, 0), i)
    
    print(len(active_cells))
