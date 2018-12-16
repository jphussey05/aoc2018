

with open('day5.txt') as fin:
    contents = fin.readlines()

cursor = 0

line = contents[0].strip()
min_line = len(line)
for x in range(97,123):
    print(f'working on {chr(x)}')
    new_line = line.replace(chr(x), '').replace(chr(x-32), '')

    flag = False
    while flag == False:
        # print(new_line)
        flag = True
        # print(len(new_line))
        for i, c in enumerate(new_line):
            if i + 1 < len(new_line) and abs(ord(c) - ord(new_line[i+1])) == 32:
                new_line = new_line[:i] + new_line[i+2:]
                flag = False
                break
        

    if len(new_line) < min_line:
        min_line = len(new_line)
        min_chr = chr(x)

print(min_line, min_chr)