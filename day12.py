with open('day12.txt') as fin:
    contents = fin.readlines()

initial = contents[0][15:]

print(initial)

spread_dict = dict()

for line in contents[2:]:
    line = line.strip()
    spread_dict[line[:5]] = line[-1]

print(spread_dict)