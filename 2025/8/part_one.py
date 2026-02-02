import sys
import math
from functools import lru_cache

# Get distance, no need for square root as we are only sorting
@lru_cache(maxsize=None)
def get_sq_distance(a, b):
    xa, ya, za = a
    xb, yb, zb = b

    xd = xb - xa
    yd = yb - ya
    zd = zb - za

    return xd*xd + yd*yd + zd*zd

def find_closest_coords(coords, limit):
    min_dist = sys.maxsize
    coords_with_distance = []
    for index_a in range(len(coords)):
        # Avoid comparing the same pair in reverse
        for index_b in range(index_a + 1, len(coords)):
            coord_a = coords[index_a]
            coord_b = coords[index_b]

            distance = get_sq_distance(coord_a, coord_b) 

            coords_with_distance.append({ 'distance': distance, 'coord_a': coord_a, 'coord_b': coord_b })            

    closest_coords = sorted(coords_with_distance, key=lambda x: x['distance'])

    return [(c['coord_a'], c['coord_b']) for c in closest_coords[:limit]]

def outer_find_circuits(connections):
    circuit_coords = []
    added_any = 1
    while added_any > 0:
        circuit_coords, added_any = find_circuits(connections, circuit_coords)
    return circuit_coords

def find_circuits(connections, circuit_coords):
    added_any = 0
    for connection in connections:
        # Pick a connection to start with
        if (len(circuit_coords) == 0):
            circuit_coords.append(connection[0])
            circuit_coords.append(connection[1])
            added_any+=1

        # If a connection exists where one of the ends is already in the current circuit then add it
        if (connection[0] in circuit_coords) and not (connection[1] in circuit_coords):
            circuit_coords.append(connection[1])
            added_any += 1
        elif (connection[1] in circuit_coords) and not (connection[0] in circuit_coords):
            circuit_coords.append(connection[0])
            added_any += 1

    return circuit_coords, added_any
    
def remove_circuits_from_coords(circuit_coords, connections):
    remaining_connections = []
    for connection in connections:
        if (connection[0] not in circuit_coords) and (connection[1] not in circuit_coords):
            remaining_connections.append(connection)
    return remaining_connections

def process():
    with open('input.txt', 'r') as file:
        coords = [tuple(int(i) for i in line.strip().split(',')) for line in file.readlines()]

    connections_limit = 1000
    connections = find_closest_coords(coords, connections_limit)
  
    # Find 'circuits' which are not connected    
    connected_points = [coord for connection in connections for coord in connection]    
    singles = [p for p in coords if p not in connected_points]

    circuit_counts = []
    while connections is not None and len(connections) > 0:       
        circuits = outer_find_circuits(connections)
        connections = remove_circuits_from_coords(circuits, connections)
        circuit_counts.append(len(circuits))

    circuit_counts.sort(reverse=True)
    total = math.prod(circuit_counts[0:3])

    print(f'Total {total}')

process()

