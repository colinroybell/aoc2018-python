def disp(a,size):
    for y in range(size):
        for x in range(size):
            print(a[y][x],end='')
        print()
    print()

def process(a,size):
    b = [['.'] * size for i in range(size)]

    for y in range(size):
        for x in range(size):
            count = {'.':0, '|': 0, '#': 0}
            for yy in range(y-1,y+2):
                for xx in range(x-1,x+2):
                    if yy >= 0 and yy < size and xx >=0 and xx < size and not (yy==y and xx==x):
                        c = a[yy][xx]
                        count[c] = count[c] + 1    
            s = a[y][x]
            if s == '.':
                if count['|']>=3:
                    out = '|'
                else:
                    out = '.' 
            elif s == '|':
                if count['#']>=3:
                    out = '#'
                else:
                    out = '|'
            elif s == '#':
                if count['#']>=1 and count['|']>=1:
                    out = '#'
                else:
                    out = '.' 
            b[y][x] = out
    return b               

def part1(filename, size):
    a = [['.'] * size for i in range(size)]
    with open(filename,'r') as f:
        y = 0
        for line in f:
            x = 0
            line = line.rstrip('\n')
            for c in line:
                a[y][x] = c
                x += 1
            y += 1    

    disp(a,size)
    for i in range(10):
        b = process(a,size)    
        a = b 
        disp(a,size)

    count = {'.':0,'|':0,'#':0}
    for y in range(size):
        for x in range(size):
            c = a[y][x]
            count[c] = count[c]+1

    print("{} x {} = {}".format(count['#'],count['|'],count['#']*count['|']))      

def part2(filename,size):
    a = [['.'] * size for i in range(size)]
    with open(filename,'r') as f:
        y = 0
        for line in f:
            x = 0
            line = line.rstrip('\n')
            for c in line:
                a[y][x] = c
                x += 1
            y += 1    

    cache = []
    m = -1
    n = 0
    while m == -1:
        cache.append(a)
        b = process(a,size)    
        a = b
        n += 1 
        for j in range(n):
            if a == cache[j]:
                m = j

    print("Repeat from {} to {}".format(m,n))

    cachePos = (1000000000-m)%(n-m) + m

    count = {'.':0,'|':0,'#':0}
    for y in range(size):
        for x in range(size):
            c = cache[cachePos][y][x]
            count[c] = count[c]+1

    print("{} x {} = {}".format(count['#'],count['|'],count['#']*count['|']))      





    
    

#part1('../data/18test1.txt',10)
part1('../data/18input.txt',50)
part2('../data/18input.txt',50)

