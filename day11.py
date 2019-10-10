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

    # x, y is the top left of the square
    # size is how big the square is

    cell_power = grid[y][x]
    if size > 0:
        for offset in range(1, size):
            # print(f'Point {x},{y}, power={cell_power}, offset={offset}')
            cell_power += sum(grid[y+offset][x:x+size])

    # print(f'Final power for {x},{y} with {size}x{size} is {cell_power}')

    return cell_power

if __name__ == "__main__":
    import time

    serial = 42
    grid_size = 300
    # create 300x300 grid with 'rack id' as each cell value
    # rack id is x coordinate (starts at 1, not 0) plus 10
    grid = [[x + 11 for x in range(grid_size)] for y in range (grid_size)]

    populate_grid()

    high_power = 0
    high_coords = 0,0
    
    start_time = time.time()
    for y in range(grid_size-1):  # creates x and y indices to the grid, so -1
        print(f'Examining row {y+1}')
        for x in range(grid_size-1):

            x_dist = grid_size - x
            y_dist = grid_size - y
            num_squares = min(y_dist, x_dist) 

            for square_size in range(num_squares):  # 0 to the biggest square
                cell_power = calc_power(x,y,square_size)

                if cell_power > high_power:
                    high_power = cell_power
                    high_coords = x+1,y+1
                    high_size = square_size
    duration = time.time() - start_time
        
            
print(f'High power is {high_power} at {high_coords}, {high_size}')
print(f'Total time took {duration} seconds')