# too low = 347444809832240
# too low = 347444809832416

def process():
    ranges = []    
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                break
            
            values = line.split('-')
            ranges.append((int(values[0]), int(values[1])))                

    ranges.sort(key=lambda range: (range[0], range[1]))

    min_ingredient = ranges[0][0]
    max_ingredient = ranges[-1][1]
    potential_max = max_ingredient - min_ingredient

    total = 0
    gaps = []

    # Count the gaps between ranges, then subtract from potential_max
    for r in range(len(ranges) - 1):
        a = ranges[r]
        b = ranges[r+1]

        if a[1] < b[0]:
            gaps.append((a[1] + 1, b[0] - 1))

    gap_total = 0
    for g in gaps:
        print(f'Gap ({g[0]},{g[1]})')
        gap_total += g[1]-g[0]

    print(f'Potential max {potential_max} gap total {gap_total} min_ingredient {min_ingredient} max_ingredient {max_ingredient}')
    total = potential_max - gap_total
    print(f'Total {total}')

process()