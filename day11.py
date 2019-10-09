'''
new branch for part 2 that I may trash if it doesn't work
'''

def populate_grid():
    for y, row in enumerate(grid):
        for x, rack_id in enumerate(row):

            power = rack_id * (y + 1)
            power += serial
            power *= rack_id
            try:
                power = int(str(power)[-3])
            except IndexError:
                power = 0
            power -= 5

            grid[y][x] = power


def calc_power(x, y, size):

    # 0, 0, 3
    # we need to change this to use top left as origin for the square
    # then we need to sum from the origin across each row
    # ex. a 5x5 square would look like...
    # sum(first row from origin to size, second row, etc.)

    cell_power = 0
    for offset in range(size):
        print(f'Point {x},{y}, power={cell_power}, offset={offset}')
        cell_power += sum(grid[y+offset][x:x+size])

    print(f'Final power for {x},{y} is {cell_power}')

    return cell_power

if __name__ == "__main__":
    
    serial = 6042

    # create 300x300 grid with 'rack id' as each cell value
    # rack id is x coordinate (starts at 1, not 0) plus 10
    grid = [[x + 11 for x in range(300)] for y in range (300)]

    populate_grid()

    high_power = 0
    high_coords = 0,0
    
    for y in range(299):
        for x in range(299):

            # loop again for every possible square size with this origin
            #TODO  which is what...? 
            if x == 0 and y == 0:
                cell_power = calc_power(x,y, 3)

            # due to 0 indexing, x,y is actually the 'top left' of a 1 index
            if cell_power > high_power:
                high_power = cell_power
                high_coords = x,y
            
print(f'High power is {high_power} at {high_coords}')