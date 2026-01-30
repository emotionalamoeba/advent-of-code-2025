import sys

# Get distance, no need for square root as we are only sorting
def get_sq_distance(a, b):
    xa, ya, za = a
    xb, yb, zb = b

    xd = xb - xa
    yd = yb - ya
    zd = zb - za

    return xd*xd + yd*yd + zd*zd

def find_closest_coords(coords, connections):
    min_dist = sys.maxsize
    closest_coords = []
    for coord_a in coords:
        for coord_b in coords:
            if coord_a == coord_b:
                continue

            if [coord_a, coord_b] in connections or [coord_b, coord_a] in connections:
                continue

            distance = get_sq_distance(coord_a, coord_b)
            if distance < min_dist:
                closest_coords = [coord_a, coord_b]
                min_dist = distance
    return closest_coords

def process():
    with open('test.txt', 'r') as file:
        coords = [tuple(int(i) for i in line.strip().split(',')) for line in file.readlines()]

    connections_left = 10

    connections = []

    while connections_left > 0:
        closest_coords = find_closest_coords(coords, connections)
        connections.append(closest_coords)
        connections_left -= 1    

    # Find 'circuits' which are not connected
    connected_points = [coord for connection in connections for coord in connection]    
    singles = [p for p in coords if p not in connected_points]
           
    result = group_connections(connections)
    print(f'Connections {connections}')
    print()
    print(f'Result {result} singles {singles}')
    print(f'Result {len(result)} singles {len(singles)}')

    #print(f'Data {coords}')

process()

