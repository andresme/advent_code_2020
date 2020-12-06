def get_group_answers(content, append_operation):
    answers = []
    current_group = []
    for line_index in range(len(content)):
        person_answers = {letter for letter in content[line_index]}
        
        if len(person_answers) > 0:
            current_group.append(person_answers)

        if len(person_answers) == 0 or line_index == len(content) - 1:
            if append_operation == 'union': 
                operation_result = current_group[0].union(*current_group[1:])
            elif append_operation == 'intersection':
                operation_result = current_group[0].intersection(*current_group[1:])
            answers.append(operation_result)
            current_group = []

    return answers


if __name__ == "__main__":
    answers = []
    with open('input.txt', 'r') as inputFile:
        content = inputFile.read()
    
    answers = get_group_answers(content.split('\n'), 'union')
    print(f'part 1 answer: {sum([len(i) for i in answers])}')

    answers = get_group_answers(content.split('\n'), 'intersection')
    print(f'part 2 answer: {sum([len(i) for i in answers])}')
