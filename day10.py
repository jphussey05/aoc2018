from pprint import pprint
from time import sleep
import numpy as np


def update_points(old_points):
    new_points = []
    
    for point in old_points: 
        new_points.append([point[0] + point[2], point[1] + point[3], point[2], point[3]])

    return new_points

def clean_line(line: str):
    line = line.strip().replace('position=<', '')
    line = line.replace('> velocity=<', ',')
    line = line.replace('>', '')

    pieces = list(map(int, line.split(',')))
    
    
    return pieces


# initial population
with open('day10.txt') as fin:
    contents = fin.readlines()

starting_points = [clean_line(line) for line in contents]
# print(starting_points)
square = 2 * max(
    max([x[0] for x in starting_points]),
    abs(min([x[0] for x in starting_points])),
    max([y[1] for y in starting_points]),
    abs(min([y[1] for y in starting_points]))
)

xdiff = max([x[0] for x in starting_points]) - min([x[0] for x in starting_points])
ydiff = max([y[1] for y in starting_points]) - min([y[1] for y in starting_points])
print(f'diff in x is {xdiff} and diff in y is {ydiff}')
if square % 2 == 0:
    square += 1
center = (square - 1) // 2

print(f'Grid size is {square}')
cnt = 0
# start cycle
with open('day10output.txt', 'w') as fout:
    fout.write('NEW FILE\n')
while True:
    cnt +=1 
    print(f'****** TIME IS {cnt} ********')

    # grid = [['.' for _ in range(square)] for _ in range(square)]
    grid = np.full((square, square), '.')

    print('Grid created')

    for i, point in enumerate(starting_points):
        grid[center + point[1]][center + point[0]] = '#'

    print('Writing output...')
    with open('day10output.txt', 'a') as fout:
        fout.write('********************\n********************\n')
        for line in grid:
            # line = np.array2string(line)
            line = str(line)
            fout.write(''.join(line) + '\n')
    print(f'Wrote output for time {cnt}')
    starting_points = update_points(starting_points)
