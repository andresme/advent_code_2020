
# from day 1
def solve_for_two(numbers, target):
    for i in numbers:
        seek_number = target - i
        if seek_number in numbers and i != seek_number:
            return i, seek_number
    return None, None

def find_contiguous(numbers, target, length):
    for i in range(len(numbers)):
        sum_for_range = sum(numbers[i:i+length])
        if sum_for_range == target:
            return numbers[i:i+length]
    return None

if __name__ == "__main__":
    with open('day_9/input.txt', 'r') as inputFile:
        encrypted = inputFile.read().split('\n')
    encrypted = [int(i) for i in encrypted]
    
    for index in range(25, len(encrypted)):
        available_numbers = set(encrypted[index-25:index])
        x, y = solve_for_two(available_numbers, encrypted[index])
        if not x and not y:
            weakness_1 = encrypted[index]
            break

    print(weakness_1)
    
    for i in range(2, len(encrypted)):
        result = find_contiguous(encrypted, weakness_1, i)
        if result != None:
            print(result)
            break
    print(sum(result))
    print(min(result) + max(result))
    