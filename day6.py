import numpy as np




with open('day6.txt') as fin:
    contents = fin.readlines()

grid = np.zeros((400,400))
cnt = 1
coords = {}

#populate the grid
for coord in contents:
    x, y = coord.strip().split(', ')

    coords[cnt] = (int(x), int(y))
    grid[int(y)][int(x)] = cnt

    cnt += 1

total_cnt = 0
for y1, row in enumerate(grid):
    for x1, col in enumerate(grid):
        # if the point is a coord, pass
        if (x1, y1) in coords.values():
            total_dist = 0
            for key, value in coords.items():
                dist = abs(x1 - value[0]) + abs(y1 - value[1])
                total_dist += dist
            if total_dist < 10000:
                total_cnt += 1
        else:
            min_dist = 10000
            total_dist = 0
            for key, value in coords.items():
                dist = abs(x1 - value[0]) + abs(y1 - value[1])
                total_dist += dist
                if dist < min_dist:
                    min_dist = dist
                    grid[y1][x1] = key * 10
                elif dist == min_dist:
                    grid[y1][x1] = -1
            if total_dist < 10000:
                total_cnt += 1


# look at perimeters, if there exists a number on the perimeter, area is infinite
# coutn total occurrences of all remaining numbers
pops = list(grid[0])
pops.extend(grid[-1])
for row in grid:
    pops.extend([row[0], row[-1]])

for item in pops:
    try:
        del coords[item / 10]
    except:
        pass

max_coords = 0
for coord in coords:
    coord_count = 1

    for row in grid:
        row = list(row)
        coord_count += row.count(coord * 10)
        
    if coord_count > max_coords:
        max_coords = coord_count
        max_val = coord

    
print(coords)

print(grid)

print(max_coords, max_val)

print(f'Total count inside 32 is {total_cnt}')