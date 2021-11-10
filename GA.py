import pdb,random,copy
#set seed
random.seed(0)
secretKey = list('173478fjksdjl27aef73bt4jksf9we93brf346dr7rhuifr')
n = len(secretKey)
#Initial Population
#space is 32
#digits are 48 to 57
#lowercase alphabet is 97 to 122
#uppercase is 65 to 90

def newBit(minSet,maxSet):
    c = random.randint(minSet,maxSet)
    s = random.randint(0,5)
    if(c==0):
        temp = random.randint(0,9)
        val = chr(temp + 48)
    elif(c==1):
        temp = random.randint(0,25)
        val = chr(temp+97)
    if (s==1):
        val = chr(32)
    return(val)

#track what values are being considered, range is ascii values.
#generate a random alphanumeric string of length n
def randomize():
    arr = []
    for i in range(n):
        index = random.randint(0,1)
        #generate 0-9
        if(index==0):
            val = newBit(0,0)
            arr.append(val)
        #generate a-z
        else:
            val = newBit(1,1)
            arr.append(val)
    return arr
            
#Generate potential population of size k
#a mix of lowercase letters, numbers, and spaces
def populate(k):
    fitM,popM = [0] * k,[]
    for i in range(k):
        popM.append(randomize())
    return(fitM,popM)

#fitness function, each bull is 1, each cow is 1/n
def fitness(popM,fitM):
    for i in range(len(fitM)):
        nCow,nBull = 0,0
        track = copy.deepcopy(secretKey)
        for ii in range(n):
            if(popM[i][ii] in track):
                if(track[ii] == popM[i][ii]):
                    nBull += 1
                else:
                    nCow += 1/n
                #pdb.set_trace()
                track[track.index(popM[i][ii])] = ''                
        fitM[i] = round(nCow + nBull,5)
    #pdb.set_trace()
    return(fitM)


def xfMax(fitM,x):
    count,minn,fitMCP = 0,0,fitM.copy()
    for i in range(x-1):
        fitMCP[fitMCP.index(max(fitMCP))] = minn
    return fitM.index(max(fitMCP))

#Selection, do elitism.
def pairing(fitM):
    pairNum = len(fitM)
    selected,bestFit,pairs = [0]*pairNum,fitM.index(max(fitM)),[]
    #elitism process
    for i in range(pairNum//2):
        if(i < 3):
            #pdb.set_trace()
            m1,m2 = bestFit,xfMax(fitM,i+2)
        else:
            m1 = random.randint(0,pairNum//2)
            m2 = random.randint(0,pairNum//2)
            m1,m2 = xfMax(fitM,m1),xfMax(fitM,m2)
        while(m1 == m2):
            m1 = random.randint(0,pairNum-1)
        pairs.append([m1,m2])
    return(pairs)

#First crossover function. this splits it into 3 partitions, to be swapped
def swap(list1,list2,c1):
    lenA = len(list1)
    list1S,list2S = [0]*lenA,[0]*lenA
    list1S,list2S = list2[0:c1],list1[0:c1]
    list1S[c1:lenA],list2S[c1:lenA] = list1[c1:lenA],list2[c1:lenA]
    return([list1S,list2S])

#selection function
def selection(fitM, newMates, popM):
    offspring,offspringformat,num = [],[],len(popM[0])
    num,c1=len(popM[0]),random.randint(num//10,num*9//10)
    for i in range(len(fitM)//2):
        offspring.append(swap(popM[newMates[i][0]],popM[newMates[i][1]],c1))
    for i in range(len(offspring)):
        offspringformat.append(offspring[i][0])
        offspringformat.append(offspring[i][1])
    return(offspringformat)

#random mutation function, change one value randomly
def mutate(nextGen,mutRat):
    nGen=copy.deepcopy(nextGen)
    for i in range(len(nextGen)-1):
        for ii in range(mutRat):
            n1 = random.randint(0,n-1)
            nGen[i][n1] = newBit(0,1) 
    return(nGen)

#second mutation function, swap two values
def swapMutate(nextGen,mutRat):
    nGen=copy.deepcopy(nextGen)
    for i in range(len(nextGen)-1):
        for ii in range(mutRat):
            i=i
            n1=random.randint(0,n)
            n2=random.randint(0,n)
            nGen[i][n1]=nGen[i][n2]
            
def evolution(numGens):
    x,maxx = populate(100),0
    population,fitM = x[1],x[0]
    for i in range(numGens):
        fitM=fitness(population,fitM)
        newMates=pairing(fitM)
        nextGen=selection(fitM,newMates,population)
        if(max(fitM) > maxx):
            maxx=max(fitM)
            if(maxx==n):
                print("Secret Found!")
            print("New Max at " + str(i) + " generation, fitness" + str(maxx))
            print(population[fitM.index(maxx)])
        if(i%2==0):
            nextGen=mutate(nextGen,3)
        if(i%5==0):
            nextGen=mutate(nextGen,3)
        else:
            population = nextGen
    return

evolution(10000)
