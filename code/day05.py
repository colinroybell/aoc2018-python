import re

def loadFile(filename):
    with open(filename,"r") as f:
        strings=[]
        for line in f:
            line = line.rstrip('\n')
            strings.append(line)

    return strings

def match(a,b):
    return a.upper() == b.upper() and not a == b

def matchpair(a,b):
    return a.upper() == b.upper()    

def bothParts():
    strings = loadFile('../data/05input.txt')
   
    string = strings[0]

    units = set()
    residue = []

    for c in string:
        if len(residue) > 0 and match(c,residue[-1]):
            residue.pop()
        else:
            residue.append(c)
        units.add(c.upper())

    print("*** {}".format(len(residue)))

    # part 2
    size = len(residue)
    for exclude in units:
        residue = []
        for c in string:
            if matchpair(c,exclude):
                pass
            elif len(residue) > 0 and match(c,residue[-1]):
                residue.pop()
            else:
                residue.append(c)                
        size = min(size,len(residue))

    print("*** {}".format(size))    

bothParts()

