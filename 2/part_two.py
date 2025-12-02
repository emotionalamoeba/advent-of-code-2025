# 23778731601 - too low
# 25344579921 - too low
# 66500947346 - correct

def is_invalid(strid):
    search_len = 1
    while search_len <= len(strid) >> 1:
        term = strid[0:search_len]
        repetitions = 0
        for t in range(1, len(strid) // search_len):
            if strid[t * search_len:(t+1) * search_len] == term:
                repetitions += 1
        
        # Repetitions are the entire string, and there are 2 or more
        if ((repetitions + 1) * search_len) == len(strid) and repetitions >= 1:
            return True

        search_len += 1

    return False


def get_invalid_ids_in_range(start, end):
    invalid_ids = []
    for id in range(start, end + 1):
        strid = str(id)        
        if is_invalid(strid):
            invalid_ids.append(id)

    return invalid_ids
        

def parse_id_range(id_range):
    ids = id_range.split('-')
    return int(ids[0]), int(ids[1])

def process():
    total = 0
    with open('input.txt', 'r') as file:
        input = file.readline().strip()
        id_ranges = input.split(',')
        for id_range in id_ranges:
            invalid_ids = get_invalid_ids_in_range(*parse_id_range(id_range))
            if len(invalid_ids):
                print(f'In range {id_range} invalid ids are {invalid_ids}')
            #if len(invalid_ids) == 0:
            #    print(f'None found in range {id_range}')
            total += sum(invalid_ids)

    print(f'Total is {total}')

process()