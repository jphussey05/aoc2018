import Levenshtein

def check_count(nums):
    twos = 0
    threes = 0


    uniques = set(nums)

    for char in uniques:
        cnt = nums.count(char)
        if cnt == 2:
            twos = 1
            # print(f'{nums} has {twos} doubles')
        elif cnt == 3:
            threes = 1
            # print(f'{nums} has {threes} triples')
        else:
            pass
    
    return twos, threes

def find_similar(line, contents):
    for other in contents:
        if Levenshtein.distance(line, other) == 1:
            return other
    return None

twos = 0
threes = 0

with open('day2_input.txt') as fin:
    contents = fin.readlines()

for line in contents:
    x, y = check_count(line.strip())
    twos += x
    threes += y

    match = find_similar(line, contents)
    if match:
        print(f'{line} almost matches {match}')


print(twos*threes)