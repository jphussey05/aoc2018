from collections import Counter

freq = 0
freq_cnt = Counter()
freq_cnt[freq] += 1

def instantiate():
    with open('day1_input.txt') as fin:
        inputs = fin.readlines()
    return inputs


inputs = []

while freq_cnt[freq] != 2:
    if len(inputs) == 0:
        inputs = instantiate()
    freq_change = inputs.pop(0)
    print(f'Current freq is {freq}, adding {freq_change.strip()}')

    freq += int(freq_change)
    
    freq_cnt[freq] += 1
    print(f'Frequency count for {freq} is {freq_cnt[freq]}\n')


print(f'Final frequency is {freq}')
print(f'First repeated final frequency is {freq}')