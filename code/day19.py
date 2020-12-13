# also for day21

# What the program is doing is summing the factors of 893 (part 1) and 10551293 (part 2)

# day 21: we optimise the middle loop, which is doing a divide
# program inspection shows that we don't touch reg0, and if it is equal to reg5 at 
# step 28, we terminate. Hence we get first termination by seeing what value is at
# this point first.

def in_range(r):
    return r>=0 and r<=5
   
    
def process(op, A, B, C, reg):
    if op == 'addr':
        assert(in_range(A) and in_range(B) and in_range(C))
        reg[C] = reg[A] + reg[B]
    elif op == 'addi':
        assert(in_range(A) and in_range(C))
        reg[C] = reg[A] + B
    elif op == 'mulr':
        assert(in_range(A) and in_range(B) and in_range(C))
        reg[C] = reg[A] * reg[B]
    elif op == 'muli':
        assert(in_range(A) and in_range(C))
        reg[C] = reg[A] * B
    elif op == 'banr':
        assert(in_range(A) and in_range(B) and in_range(C))
        reg[C] = reg[A] & reg[B]
    elif op == 'bani':
        assert(in_range(A) and in_range(C))
        reg[C] = reg[A] & B
    elif op == 'borr':
        assert(in_range(A) and in_range(B) and in_range(C))
        reg[C] = reg[A] | reg[B]
    elif op == 'bori':
        assert(in_range(A) and in_range(C))
        reg[C] = reg[A] | B
    elif op == 'setr':
        assert(in_range(A) and in_range(C))
        reg[C] = reg[A] 
    elif op == 'seti':
        assert(in_range(C))
        reg[C] = A   
    elif op == 'gtir':
        assert(in_range(B) and in_range(C))
        if A > reg[B]:
            reg[C] = 1
        else:
            reg[C] = 0
    elif op == 'gtri':
        assert(in_range(A) and in_range(C))
        if reg[A] > B:
            reg[C] = 1
        else:
            reg[C] = 0
    elif op == 'gtrr':
        assert(in_range(A) and in_range(B) and in_range(C))
        if reg[A] > reg[B]:
            reg[C] = 1
        else:
            reg[C] = 0                                           
    elif op == 'eqir':
        assert(in_range(B) and in_range(C))
        if A == reg[B]:
            reg[C] = 1
        else:
            reg[C] = 0
    elif op == 'eqri':
        assert(in_range(A) and in_range(C))
        if reg[A] == B:
            reg[C] = 1
        else:
            reg[C] = 0
    elif op == 'eqrr':
        assert(in_range(A) and in_range(B) and in_range(C))
        if reg[A] == reg[B]:
            reg[C] = 1
        else:
            reg[C] = 0             
    else:
        assert 0, "unknown opcode {}".format(op)    

    return reg

def loadFile(filename):
    ip = 0
    program = []
    with open(filename,"r") as f:
        for line in f:
            line = line.rstrip('\n')
            string = line.split(' ')
            print(string)
            if (string[0]=='#ip'):
                ip = int(string[1])
            else:
                program.append([string[0],int(string[1]),int(string[2]),int(string[3])])    
    return (ip, program)


def bothParts(init_reg0):
    ip_loc, program = loadFile('../data/21input.txt')
  
    regs=[0]*6
 
    regs[0] = init_reg0

#    regs = [1,10000000,3,20000000,10551293,3]

    ip = regs[ip_loc]
    print(program)
    steps = 0
    while (ip >=0 and ip < len(program) and steps < 10000):
        regs = process(program[ip][0],program[ip][1],program[ip][2],program[ip][3],regs)
        print(program[ip], regs)
        regs[ip_loc] += 1
        ip = regs[ip_loc]
        steps += 1

    print(regs[0])    

def day21_part1():
    ip_loc, program = loadFile('../data/21input.txt')
  
    regs=[0]*6
#    regs[0] = 12935354
 
    ip = regs[ip_loc]
    print(program)
    steps = 0
    while (ip >=0 and ip < len(program) and steps < 10000):
        if ip == 19:
            # optimise this loop
            print("opt")
            regs[4] = regs[1]//256 
            regs[3] = (regs[4]+1) * 256
        else:    
            regs = process(program[ip][0],program[ip][1],program[ip][2],program[ip][3],regs)
        print(ip,program[ip], regs)
        regs[ip_loc] += 1
        ip = regs[ip_loc]
        steps += 1

    print(regs[0])    


def day21_part2():
    comps = set()
    ip_loc, program = loadFile('../data/21input.txt')
  
    regs=[0]*6

    last_comp = -1
    ip = regs[ip_loc]
    print(program)
    steps = 0
    while (ip >=0 and ip < len(program)):
        if ip == 19:
            # optimise this loop
            print("opt")
            regs[4] = regs[1]//256 
            regs[3] = (regs[4]+1) * 256
        else:    
            regs = process(program[ip][0],program[ip][1],program[ip][2],program[ip][3],regs)
        if ip == 28:
            comp = regs[5]
            if comp in comps:
                print(last_comp)
                break
            else:
                comps.add(comp)
                last_comp = comp     
            print(last_comp)
                
#        print(ip,program[ip], regs)
        regs[ip_loc] += 1
        ip = regs[ip_loc]
        steps += 1

def bothParts19_quick(n):
    i = 1
    sum = 0
    while i*i < n:
        if (n%i == 0):
            sum += i + n//i
        i+=1
    if (i*i==n):
        sum+=i

    print(sum)         



# day 19
#bothParts_quick(893)
#bothParts_quick(10551293)

#day21_part1() # we work out the first place it will terminate
day21_part2()
#bothParts_quick(893)
#bothParts_quick(10551293)