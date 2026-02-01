def is_invalid(strid):
    # Skip strings which are not made of two equal lengths
    half_len = len(strid) >> 1    
    if half_len * 2 != len(strid):
        return False
    
    a = strid[0:half_len]
    b = strid[half_len:len(strid)]

    if a == b:
        return True


def get_invalid_ids_in_range(start, end):
    invalid_ids = []
    for id in range(start, end + 1):
        strid = str(id)
        # Skip leading zeroes
        if strid[0] == '0':
            continue
        if is_invalid(strid):
            invalid_ids.append(id)

    return invalid_ids
        

def parse_id_range(id_range):
    ids = id_range.split('-')
    return int(ids[0]), int(ids[1])

def process():
    total = 0
    with open('input.txt', 'r') as file:
        input = file.readline()
        id_ranges = input.split(',')
        for id_range in id_ranges:
            invalid_ids = get_invalid_ids_in_range(*parse_id_range(id_range))
            #if len(invalid_ids):
            #    print(f'In range {id_range} invalid ids are {invalid_ids}')
            total += sum(invalid_ids)

    print(f'Total is {total}')

process()