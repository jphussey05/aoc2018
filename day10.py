
'''WAY AHEAD

we should have every star calculate the number of adjacent stars
if we then sum this number, we could create the top 5 times that had the
most adjacenies this would probably indicate when there was a message?'''

class Star(object):
    # represets each star
    # has start point, which is used only to find max size of grid
    # also has a velocity and current position
    # needs an update function to record a new location when moved

    def __init__(self, start_x, start_y, x_move, y_move):
        self.start_x = start_x
        self.start_y = start_y
        self.cur_x = start_x
        self.cur_y = start_y
        self.x_velocity = x_move
        self.y_velocity = y_move

    def move(self, step=1):
        self.cur_x += (self.x_velocity * step)
        self.cur_y += (self.y_velocity * step)

    def __str__(self):
        return f'Star at {self.cur_x}, {self.cur_y} w/ V: {self.x_velocity}, {self.y_velocity}'

    def __repr__(self):
        return (
            f'Star({self.start_x},'
            f'{self.start_y},'
            f'{self.x_velocity},'
            f'{self.y_velocity})'
        )

def find_max_xy(stars):
    '''
    Take in all of the points to determine max xy for the grid size
    '''
    max_x = 0
    max_y = 0

    for star in stars:
        max_x = max(max_x, abs(star.cur_x))
        max_y = max(max_y, abs(star.cur_y))
    
    
    return (max_x, max_y)

def parse_start_points(contents):
    '''
    The initial strip of the ingested day10.txt file that has all of the points
    creates a list of Star objects
    '''
    stars = []
    for line in contents:
        start, velocity = line.split(' velocity=')
        x,y = map(int, start[start.find('<') + 1:start.find('>')].split(','))
        dx, dy = map(
            int, velocity[velocity.find('<') + 1: velocity.find('>')].split(',')
            )
        
        stars.append(Star(x, y, dx, dy))
    
    return stars



def print_star_map(stars):
    max_x, max_y = find_max_xy(stars)
    
    star_map = [[' ' for _ in range(max_x+1)] for _ in range(max_y+1)]

    for star in stars:
        star_map[star.cur_y][star.cur_x] = '*'

    for row in star_map:
        print(''.join(row))

with open('day10.txt') as fin:
    contents = fin.readlines()

stars = parse_start_points(contents)

for star in stars:
    star.move(3)
print_star_map(stars)

