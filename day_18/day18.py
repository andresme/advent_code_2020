import re

solvable_regex = re.compile(r'\(([0-9\ +*]+)\)')
sum_regex = re.compile(r"\d+ [\+ \d+| \+ \d+]+")

def eval_sum_first(expression):
    print(expression)
    while '+' in expression:
        for m in re.finditer(sum_regex, expression):
            sub_expression = m.group(0)
            print(sub_expression)
            result = eval(sub_expression)
            expression = expression.replace(sub_expression, str(result))
            print(expression)
    return eval(expression)

def eval_simple(expression):
    result = 0
    last_symbol = ''
    for i in expression.split(' '):
        if i.isnumeric():
            if last_symbol == '':
                result = int(i)
            elif last_symbol == '+':
                result += int(i)
            elif last_symbol == '*':
                result *= int(i)
        else:
            last_symbol = i
    return result

def eval_custom(expression, sum_first=False):
    while '(' in expression:
        for m in re.finditer(solvable_regex, expression):
            sub_expression = m.group(0)
            if sum_first:
                sub_expression_result = eval_sum_first(sub_expression.replace('(', '').replace(')', ''))
            else:
                sub_expression_result = eval_simple(sub_expression.replace('(', '').replace(')', ''))
            expression = expression.replace(sub_expression, str(sub_expression_result))
    if sum_first:
        return eval_sum_first(expression)
    else:
        return eval_simple(expression)

if __name__ == "__main__":
    with open('day_18/input.txt') as input_file:
        expressions = input_file.read().split('\n')
    
    print(sum([eval_custom(i) for i in expressions]))
    print(sum([eval_custom(i, sum_first=True) for i in expressions]))
