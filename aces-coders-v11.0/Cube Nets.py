# https://www.hackerrank.com/contests/aces-coders-v11-0/challenges/cube-nets

# We tried hardcoding the cube nets, but we were only able to get 21.67 marks out of 200

cube_nets = (
    ((0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1)),
    ((0, 0), (0, 1), (1, 1), (1, 2), (2, 1), (3, 1)),
    ((0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 1)),
    ((0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2)),
    ((0, 0), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)),
    ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 1)),
    ((0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2)),
    ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1)),
)

def compare_with_nets(positions):
    positions = tuple(sorted(positions))
    return positions in cube_nets

def rotate_and_normalize_all(positions):
    def rotate_90(positions):
        return [(y, -x) for x, y in positions]

    def rotate_180(positions):
        return [(-x, -y) for x, y in positions]

    def reflect_horizontal(positions):
        return [(x, -y) for x, y in positions]

    def reflect_vertical(positions):
        return [(-x, y) for x, y in positions]

    def normalize(positions):
        min_x = min(x for x, y in positions)
        min_y = min(y for x, y in positions)
        return [(x - min_x, y - min_y) for x, y in positions]

    original = normalize(positions)
    rotated_90 = normalize(rotate_90(original))
    rotated_180 = normalize(rotate_180(original))
    rotated_neg90 = normalize(rotate_90(rotated_180))
    
    # Include reflections
    reflected_original = normalize(reflect_horizontal(original))
    reflected_rotated_90 = normalize(reflect_horizontal(rotated_90))
    reflected_rotated_180 = normalize(reflect_horizontal(rotated_180))
    reflected_rotated_neg90 = normalize(reflect_horizontal(rotated_neg90))

    return [
        original, rotated_90, rotated_neg90, rotated_180,
        reflected_original, reflected_rotated_90, reflected_rotated_neg90, reflected_rotated_180,
        # Also consider vertical reflections
        normalize(reflect_vertical(original)),
        normalize(reflect_vertical(rotated_90)),
        normalize(reflect_vertical(rotated_180)),
        normalize(reflect_vertical(rotated_neg90))
    ]

def flood_fill(grid, visited, y, x, height, width):
    # Directions for 8-way connectivity (N, NE, E, SE, S, SW, W, NW)
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    shape = []

    stack = [(y, x)]
    while stack:
        current_y, current_x = stack.pop()
        if (current_y < 0 or current_y >= height or current_x < 0 or current_x >= width or 
                visited[current_y][current_x] or grid[current_y][current_x] != '#'):
            continue

        visited[current_y][current_x] = True
        shape.append((current_y, current_x))

        for dy, dx in directions:
            ny, nx = current_y + dy, current_x + dx
            stack.append((ny, nx))
    
    return shape
precalc_list = [1505, 2530, 3024, 4578, 252, 6552, 2529, 4577, 2499, 4547, 7056]
def is_bitmap_in_precalc(bitmap, precalc_list):
    return bitmap in precalc_list

q = int(input())
for _ in range(q):
    m, n = map(int, input().split())
    input_string = []
    for _ in range(m):
        line = input()
        input_string.append(line)
    
    visited = [[False] * n for _ in range(m)]
    nets = []

    for y in range(m):
        for x in range(n):
            if not visited[y][x] and input_string[y][x] == '#':
                # Found an unvisited '#' cell, perform flood fill to get the entire shape
                shape = flood_fill(input_string, visited, y, x, m, n)
                if shape:
                    nets.append(shape)

    valid_count = 0
    invalid_count = 0
    for net in nets:
        # Create a minimal representation of the net for bitmap calculation
        min_y = min(net, key=lambda pos: pos[0])[0]
        min_x = min(net, key=lambda pos: pos[1])[1]
        max_y = max(net, key=lambda pos: pos[0])[0]
        max_x = max(net, key=lambda pos: pos[1])[1]

        # Create the trimmed shape string based on the min/max coordinates
        shape_str = []
        for y in range(min_y, max_y + 1):
            line = ''.join(input_string[y][x] for x in range(min_x, max_x + 1))
            shape_str.append(line)
        positions = []
        shape_str = "\n".join(shape_str)
        # print(shape_str, "\n")
        i = 0
        j = 0
        for ch in shape_str:
            if ch == '#':
                positions.append((i, j)) 
            j += 1
            if ch == "\n":
                i += 1
                j = 0
        if len(positions) != 6:
            invalid_count += 1  
            continue
        # print(positions)
        for pos in rotate_and_normalize_all(positions):
            if compare_with_nets(pos):
                valid_count += 1
                break
        else:
            invalid_count += 1
            
    print(valid_count, invalid_count) 