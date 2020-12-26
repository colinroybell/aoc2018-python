def manhattan(x,y):
    d = 0
    for i in range(0, 4):
        d += abs(x[i] - y[i])
    return d    


class Star:
    def __init__(self, loc):
        self.loc = loc
        self.used = False


def loadFile(filename):
    stars = [] 
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            coord_strings = line.split(',')
            coord = []
            for c in coord_strings:
                coord.append(int(c))
            stars.append(Star(coord))    
    return stars

def part1():
    stars = loadFile('../data/25input.txt')

    consts = 0

    while 1:
        queue = []
        done = True
        for s in stars:
            if s.used == False:
                queue.append(s)
                done = False
                break

        if done:
            break

        consts += 1
 
        while (len(queue)):
            s = queue.pop()
            s.used = True
            for t in stars:
                if t.used == False and t not in queue and manhattan(s.loc, t.loc) <= 3:
                    queue.append(t)
    print(consts)    

part1()            


