import numpy as np

class Pattern(object):
    def __init__(self, idx, left_margin, top_margin, width, height):
        self.idx = int(idx[1:])
        self.left_margin = int(left_margin)
        self.top_margin = int(top_margin)
        self.height = int(height)
        self.width = int(width)
        self.total = self.height * self.width
    
    def plot(self, fabric):
        vert = self.top_margin + self.height
        hor = self.left_margin + self.width

        for row_idx, row in enumerate(fabric):
            for col_idx, col in enumerate(row):               
                if row_idx in range(self.top_margin, vert) and col_idx in range(self.left_margin, hor):
                    if col == 0:
                        fabric[row_idx][col_idx] = self.idx
                    else:
                        fabric[row_idx][col_idx] = -1
                
        return fabric

    def __str__(self):
        return f'{self.idx} @ {self.left_margin},{self.top_margin} - {self.width}x{self.height}'


def print_fabric(fabric):
    for row in fabric:
        print(np.array_str(row))
    
    return None


def check_fabric(fabric):
    cnt = 0
    for row in fabric:
        cnt += np.sum(row == -1)

    return cnt


with open('day3.txt') as fin:
    contents = fin.readlines()

fabric = np.zeros((1000,1000))

pattern_list = []

for item in contents:
    pieces = item.strip().split(' ')

    margins = pieces[2].split(',')
    left_margin = margins[0]
    top_margin = margins[1].strip(':')

    dimensions = pieces[3].split('x')
    width = dimensions[0]
    height = dimensions[1]
    idx = pieces[0].strip()

    # print(left_margin, top_margin, width, height)
    pattern_list.append(Pattern(idx, left_margin, top_margin, width, height))

for pattern in pattern_list:
    print(pattern)
    fabric = pattern.plot(fabric)

for pattern in pattern_list:
    cnt = 0
    for row in fabric:
        cnt += np.sum(row == pattern.idx)
    
    if cnt == pattern.total:
        print(f'{pattern.idx} had no overlaps')

collisions = check_fabric(fabric)

# print_fabric(fabric)
print(f'Total number of overlaps = {collisions}')