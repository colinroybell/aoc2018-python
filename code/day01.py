def loadFile(filename):
    with open(filename,"r") as f:
        numbers=[]
        for line in f:
            line = line.rstrip('\n')
            numbers.append(int(line))

    return numbers

def part1():
    numbers = loadFile('../data/01input.txt')
    sum = 0
    for n in numbers:
        sum += n

    print("*** {}".format(sum))

def part2():
    numbers = loadFile('../data/01input.txt')
    seen = set()
    sum = 0
    while 1:
        for n in numbers:
            sum += n
            if (sum in seen):
                break
            else:
                seen.add(sum)   
        else: 
            continue
        break

    print("*** {}".format(sum))                


part1()
part2()
