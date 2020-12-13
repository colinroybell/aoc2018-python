import re

def loadFile(filename):
    with open(filename,"r") as f:
        strings=[]
        for line in f:
            line = line.rstrip('\n')
            strings.append(line)

    return strings

class Claim:

    @classmethod
    def init_regexp(cls):
        cls.regexp = re.compile('\#(\d+) @ (\d+),(\d+):\s(\d+)x(\d+)')

    def __init__(self, string):
        result = self.regexp.match(string)
        self.num = int(result.group(1))
        self.x_base = int(result.group(2))
        self.y_base = int(result.group(3))
        self.x_range = int(result.group(4))
        self.y_range = int(result.group(5))

def bothParts():
    strings = loadFile('../data/03input.txt')
    Claim.init_regexp()
    claims = []
    for string in strings:
        claims.append(Claim(string))

    x_max = 0
    y_max = 0

    for claim in claims:
        x_claim_max = claim.x_base + claim.x_range
        y_claim_max = claim.y_base + claim.y_range

        x_max = max(x_max,x_claim_max) 
        y_max = max(y_max,y_claim_max)

    # 0 nobody claimed, -1 multiple claims
    grid = [[0] * y_max for i in range(x_max)]

    uncontested = set()
    contested_count = 0

    for claim in claims:
        uncontested.add(claim.num)

        for x in range(claim.x_base,claim.x_base+claim.x_range):
            for y in range(claim.y_base,claim.y_base+claim.y_range):
                if (grid[x][y] == 0):
                    # claim it
                    grid[x][y] = claim.num
                elif (grid[x][y]>0):
                    # one other claim
                    contested_count += 1
                    uncontested.discard(grid[x][y])
                    uncontested.discard(claim.num)
                    grid[x][y] = -1
                 
                else:
                    # already multiple claims
                    uncontested.discard(claim.num)


    print("*** {}".format(contested_count))
    assert(len(uncontested)==1)
    part2 = uncontested.pop()
    print("*** {}".format(part2))

bothParts()