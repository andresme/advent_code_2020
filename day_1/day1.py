def solve_for_two(numbers, target):
    for i in numbers:
        seek_number = target - i
        # Check if seek_number is in the set
        # Also check that we are not looking for
        # the same number
        if seek_number in numbers and i != seek_number:
            return i, seek_number
    return None, None

def solve_for_three(numbers, target):
    for i in numbers:
        x, y = solve_for_two(numbers, 2020 - i)
        # Check if we have a possible answer
        # Also check we are not repeating numbers
        if x and y and i != x and i != y:
            return i, x, y



if __name__ == "__main__":
    with open('input.txt', 'r') as inputFile:
        numbers = {int(line) for line in inputFile.readlines()}
    res1_x, res1_y = solve_for_two(numbers, 2020)
    res2_x, res2_y, res3_z = solve_for_three(numbers, 2020)
    print(f'solution for two numbers: {res1_x * res1_y}')
    print(f'solution for three numbers: {res2_x * res2_y * res3_z}')
