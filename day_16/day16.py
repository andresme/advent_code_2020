import re
from collections import defaultdict

TICKET_RULE_REGEX = re.compile(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)')

def check_rule(field, rule):
    return rule[0][0] <= field <= rule[0][1] or rule[1][0] <= field <= rule[1][1]
         

def check_fields(ticket, rules):
    for i in ticket:
        for j in rules.values():
            if check_rule(i, j):
                break
        else:
            return i
    return -1

if __name__ == "__main__":
    with open('day_16/input.txt', 'r') as input_file:
        tickets = input_file.read().split('\n')
    
    ticket_rules = {}

    current_line = 0
    while tickets[current_line] != '':
        ticket_rule_match = TICKET_RULE_REGEX.match(tickets[current_line])
        ticket_rules[ticket_rule_match.group(1)] = ((int(ticket_rule_match.group(2)), int(ticket_rule_match.group(3))), 
                                                    (int(ticket_rule_match.group(4)), int(ticket_rule_match.group(5))))
        current_line += 1
    
    current_line += 2
    my_ticket = [int(ticket) for ticket in tickets[current_line].split(',')]

    current_line += 2
    nearby_tickets = [[int(ticket) for ticket in tickets[idx].split(',')] for idx in range(current_line+1, len(tickets))]
    ticket_check = [check_fields(ticket, ticket_rules) for ticket in nearby_tickets]
    invalid_tickets = [ticket for ticket in ticket_check if ticket >= 0]
    error_rate = sum(invalid_tickets)
    print(error_rate)

    possible_fields = {}
    valid_tickets = []
    for idx in range(len(ticket_check)):
        if ticket_check[idx] == -1:
            valid_tickets.append(nearby_tickets[idx])
    

    for ticket_field in range(len(valid_tickets[0])):
        fields = list(ticket_rules.keys())
        possible_fields_for_ticket_field = []
        while len(fields) > 0:
            field = fields.pop(0)
            for ticket in valid_tickets:
                if not check_rule(ticket[ticket_field], ticket_rules[field]):
                    break
            else:
                possible_fields_for_ticket_field.append(field)
        possible_fields[ticket_field] = possible_fields_for_ticket_field

    possible_fields_reverse = defaultdict(list)
    for ticket_field in ticket_rules.keys():
        for ticket_field_2 in possible_fields:
            if ticket_field in possible_fields[ticket_field_2]:
                possible_fields_reverse[ticket_field].append(ticket_field_2)
    
    unique_list = []
    processed = set()
    for value in possible_fields_reverse.values():
        if len(value) == 1:
            if len(value) == 1 and not value[0] in processed:
                unique_list.append(value[0])
                processed.add(value[0])

    while len(unique_list) > 0: 
        unique = unique_list.pop(0)
        for field in possible_fields_reverse:
            if len(possible_fields_reverse[field]) > 1 and unique in possible_fields_reverse[field]:
                possible_fields_reverse[field].remove(unique)
        for value in possible_fields_reverse.values():
            if len(value) == 1 and not value[0] in processed:
                unique_list.append(value[0])
                processed.add(value[0])
    
    multiplication = 1
    for key in possible_fields_reverse:
        if key.startswith('departure'):
            multiplication *= my_ticket[possible_fields_reverse[key][0]]
    
    print(multiplication)