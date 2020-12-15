def index_of_last(numbers, number):
    return len(numbers) - 1 - numbers[::-1].index(number)

def guess_number(start_list, turns):
    numbers_in_list = set(start_list[:-1])
    numbers = start_list.copy()

    for turn in range(len(numbers), turns):
        if numbers[turn-1] in numbers_in_list:
            new_number = index_of_last(numbers, numbers[turn-1]) - index_of_last(numbers[:-1], numbers[turn-1])
            numbers.append(new_number)
        else:
            numbers.append(0)
            numbers_in_list.add(numbers[turn-1])
    return numbers[len(numbers)-1]

def guess_number_v2(start_list, turns):
    numbers_in_list = {
        number: turn
    for turn, number in enumerate(start_list[:-1])}
    last_number = start_list[-1]

    for turn in range(len(numbers), turns):
        if last_number in numbers_in_list:
            prev = turn - 1
            before_that = numbers_in_list[last_number]
            previous_last_number = last_number
            last_number =  prev - before_that
            numbers_in_list[previous_last_number] = turn-1
        else:
            numbers_in_list[last_number] = turn-1
            last_number = 0

    return last_number

if __name__ == "__main__":
    numbers = [20,0,1,11,6,3]
    print(guess_number(numbers, 2020))
    print(guess_number_v2(numbers, 30000000))
