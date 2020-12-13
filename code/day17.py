import re

def disp(squares,maxY,minX,maxX):
    for y in range(0,maxY+1):
        for x in range(minX,maxX+1):
            res = squares.get((x,y))
            print(res,end='')
        print()    
    print()

def supported(squares,x,y):
    below=(x,y+1)
    if below not in squares:
        return False
    return squares[below] == '#' or squares[below] == '~'

def leftExtend(squares,x,y):
    while (supported(squares,x,y)):
        if (squares[(x-1,y)]=='#'):
            # block
            return (x,True)
        x -= 1
    return (x,False)     

def rightExtend(squares,x,y):
    while (supported(squares,x,y)):
        if (squares[(x+1,y)]=='#'):
            # block
            return (x,True)
        x += 1
    return (x,False)     

def part1(filename):
    squares = {}
    maxY = 0
    minY = 1e6
    minX = 500
    maxX = 500

    line_re = re.compile('([xy])=(\d+),\s+([xy])=(\d+)\.\.(\d+)')

    with open(filename,'r') as f:
        for line in f:
            m = line_re.search(line)
            assert(m)
            type = m.group(1)
            a = int(m.group(2))
            i = int(m.group(4))
            j = int(m.group(5))

            if (type == 'x'):
                if j > maxY:
                    maxY = j
                if i < minY:
                    minY = i    
                if a-1 < minX:
                    minX = a-1
                if a+1 > maxX:
                    maxX = a+1        
                for n in range(i,j+1):
                    squares[(a,n)] = '#'
            else:
                if a > maxY:
                    maxY = a
                if a < minY:
                    minY = a    
                if i-1 < minX:
                    minX = i-1
                if j+1 > maxX:
                    maxX = j+1
                for n in range(i,j+1):
                    squares[(n,a)] = '#'                     

    squares[(500,0)] = '+'
    stack = []

    for y in range(0,maxY+1):
        for x in range(minX,maxX+1):
            if (x,y) not in squares:
                squares[(x,y)]='.'


    disp(squares,maxY,minX,maxX)                

    y = 1
    while y<=maxY and squares[(500,y)] != '#':
        squares[(500,y)] = '|'
        stack.append((500,y))
        y += 1

    disp(squares,maxY,minX,maxX)        

    while(len(stack)):
        x,y = stack.pop()
        print("pop ({},{})".format(x,y))
        if squares[(x,y)] == '~':
            continue

        x_left,x_block = leftExtend(squares,x,y)
        x_right,y_block = rightExtend(squares,x,y)

        if (x_block and y_block):
            for i in range(x_left,x_right+1):
                squares[(i,y)] = '~'
        else:
            for i in range(x_left+1,x_right):
                squares[(i,y)] = '|'

            # we only push these squares once (need to in case everything below fills up)
            if x_left < x and squares[(x_left,y)] != '|':
                j = y
                while j <= maxY and squares[(x_left,j)] != '#' and squares[(x_left,j)] != '~':
                    squares[(x_left,j)] = '|'
                    stack.append((x_left,j))
                    print("push ({},{})".format(x_left,j))
                    j += 1
                    
            if x_right > x and squares[(x_right,y)] != '|':
                j = y
                while j <= maxY and squares[(x_right,j)] != '#' and squares[(x_right,j)] != '~':
                    squares[(x_right,j)] = '|'
                    stack.append((x_right,j))
                    print("push ({},{})".format(x_right,j))
                    j += 1

    disp(squares,maxY,minX,maxX)            
   
    count = 0
    remainCount = 0
    for y in range(minY,maxY+1):
        for x in range(minX,maxX+1):
            if squares[(x,y)] == '|' or squares[(x,y)] == '~':
                count += 1
            if squares[(x,y)] == '~':
                remainCount += 1    

 
    print("{},{}".format(minY,maxY))
    print("{} {}".format(count,remainCount))







part1('../data/17input.txt')