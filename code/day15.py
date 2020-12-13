import operator

class Pos:
    def __init__(self,loc):
        self.loc = loc

    def add(self,mod):
        x,y = self.loc
        xm,ym = mod.loc

        return Pos((x+xm,y+ym))

    def __lt__(self,other):
        x,y = self.loc
        xo,yo = other.loc

        return (y < yo or y==yo and x<xo)

    def __str__(self):
        x, y = self.loc
        return "({},{})".format(x,y)

    def __eq__(self,other):
        x, y = self.loc
        xo, yo = other.loc

        return (x==xo and y==yo)    

    def __hash__(self):
        return hash(self.loc)   

class Person:
    def __init__(self,team,pos):
        self.pos = pos
        self.team= team
        self.hp = 200
        self.power = 3
        #if team=='E':
        #    self.power = 25
        self.alive = 1

    def move(self,pos):
        self.pos = pos    

    def __str__ (self):
        return "{}{}:{}".format(self.team,self.pos,self.hp)    

class Route:
    def __init__(self,pos,first):
        self.pos = pos
        self.first = first

spaces = set()
people = []
elves = 0
goblins = 0

adjacencies = [Pos((0,-1)),Pos((-1,0)),Pos((1,0)),Pos((0,1))]

def move(actor):
    print("Moving {} at {}".format(actor.team,actor.pos))
    adjList = set()
    occList = set()
    for p in people:
        if p.alive:
            occList.add(p.pos)
            if p.team != actor.team:
                for dir in adjacencies:
                    pos = p.pos.add(dir)
                    if pos in spaces:
    #                    print("adj list {}".format(pos))
                        adjList.add(pos)

    if actor.pos in adjList:
        print("Already adjacent")
        return

    routes = [Route(actor.pos, Pos((0,0)))]
    considered = set()
    considered.add(actor.pos)
    found = False
    foundList = []

    while found == False and not routes == []:
#        print("New round")
        newRoutes = []
        for r in routes:
            for dir in adjacencies:
                pos = r.pos.add(dir)
#                print("Considering {} {} to {}".format(r.pos,dir,pos))
#                print("{} {}".format(pos in spaces,pos not in considered))
                if pos in spaces and not pos in considered and not pos in occList:
                    first = r.first
                    if first == Pos((0,0)):
                        first = dir
                    newRoutes.append(Route(pos,first))
                    considered.add(pos)
#                    print("adding {} {}".format(pos,first))
                    if pos in adjList:
#                        print("found location")
                        found = True
                        foundList.append(Route(pos,first))
        routes = newRoutes                

    if (routes == []):
        print("No available target") 
        return   

    bestPos = foundList[0].pos
    bestLoc = 0

    for i in range(1,len(foundList)):
        if foundList[i].pos < bestPos:
            bestPos = foundList[i].pos
            bestLoc = i

    newPos = actor.pos.add(foundList[bestLoc].first)

    print("Moving to {}".format(newPos))

    actor.move(newPos)  
    
def attack(actor):
    global elves
    global goblins
    target = None
    for p in people:
        if p.alive and p.team != actor.team:
            for dir in adjacencies:
                pos = p.pos.add(dir)
                if pos == actor.pos:
                    if (target == None or p.hp < target.hp or p.hp == target.hp and p.pos < target.pos):
                       target = p

    if (not target == None):
        print("Attacks {}".format(target))
        target.hp -= actor.power
        if (target.hp<=0):
            print("Dies")
            target.alive = 0
            target.hp = 0
            if target.team == 'E':
                elves -= 1
            else:
                goblins -= 1





def part1(filename):   
    y = 0
    global goblins
    global elves
    with open(filename,'r') as f:
        for line in f:
            x = 0
            for c in line:
                if c == '.' or c == 'E' or c=='G':
                    pos = Pos((x,y))
                    spaces.add(pos)
                    if c == 'E' or c=='G':  
                        people.append(Person(c,pos))
                        print("adding {} at {}".format(c,pos))
                        if c=='E':
                            elves += 1
                        else:
                            goblins += 1
                x+=1                
            y+=1

    round = 0
    finished = False

    while  not finished:
        people.sort(key = lambda x: x.pos)

        for p in people:
            if p.alive:
                print("list now")
                for np in people:
                    print(np)
                move(p)
                attack(p)

        finished = (elves == 0) or (goblins == 0)       
        round+= 1 

        print("End of round {}".format(round))
        for p in people:
            if p.alive:
                print(p)

    total_hp = 0
    for p in people:
        if p.alive:
            total_hp += p.hp


    round-=1 
    # This is needed in most cases - the termination condition is the first person to find
    # no enemy to fight. In the worked example, this is in the _next_ round, as the last goblin
    # in 47 attacks someone. But for subsequent cases, there's an unused victor on that round,
    # so the round in which someone dies isn't complete
    print("Finished with {} elves {} goblins: {} x {} = {}".format(elves,goblins,round,total_hp,round*total_hp))

part1("../data/15input.txt")

# part 2 done by hack and binary chop
