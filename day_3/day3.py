def countTrees(grid, right, down):
    trees = 0
    right_accum = right
    down_accum = down
    while down_accum < len(grid):
        fixed_right = right_accum % len(grid[down_accum])
        if grid[down_accum][fixed_right] == '#':
            trees = trees + 1
        right_accum += right
        down_accum += down
    return trees

if __name__ == "__main__":
    grid = []
    with open('day_3/input.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            grid.append(line.replace('\n', ''))


    a,b,c,d,e = (countTrees(grid, 1, 1), countTrees(grid, 3, 1), countTrees(grid, 5, 1),
                 countTrees(grid, 7, 1), countTrees(grid, 1, 2))

    print(f"trees: {a}")
    print(f"trees: {b}")
    print(f"trees: {c}")
    print(f"trees: {d}")
    print(f"trees: {e}")
    print(f"multiplication: {a*b*c*d*e}")
