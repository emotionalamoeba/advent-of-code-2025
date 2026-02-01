
def constrained_bounds(center_x, center_y, x_size, y_size):
    x1 = center_x - 1
    x2 = center_x + 1
    y1 = center_y - 1
    y2 = center_y + 1

    if x1 < 0: x1 = 0
    if y1 < 0: y1 = 0
    if x2 >= x_size: x2 = x_size - 1
    if y2 >= y_size: y2 = y_size - 1

    return x1, y1, x2, y2


def can_access_roll(data, xc, yc, x_size, y_size):
    if data[yc][xc] != '@':
        return False

    x1, y1, x2, y2 = constrained_bounds(xc, yc, x_size, y_size)

    total_rolls = -1 # ignore center roll
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if data[y][x] == '@':
                total_rolls += 1
                if total_rolls > 3:
                    return False

    return True

def process():
    with open('input.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
    print(data)   
    y_size = len(data)
    accessible_roll_count = 0
    for y in range(y_size):
        x_size = len(data[y])
        for x in range(x_size):            
            can_access = can_access_roll(data, x, y, x_size, y_size)
            print(f'Can access roll at {x},{y} : {can_access}')
            if can_access:
                accessible_roll_count += 1

    print(f'Accessible roll count {accessible_roll_count}')

process()