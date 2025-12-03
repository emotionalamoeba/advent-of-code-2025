def get_highest_pair(batteries):
    list_without_end = batteries[:-1]
    highest_left_digit = max(list_without_end)
    start_index = list_without_end.index(highest_left_digit)
    list_without_start = batteries[start_index+1:]
    highest_right_digit = max(list_without_start)
    
    return int(f'{highest_left_digit}{highest_right_digit}')

def process():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:            
            batteries = line.strip()
            pair = get_highest_pair(batteries)            
            print(f'Pair {pair}')
            total += pair
            
    print(f'Result is {total}') 

process()