from functools import lru_cache

@lru_cache(maxsize=None)
def split_recurse(x_position: int, row_index: int) -> int:   
    while row_index < len(data) - 1 and data[row_index][x_position] != '^':
        row_index += 1
        
    if row_index == len(data) - 1:
        return 1

    total = 0
    if data[row_index][x_position] == '^':
        total += split_recurse(x_position - 1, row_index)
        total += split_recurse(x_position + 1, row_index)

    return total

def process():
    with open('input.txt', 'r') as file:
        global data
        data = [line.strip() for line in file.readlines()]
    
    beam_start_position = data[0].index('S')

    y = 1
    while data[y][beam_start_position] != '^': y+=1
    
    print(f'Splits: {split_recurse(beam_start_position, y)}')

process()