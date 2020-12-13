import re

def loadFile(filename):
    with open(filename,"r") as f:
        strings=[]
        for line in f:
            line = line.rstrip('\n')
            strings.append(line)

    return strings

def bothParts():
    strings = loadFile('../data/04input.txt')
    strings.sort()

    regexp = re.compile('Guard \#(\d+)')

    state = "awake"
    last = 0
    current_guard = 0

    total_asleep = {}
    min_asleep = {}

    for string in strings:
        print(string)
        time = int(string[15:17])
        result = regexp.search(string)
        if result:     
            current_guard = int(result.group(1))
            print("Guard {}".format(current_guard))
        elif string[19:24] == 'falls':
            last = time    
        else: # wakes up
            print("from {} to {}".format(last,time))  
            total_asleep[current_guard] = total_asleep.get(current_guard,0)+time-last
            asleep_counts = min_asleep.get(current_guard,[0]*60)
            for t in range(last,time):
                asleep_counts[t]+=1
            min_asleep[current_guard] = asleep_counts    


    # part 1

    our_guard = 0
    time_max = 0
    for g,count in total_asleep.items():
        if count > time_max:
            our_guard = g
            time_max = count

    print("our guard {}".format(our_guard))

    asleep_counts = min_asleep.get(our_guard)             
    our_minute = 0
    count_max = 0
    for t in range(0,60):
        if asleep_counts[t] > count_max:
            our_minute = t
            count_max = asleep_counts[t]

    mul = our_guard * our_minute
    print("*** {}".format(mul))       

    # part 2

    our_guard = 0
    our_minute = 0
    count_max = 0

    for g,asleep_counts in min_asleep.items():
        for t in range(0,60):
            if asleep_counts[t] > count_max:
                our_guard = g
                our_minute = t
                count_max = asleep_counts[t]

    mul = our_guard * our_minute
    print("*** {}".format(mul))             

bothParts()

