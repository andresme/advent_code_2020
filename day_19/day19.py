import re

rule_regex = re.compile(r'(\d+):\ (.*)')

max_depth = 3

def get_regex(expr, rules):
    regex = ''
    sub_sections = expr.split(' | ')
    for sub_section in sub_sections:
        regex += '('
        sub_section = sub_section.strip()
        for sub_sub_section in sub_section.split(' '):
            sub_sub_section = sub_sub_section.strip()
            if sub_sub_section == '(' or sub_sub_section == ')':
                regex += sub_sub_section
            elif rules[sub_sub_section] == 'a' or rules[sub_sub_section] == 'b':
                regex += rules[sub_sub_section]
            else: 
                regex += '(' + get_regex(rules[sub_sub_section], rules) + ')'
        regex += ')|'
    return regex.replace('|)', ')')
    

if __name__ == "__main__":
    with open('day_19/input.txt') as input_file:
        rules, expressions  = input_file.read().split('\n\n')

    rules = rules.split('\n')
    expressions = expressions.split('\n')

    rules = {
        rule.split(':')[0]: rule.split(':')[1].strip().replace('"', '')
    for rule in rules}

    regex = re.compile(get_regex(rules['0'], rules)[:-1] + '$')
    print(sum([1 for expr in expressions if re.match(regex, expr)]))

    rules["8"] = "( 42 | 42 8 )"
    rules["11"] = "( 42 31 | 42 11 31 )"

    # Not proud but works...
    for i in range(max_depth):
        rules['8'] = rules['8'].replace('8', ' ( ' + rules['8'] + ' ) ')
        rules['11'] = rules['11'].replace('11', ' ( ' + rules['11'] + ' ) ')
    
    rules['11'] = rules['11'].replace('11', '').replace('  ', ' ')
    rules['8'] = rules['8'].replace('8', '').replace('  ', ' ')
    

    regex = get_regex(rules['0'], rules).replace('|)', ')')[:-1] + '$'
    print(sum([1 for expr in expressions if re.match(regex, expr)]))