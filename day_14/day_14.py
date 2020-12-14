import re

address_regex = re.compile(r'mem\[(.*)\]')

def apply_mask(mask, number, wildcard):
    # Convert to binary
    binary_number = str(bin(int(number))).replace('0b', '').rjust(36, '0')
    binary_number = list(binary_number)

    # Apply mask
    for index, item in enumerate(mask):
        if item != wildcard:
            binary_number[index] = item
    
    return binary_number

def apply_address_mask(mask, number):
    addresses = []
    binary_number = apply_mask(mask, number, '0')

    # Generate all combinations
    stack = [binary_number]
    while len(stack) > 0:
        address = stack.pop()
        if address.count('X') > 0:
            new_address0 = address.copy()
            new_address1 = address.copy()
            for index, item in enumerate(address):
                if item == 'X':
                    new_address0[index] = '0'
                    new_address1[index] = '1'
                    break
            stack.extend([new_address0, new_address1])
        elif address.count('X') == 0:
            binary_number = int(''.join(address), 2)
            addresses.append(binary_number)
    
    return addresses

def write_to_memory(instructions, apply_mask_address=False):
    current_mask = ''
    memory = {}

    for line in instructions:
        instruction, argument = line.split(' = ')
        if instruction == 'mask':
            current_mask = argument
            continue
        
        address = int(re.match(address_regex, instruction).group(1))
        if apply_mask_address:
            addresses = apply_address_mask(current_mask, address)
            for address in addresses:
                memory[address] = int(argument)
        else:
            memory[address] = int(''.join(apply_mask(current_mask, argument, 'X')), 2)
        
    return memory

if __name__ == "__main__":
    with open('day_14/input.txt', 'r') as input_file:
        instructions = input_file.read().split('\n')
    
    memory = write_to_memory(instructions)
    total_sum = 0
    for _, value in memory.items():
        total_sum += value
    print(total_sum)

    memory = write_to_memory(instructions, True)
    total_sum = 0
    for _, value in memory.items():
        total_sum += value
    print(total_sum)
