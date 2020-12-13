def loadFile(filename):
    with open(filename,"r") as f:
        strings=[]
        for line in f:
            line = line.rstrip('\n')
            strings.append(line)

    return strings

def part1():
    strings = loadFile("../data/02input.txt") 
    
    twos = 0
    threes = 0

    for string in strings:
        counts = {}
        for char in string:
            counts[char] = counts.get(char,0) + 1

        two = False
        three = False

        for k,v in counts.items():
            if v==2:
                two = True
            if v==3:
                three = True

      
        if two:
            twos += 1
        if three:
            threes += 1

    print("*** {}".format(twos*threes))                            

def part2():
    strings = loadFile("../data/02input.txt")

    for s1 in range(0,len(strings)):
        for s2 in range(s1+1,len(strings)):
            string1 = strings[s1]
            string2 = strings[s2]
            miss = 0
            shared = ''
            for c in range(0,len(string1)):
                char1 = string1[c]
                char2 = string2[c]
                if (char1 == char2):
                    shared += char1
                else:
                    miss += 1
                if (miss > 1):
                    break
            else:
                print("*** {}".format(shared)) 

part1()
part2()