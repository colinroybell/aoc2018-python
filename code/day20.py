from collections import deque

def plus(loc,dir):
    x, y = loc
    if (dir == 'N'):
        return (x,y-1)
    elif (dir == 'S'):
        return (x,y+1)
    elif (dir == 'E'):
        return (x+1,y)
    else:
        return (x-1,y)           

def revdir(dir):
    if dir == 'N':
        return 'S'
    elif dir == 'S':
        return 'N'
    elif dir == 'E':
        return 'W'
    elif dir == 'W':
        return 'E'
    print("unknown direction {}".format(dir))
    assert 0    

def addadj(adj,loc,dir):
    other = plus(loc,dir)
    rev = revdir(dir)
    if loc not in adj:
        adj[loc] = []
    adj[loc].append(dir)
#    print("adding {},{} {}".format(loc[0],loc[1],dir))

    if other not in adj:
        adj[other] = []
    adj[other].append(rev)    
#    print("and {},{} {}".format(other[0],other[1],rev))

class Node:
    def __init__ (self):
        self.start = set()
        self.end = set()

    def __repr__ (self):
        return "{}/{}".format(self.start,self.end)                        

def part1(string):
    adj = {}
    initial = Node()
    initial.start.add((0,0))

    status = [initial]

    for c in string:
#        print(c)
        if c == 'E' or c == 'N' or c == 'S' or c == 'W':
            for loc in status[-1].start:
                addadj(adj,loc,c)
                status[-1].end.add(plus(loc,c))
            status[-1].start = status[-1].end.copy()
            status[-1].end = set()
        elif c == '(':
            newNode = Node()
            newNode.start = status[-1].start.copy()        
            status.append(newNode)
        elif c == '|':
            status[-2].end |= status[-1].start
            status[-1].start = status[-2].start.copy()
        elif c == ')':
            status[-2].end |= status[-1].start 
            status[-2].start = status[-2].end.copy()
            status[-2].end = set()
            status.pop()
#        print(status) 

    dist = {}
    dist[(0,0)] = 0

    q = deque()
    q.append((0,0))
    max_distance = 0
    count_1000 = 0

    while len(q)>0:
        base = q.popleft()
        base_distance = dist[base]
        for dir in adj[base]:
            loc = plus(base,dir)
            if loc not in dist:
                dist[loc] = base_distance + 1
                if (dist[loc] >= 1000):
                    count_1000 +=1
#                print("{} {} at {}".format(loc[0],loc[1],dist[loc]))
                if (dist[loc] > max_distance):
                   max_distance = dist[loc] 
                q.append(loc)

    print(max_distance,count_1000)            



#part1("^ENWWW(NEEE|SSE(EE|N))$")
part1("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$")
#part1("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$")
#part1("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$")


with open ('../data/20input.txt','r') as f:
    for line in f:
        part1(line)
