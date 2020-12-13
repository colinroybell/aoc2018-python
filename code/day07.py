import re

def loadFile(filename):
    with open(filename,"r") as f:
        strings=[]
        for line in f:
            line = line.rstrip('\n')
            strings.append(line)

    return strings

class Task:

    def __init__(self,name):
        self.name = name
        self.priority = ord(name)-ord('A')
        self.length = ord(name)-ord('A')+61
        self.requirement_count = 0
        self.precedes = []

def get_priority(self):
    return self.priority    

def part1():
    strings = loadFile('../data/07input.txt')

    ready_tasks = []
    tasks = {}

    for c in range(65,91):
        name = chr(c)
        tasks[name] = Task(name)

    regexp = re.compile('Step (.) must be finished before step (.) can begin.')

    for string in strings:
        print(string)
        result = regexp.search(string)
        first = result.group(1)
        second = result.group(2)
        tasks[first].precedes.append(second)
        tasks[second].requirement_count += 1

    # find out which tasks can be done initially

    for c,task in tasks.items():
        if (task.requirement_count == 0):
            ready_tasks.append(task)
            print("Task {} ready initially".format(task.name))
  
    task_strings=""
 
    while (len(ready_tasks) > 0):
        ready_tasks.sort(key=get_priority)
        
        running_task = ready_tasks[0]

        print("Running task {}".format(running_task.name))

        for c in running_task.precedes:
            tasks[c].requirement_count -= 1
            if tasks[c].requirement_count == 0:
                print("Task {} now ready".format(c))
                ready_tasks.append(tasks[c])

        task_strings += running_task.name

        ready_tasks = ready_tasks[1:]

    print("*** {}".format(task_strings))

class Elf:
    def __init__(self, id):
        self.id =id
        self.timeToFree = 0
        self.task = ''

def part2():
    strings = loadFile('../data/07input.txt')

    ready_tasks = []
    tasks = {}
    elves = []

    for c in range(65,91):
        name = chr(c)
        tasks[name] = Task(name)

    for e in range(1,6):
        elves.append(Elf(e))

    regexp = re.compile('Step (.) must be finished before step (.) can begin.')

    for string in strings:
        result = regexp.search(string)
        first = result.group(1)
        second = result.group(2)
        tasks[first].precedes.append(second)
        tasks[second].requirement_count += 1

    # find out which tasks can be done initially

    for c,task in tasks.items():
        if (task.requirement_count == 0):
            ready_tasks.append(task)
            print("Task {} ready initially".format(task.name))
  
    task_strings=""
 
    time = 0
    doneTasks = 0

    while (doneTasks < 26):
        
        ready_tasks.sort(key=get_priority)

        for e in elves:
            if (e.timeToFree == 0 and len(ready_tasks)>0):
                e.task = ready_tasks[0]
                e.timeToFree = e.task.length
                ready_tasks = ready_tasks[1:]
                print("Elf {} starts {} length {}".format(e.id, e.task.name, e.timeToFree))

        time += 1
        print("Time {}".format(time))
  
        for e in elves:
            if (e.timeToFree > 0):
                e.timeToFree -=1
                if (e.timeToFree == 0):
                    print("Elf {} completes {}".format(e.id,e.task.name))
                    doneTasks += 1
                    for c in e.task.precedes:
                        tasks[c].requirement_count -= 1
                        if tasks[c].requirement_count == 0:
                            print("Task {} now ready".format(c))
                            ready_tasks.append(tasks[c])

    print("*** {}".format(time))


#part1()
part2()


