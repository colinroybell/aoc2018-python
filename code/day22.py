import heapq

# Hacky. Also note that there are more efficient methods than breadth-first search.

def part1_2(depth,target_x,target_y):
    erosion = [[0] * (10*target_y+1) for x in range (50*target_x+1)]
    risk = 0
    # hack to allow for going beyond target
    for x in range(0,50*target_x+1):
        for y in range(0,10*target_y+1):
            if x ==0 and y == 0:
                index = 0
            elif x == 0:
                index = y * 48271
            elif y == 0:
                index = x * 16807
            elif x == target_x and y == target_y:
                index = 0
            else:    
                index = erosion[x][y-1] * erosion[x-1][y]

            e = (index + depth) % 20183

            erosion[x][y] = e
            print("{},{} = {}".format(x,y,e))

            if (x < target_x or y < target_y):
                risk += e % 3

    print(risk)

    for y in range(16):
        for x in range(16):
            s = ['.','=','|']
            geology = erosion[x][y] % 3
            print(s[geology],end='')
        print()

    done = set()
    found = False
    time = 0

    # status is x,y,holding
    # 0 is neither, 1 torch, 2 climbing.

    q = []
 
    heapq.heappush(q,(0,(0,0,1)))
    while q and not found:
        item = heapq.heappop(q)
        t = item[0]
        state = item[1]
        if state not in done:
            done.add(state)
            
         
            x = state[0]
            y = state[1]
            gear = state[2]
            geology = erosion[x][y] % 3
            print("Considering {}:{} g = {}".format(t,state,geology))

            if (x == target_x and y == target_y and gear == 1):
                found = True
                time = t

            # Add the change state
          
            other_gear = 3 - geology - gear
            heapq.heappush(q,(t+7,(x,y,other_gear)))

            for d in range(4):
                new_x = x
                new_y = y

                if d==0:
                    new_x -= 1
                if d==1:
                    new_x += 1
                if d==2:
                    new_y -= 1
                if d==3:
                    new_y += 1
                if (new_x >=0 and new_y >=0):
                    geology = erosion[new_x][new_y] % 3
                    if (gear != geology):
                        heapq.heappush(q,(t+1,(new_x,new_y,gear)))    

    print(time)





part1_2(510,10,10)   
part1_2(4848,15,700)    