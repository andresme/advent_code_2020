def run_program(instructions):
    pointers_processed = set()
    accumulator = 0
    pointer = 0
    while pointer not in pointers_processed and pointer < len(instructions):
        pointers_processed.add(pointer)
        operation, argument = instructions[pointer].split(' ')
        if operation == 'acc':
            accumulator += int(argument)
            pointer += 1
        elif operation == 'jmp':
            pointer += int(argument)
        else:
            pointer += 1
    return accumulator, pointer

if __name__ == "__main__":
    with open('day_8/input.txt', 'r') as inputFile:
        instructions = inputFile.read().split('\n')
    
    print(run_program(instructions)[0])

    for i in range(len(instructions)):
        instructions_temp = instructions.copy()
        operation, argument = instructions_temp[i].split(' ')
        if operation == 'jmp':
            instructions_temp[i]  = ' '.join(['nop', argument])
        elif operation == 'nop':
            instructions_temp[i]  = ' '.join(['jmp', argument])
        else:
            continue

        accum, pointer = run_program(instructions_temp)
        if pointer == len(instructions_temp):
            print(i)
            print(accum)
            break
   