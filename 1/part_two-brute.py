def rotate(position, rotationString):
    direction = rotationString[0]
    magnitude = int(rotationString[1:])    
    sign = (-1 if direction == 'L' else 1)
    zeroCount = 0

    newPosition = position
    for i in range(magnitude):
        newPosition += sign
        if newPosition > 99:
            newPosition = 0
        elif newPosition < 0:
            newPosition = 99
        if newPosition == 0:
            zeroCount += 1

    return newPosition, zeroCount

def process():
    index = 0
    position = 50
    zeroes = 0
    with open('input.txt', 'r') as file:
        for line in file:            
            rotationString = line.strip()
            newPosition, newZeroes = rotate(position, rotationString)            
            zeroes += newZeroes           
            position = newPosition
            index += 1
    print(f'Password is {zeroes}') 

process()