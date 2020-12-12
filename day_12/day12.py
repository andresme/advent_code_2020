import re

command_regex = re.compile(r'([A-Za-z])(\d+)')
directions = ['N', 'E', 'S', 'W']


def move_ship(command, pos, direction):
    action, argument = command
    if action == 'F':
        action = directions[direction]
    if action == 'N':
        return ((pos[0]-argument, pos[1]), direction)
    elif action == 'S':
        return ((pos[0]+argument, pos[1]), direction)
    elif action == 'E':
        return ((pos[0], pos[1]+argument), direction)
    elif action == 'W':
        return ((pos[0], pos[1]-argument), direction)
    elif action == 'L':
        total_rotations = argument//90
        direction = (direction - total_rotations) % len(directions)
        return (pos, direction)
    elif action == 'R':
        total_rotations = argument//90
        direction = (direction + total_rotations) % len(directions)
        return (pos, direction)

def move_ship_v2(command, pos, waypoint):
    action, argument = command
    if action == 'F':
        return ((pos[0]+waypoint[0]*argument, pos[1]+waypoint[1]*argument), waypoint)
    if action == 'N':
        return (pos, (waypoint[0]+argument, waypoint[1]))
    elif action == 'S':
        return (pos, (waypoint[0]-argument, waypoint[1]))
    elif action == 'E':
        return (pos, (waypoint[0], waypoint[1]+argument))
    elif action == 'W':
        return (pos, (waypoint[0], waypoint[1]-argument))
    elif action == 'L':
        total_rotations = argument//90
        for _ in range(total_rotations):
            waypoint = (waypoint[1], -waypoint[0])
        return (pos, waypoint)
    elif action == 'R':
        total_rotations = argument//90
        for _ in range(total_rotations):
            waypoint = (-waypoint[1], waypoint[0])
        return (pos, waypoint)


if __name__ == "__main__":
    commands = []

    with open('input.txt', 'r') as input_file:
        commands_input = input_file.read().split('\n')
    for command in commands_input:
        command = re.match(command_regex, command)
        commands.append((command.group(1), int(command.group(2))))
    
    pos = (0,0)
    waypoint = (1, 10)
    direction = 1
    for command in commands:
        pos, direction = move_ship(command, pos, direction)
    print(abs(pos[1]) + abs(pos[0]))

    pos = (0,0)
    waypoint = (1, 10)
    direction = 1
    for command in commands:
        pos, waypoint = move_ship_v2(command, pos, waypoint)
    print(abs(pos[1]) + abs(pos[0]))

