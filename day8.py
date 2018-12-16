
def parse(data):
    print(f'***Received {data}')
    children = data.pop(0)
    metas = data.pop(0)
    print(f'\t{children} Children and {metas} metas')
    totals = 0
    scores = []

    for _ in range(children): # accumulate the totals for each child
        print(f'\tCreating child with {data}')
        total, score, data = parse(data)
        print(f'\tReturned control and total is {total} with {data} left')
        totals += total 
        scores.append(score)


    totals += sum(data[:metas]) # add the sum of all the metas to totals
    print(f'\tTotal for this node is {totals} and still have {data}, meta was {metas}')
    
    if children == 0:
        return totals, sum(data[:metas]), data[metas:]
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]

        )

with open('day8.txt') as fin:
    contents = fin.read()
    numbers = [int(x) for x in contents.split()]


total, value, remaining = parse(numbers)

print(numbers)

print(total, value, remaining)








# data = [int(x) for x in contents.split()]

# def parse(data):
#     children, metas = data[:2]
#     data = data[2:]
#     scores = []
#     totals = 0

#     for i in range(children):
#         total, score, data = parse(data)
#         totals += total
#         scores.append(score)

#     totals += sum(data[:metas])

#     if children == 0:
#         return (totals, sum(data[:metas]), data[metas:])
#     else:
#         return (
#             totals,
#             sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
#             data[metas:]
#         )

# total, value, remaining = parse(data)

# print('part 1:', total)
# print('part 2:', value)