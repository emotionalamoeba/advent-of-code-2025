import math

def perform_calc(column):
    operand = column[-1]
    values = [int(x) for x in column[:-1]]

    #print(f'Operand {operand} values {values}')

    if operand == '+':        
        return sum(values)
    
    if operand == '*':
        return math.prod(values)

def process():
    calculations = []
    with open('input.txt', 'r') as file:
        line_number = 0
        for line in file:
            line = line.strip()
            values = line.split()            
            for v in range(len(values)):                
                if line_number == 0:
                    calculations.append([])                    
                calculations[v].append(values[v])

            line_number += 1                     

    total = 0
    for c in calculations:
        total += perform_calc(c)

    #print(f'Calculations : {calculations}')
    print(f'Total {total}')

process()