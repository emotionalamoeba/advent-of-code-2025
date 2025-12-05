digits_needed = 12

def evaluate_from_start_index(batteries, start_index, digit):
    if digit >= digits_needed:
        return None

    from_end = digits_needed - 1 - digit

    if digit == digits_needed - 1:
        search_array = batteries[start_index:]
    else:
        search_array = batteries[start_index:-from_end]

    max_digit = max(search_array)
    next_start_index = start_index + search_array.index(max_digit) + 1

    next_result = evaluate_from_start_index(batteries, next_start_index, digit + 1)
    
    if next_result == None:
        return max_digit

    return max_digit + next_result

def process():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:            
            batteries = line.strip()
            value = int(evaluate_from_start_index(batteries, 0, 0))
            print(f'Twelve {value}')
            total += value
            
    print(f'Result is {total}') 

process()