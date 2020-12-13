import re

class Nanobot:

    @classmethod
    def init_regexp(cls):
        cls.regexp = re.compile("pos=\<([-\d]+),([-\d]+),([-\d]+)\>, r=(\d+)")

    def __init__(self,string):
        print(string)
        result = self.regexp.match(string)
        assert result
        self.loc = [int(result.group(1)), int(result.group(2)), int(result.group(3))]
        self.strength = int(result.group(4))

    def sees(self,other):
        dist = 0
        for i in range(0,3):
            dist += abs(self.loc[i]-other.loc[i])

        return (dist <= self.strength)

    def sees_range(self,range_lo,range_hi):
        dist = 0
        for i in range (0,3):
            if self.loc[i] < range_lo[i]:
                dist += range_lo[i] - self.loc[i]
            if self.loc[i] >= range_hi[i]:
                dist += self.loc[i] - range_hi[i] + 1
        return (dist <= self.strength)        

def loadFile(filename):
    bots = []
    Nanobot.init_regexp()
    with open(filename,"r") as f:
        for line in f:
            bots.append(Nanobot(line))

    return bots

def part1():
    bots = loadFile('../data/23input.txt')

    max_strength = 0
    best_bot = None
    for i,bot in enumerate(bots):
        if bot.strength > max_strength:
            max_strength = bot.strength
            max_bot = bot
   
    count = 0
    for bot in bots:
        if max_bot.sees(bot):
            count += 1

    print(count)

def recurse(bots, name, range_lo, range_hi, best):
    score = 0
    points = []
    for bot in bots:
        if bot.sees_range(range_lo, range_hi):
            score += 1
  
    print("Trying {} {} {}, score {}".format(name,range_lo, range_hi, score))

    if score < best:
        return best,[]

    if (range_hi[0]-range_lo[0]==1):
        return score,[range_lo]
 
    cands = []

    for sub in range(8):
        value = [sub % 2, (sub//2)%2, (sub//4)%2]

        range_lo_sub=[]
        range_hi_sub=[]

        for i in range(3):
            range_lo_val = range_lo[i] + (range_hi[i]-range_lo[i])*value[i]//2
            range_hi_val = range_lo_val + (range_hi[i]-range_lo[i])//2
            range_lo_sub.append(range_lo_val)
            range_hi_sub.append(range_hi_val)
        score = 0
        for bot in bots:
            if bot.sees_range(range_lo_sub,range_hi_sub):
                score += 1
  
        cands.append((sub,score,range_lo_sub, range_hi_sub))

    cands_sorted = sorted(cands, key=lambda x: -x[1])

    print(cands_sorted)

    for c in cands_sorted:
        sub,_,range_lo_sub, range_hi_sub = c 

        sub_best, sub_points = recurse(bots, name+str(sub), range_lo_sub, range_hi_sub, best)

#        print("got {} {}".format(sub_best,sub_points))

        if (sub_best > best):
            best = sub_best
            points = sub_points
#            print("Increasing best to {}".format(best))
            
        else:
            points.extend(sub_points)

    print("{} {} returns {} {}".format(range_lo, range_hi, best, points))

    return best,points

    
       


def part2():
    bots = loadFile('../data/23input.txt')

    # try and find a good starting maximum to cut down work later
    if 0:
        trial = 0
        for x in range(-2**26,2**26,2**22):
            for y in range(-2**26,2**26,2**22):
                for z in range(-2**26,2**26,2**22):
                    score = 0
                    for bot in bots:
                        if bot.sees_range([x,y,z],[x+1,y+1,z+1]):
                            score += 1        
                    if (score > trial):
                        trial = score
                        print(x,y,z,trial)        


    range_lo = [-2**30,-2**30,-2**30]
    range_hi = [2**30,2**30,2**30]

    #range_lo = [0,0,0]
    #range_hi = [64,64,64]

    # we know 305 exists

    for trial in range(1000,0,-1):
        best, points = recurse(bots, "", range_lo, range_hi, trial)
        print(best,points)
        if points:
            break
    dist = 2**30
    best = None
    for p in points:
        d = p[0]+p[1]+p[2]
        if d < dist:
            best = p
    print(d,p)        




part2()            


