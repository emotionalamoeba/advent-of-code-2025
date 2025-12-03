def get_highest_twelve(batteries):
    while len(batteries) > 12:
        lowest_value = min(batteries)
        rightmost_instance = len(batteries) - 1 - batteries[::-1].index(lowest_value)
        batteries = batteries[:rightmost_instance] + batteries[rightmost_instance+1:]

    return int(batteries)

def process():
    total = 0
    with open('input.txt', 'r') as file:
        for line in file:            
            batteries = line.strip()
            twelve = get_highest_twelve(batteries)            
            print(f'Twelve {twelve}')
            total += twelve
            
    print(f'Result is {total}') 

process()