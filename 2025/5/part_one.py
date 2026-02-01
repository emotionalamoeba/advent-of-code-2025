def process():
    ranges = []
    ingredients = []
    reading_ingredients = False
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                reading_ingredients = True
            elif reading_ingredients == True:
                ingredients.append(int(line))
            else:
                values = line.split('-')
                ranges.append((int(values[0]), int(values[1])))                

    ranges.sort(key=lambda range: (range[0], range[1]))

    print(f'Ranges : {ranges}')
    print(f'Ingredients : {ingredients}')

    total = 0
    for ingredient in ingredients:
        for range in ranges:
            if ingredient >= range[0] and ingredient <= range[1]:
                total +=1
                break

    print(f'Total {total}')

process()