def fix_overlaps(ranges):
    result = []
    first_range = ranges[0]
    lowest_start = first_range[0]
    highest_end = first_range[1]

    for r_index in range(1, len(ranges)):
        current_range = ranges[r_index]
        start = current_range[0]
        end = current_range[1]

        if start > highest_end:
            # We passed the overlaps, now store previous values             
            result.append((lowest_start, highest_end))
            lowest_start = start
            highest_end = end
        else:
            # Extend the maximum to include the current range
            highest_end = max(end, highest_end)

    # Store current range
    result.append((lowest_start, highest_end))

    return result

def process():
    ranges = []    
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                break
            
            values = line.split('-')
            ranges.append((int(values[0]), int(values[1])))                

    # Sort ranges by start, then by end
    ranges.sort(key=lambda range: (range[0], range[1]))

    # Remove any ranges which overlap another range   
    ranges = fix_overlaps(ranges)
    
    total = 0
    for r in ranges:
        print(f'Range {r[0]}-{r[1]}')
        total += r[1]-r[0] + 1

    print(f'Total {total}')

process()