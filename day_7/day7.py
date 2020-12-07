import re
from collections import defaultdict

def get_amount_of_bags(bag_type, bag_rules):
    sub_bags = bag_rules[bag_type]
    total = 0
    for amount, bag in sub_bags:
        total += amount + amount * get_amount_of_bags(bag, bag_rules)
    return total

def get_bags_that_contains(bag_type, bag_rules):
    possible_bags = [bag_type]
    processed = set()

    while len(possible_bags) > 0:
        bag = possible_bags.pop()
        for new_bag in bag_rules_reverse[bag]:
            if new_bag not in processed:
                possible_bags.append(new_bag)
                processed.add(new_bag)
    return processed

def get_amount_and_type(line):
    m = re.search(r'(\d+) ([a-z ]+) bags?', line)
    bag_amount = m.group(1)
    bag_type = m.group(2)
    return bag_amount, bag_type

if __name__ == "__main__":
    bag_rules_reverse = defaultdict(set)
    bag_rules = defaultdict(list)
    
    with open('day_7/input.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            bag_type = line.split('bags')[0].strip()
            possible_bags = line.split('contain')[1].strip()
            if possible_bags != 'no other bags.':
                bags = [get_amount_and_type(bag) for bag in possible_bags.split(',')]
                for amount, bag in bags:
                    bag_rules_reverse[bag] |= {bag_type}
                    bag_rules[bag_type] += [(int(amount), bag)]
    
    bags_for_shiny_gold = get_bags_that_contains('shiny gold', bag_rules_reverse)
    print(len(bags_for_shiny_gold))
    
    total_bags = get_amount_of_bags('shiny gold', bag_rules)
    print(total_bags)

            
                
