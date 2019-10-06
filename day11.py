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


if __name__ == "__main__":
    
    serial = 6042

    # create 300x300 grid with 'rack id' as each cell value
    # rack id is x coordinate (starts at 1, not 0) plus 10
    grid = [[x + 11 for x in range(300)] for y in range (300)]

    populate_grid()

    high_power = 0
    high_coords = 0,0
    
    for y in range(1, 299):
        for x in range(1,299):
            cell_power = grid[y][x]  # center
            cell_power += grid[y-1][x+1]  # top right
            cell_power += grid[y][x+1]  # right
            cell_power += grid[y+1][x+1]  # bot right
            cell_power += grid[y+1][x]  # bot
            cell_power += grid[y+1][x-1]  # bot left
            cell_power += grid[y][x-1]  # left
            cell_power += grid[y-1][x-1]  # top left
            cell_power += grid[y-1][x]  # top

            if cell_power > high_power:
                high_power = cell_power
                high_coords = x,y
            
print(f'High power is {high_power} at {high_coords}')