class Star(object):
    # represets each star
    # has start point, which is used only to find max size of grid
    # also has a velocity and current position
    # needs an update function to record a new location when moved

    def __init__(self, ID):
        pass


def find_max_xy():
    pass

def parse_start_points(contents):
    '''
    The initial strip of the ingested day10.txt file that has all of the points
    creates a list of Star objects
    '''
    pass 

    




with open('day10.txt') as fin:
    contents = fin.readlines()

points = parse_start_points(contents)