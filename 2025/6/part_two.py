import math

def perform_calc(column, operand):
    value_strings = column[:-1]
    digit_count = [len(x) for x in value_strings]

    total = 0
    values = []
    print(f'Digit count {digit_count}')
    for i in range (0, max(digit_count) - 1):
        digits = ''
        for x in value_strings:    
            digits += x[i]
        print(f'i {i} digits "{digits}"')
        
        if len(digits.strip()) > 0:
            values.append(int(digits))

    print(f'Values {values} operand "{operand}"')
    if operand == '+':        
        total += sum(values)
    
    if operand == '*':
        total += math.prod(values)

    #print(f'Operand {operand} values {values}')
    return total


def process():
    filename = 'input.txt'
    calculations = []
    last_line = ''
    with open(filename, 'r') as file:
        for line in file:
            pass
        last_line = line

    positions = [index for index, char in enumerate(last_line) if char != ' ']

    print(f'Positions {positions}')
    for index in positions:
        calculations.append([])

    with open(filename, 'r') as file:
        line_number = 0
        for line in file:
            if line == last_line:
                pass
            
            for p in range(len(positions)):
                start_index = positions[p]
                end_index = len(line)
                if p < len(positions) - 1:
                    end_index = positions[p+1]

                calculations[p].append(line[start_index: end_index])                
            line_number += 1

    total = 0
    for index, c in enumerate(calculations):
        total += perform_calc(c, last_line.split()[index])

    print(f'Total {total}')

process()