from datetime import datetime, timedelta
from pprint import pprint
from collections import Counter, namedtuple

Event = namedtuple('Event', ['timestamp', 'text'])

class Guard(object):
    # has multiple time stamps with wakes and sleeps
    # has a total number of minutes assleep
    # should have a counter that keeps track of the minutes asleep

    def __init__(self, ID):
        self.total_min_asleep = timedelta(0)
        self.min_counter = Counter()
        self.id = ID

    def parse_event(self, start, end):
        time_slept = end - start
        self.total_min_asleep += time_slept
        
        for m in range(start.minute, end.minute):
            self.min_counter[m] += 1

        print(f'Guard {self.id} slept {time_slept} from {start} to {end} \n\tand total is {self.total_min_asleep}')
    
    def __str__(self):
        return f'Guard {self.id}\n--Slept {self.total_min_asleep}\n--{self.min_counter}'


with open('day4.txt') as fin:
    contents = fin.readlines()

events = []

for timestamp in contents:
    
    date, time = timestamp[1:17].split(' ')
    year, month, day = date.split('-')
    hour, minute = time.split(':')
    year, month, day, hour, minute = map(int, [year, month, day, hour, minute])

    events.append(Event(datetime(year, month, day, hour, minute), timestamp[19:-1]))

events.sort()
guards = {}
pprint(events)
for event in events: 
    # Checks to see if we're starting a new shift
    if 'Guard' in event.text: 
        current_guard = event.text.split(' ')[1].lstrip('#')
        # print(f'Guard id is {guard_id}')

        if current_guard not in guards:
            guards[current_guard] = Guard(current_guard)
        continue
    elif 'falls' in event.text:
        start = event.timestamp
    elif 'wakes' in event.text:
        end = event.timestamp
        guards[current_guard].parse_event(start, end)
    else:
        raise(ValueError(f'Unhandled Event - {event.text}'))


max_id = ''
max_min = 0
max_val = 0

for guard in guards.values():
    print(guard)
    for k, v in guard.min_counter.items():
        print(k,v)
        if v > max_val:
            print(f'{v} was greater than {max_min}')
            max_min = k
            max_val = v
            max_id = guard.id

print(max_id, max_min, max_val)
print(int(max_id) * max_min)