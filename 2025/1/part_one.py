def rotate(position, rotationString):
    direction = rotationString[0]
    rotation = rotationString[1:]

    #print(f'Direction {direction} rotation {rotation}')
    position += int(rotation) * (-1 if direction == 'L' else 1)
    return position % 100

def process():
    position = 50
    zeroes = 0
    with open('input.txt', 'r') as file:
        for line in file:
            rotationString = line.strip()
            newPosition = rotate(position, rotationString)            
            if newPosition == 0:
                zeroes += 1
                #print(f'Position {position} rotated by {rotationString} is now {newPosition}')
            position = newPosition
    print(f'Password is {zeroes}') 

process()