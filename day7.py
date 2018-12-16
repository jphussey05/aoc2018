

class Worker(object):
    def __init__(self, worker_name):
        self.task = None
        self.worker_name = worker_name
        self.go_time = None


    def assign_job(self, next_step, cur_time):
        #set the time it takes
        #record which next_step
        self.task = next_step
        self.go_time = int(cur_time + ord(next_step) - 64 + 60)
        print(f'Worker {self.worker_name} assigned {self.task} at {cur_time} and will be done at {self.go_time}')


    def execute_step(self, step_dict):


        for k, v in step_dict.items():
            if self.task in v:
                print(f'removing {self.task} from {k}')
                v.remove(self.task)
        self.go_time = None
        self.task = None
        return step_dict

def get_available(step_dict):
    available = []

    for k, v in step_dict.items():
        if v == []:
            print(f'{k} is now available')
            available.append(k)
        
    return sorted(available)





with open('day7.txt') as fin:
    contents = fin.readlines()


# creates the dictionary of tasks
step_dict = {}

for line in contents:
    items = line.strip().split(' ')
    name = items[7]
    pre_req = items[1]

    if pre_req not in step_dict:
        step_dict[pre_req] = []

    if name in step_dict:
        step_dict[name].append(pre_req)
    else:
        step_dict[name] = [pre_req]


workers = [Worker(x+1) for x in range(5)]
print(f'Created {len(workers)} workers')

order = ''
t = 0
while step_dict:
    print(f'------Time is {t}')
    for k, v in step_dict.items():
        print(f'{k} is dependent on {v}')

    for w in workers:
        if w.go_time == t:
            order += w.task
            step_dict = w.execute_step(step_dict)

    for w in workers:

        available = get_available(step_dict)
        print(f'list of available tasks for {w.worker_name} is {available}')

        if not w.task and available: # assign a task because we're not working
            w.assign_job(available[0], t)
            del step_dict[w.task]
        else: # this worker is busy or nothing is available
            print(f'Nothing is available or {w.worker_name} is busy')
            continue
    # step_dict = execute_step(available[0], step_dict)

    t += 1
    


print(order)