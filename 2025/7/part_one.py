def process():
    with open('input.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]

    y_size = len(data)   

    beam_locations = [] 
    split_count = 0
    for y in range(y_size):
        if y == 0:
            beam_locations.append(data[y].index('S'))
            continue
        
        new_beam_locations = []
        for location in beam_locations:
            if data[y][location] == '^':
                new_beam_locations.append(location - 1)
                new_beam_locations.append(location + 1)
                split_count += 1
            else:
                new_beam_locations.append(location)

        new_unique = set(new_beam_locations)
        beam_locations = new_unique

    print(f'Split count {split_count}')

process()