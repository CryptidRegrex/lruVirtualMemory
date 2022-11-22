import sys


def main():
    len(sys.argv)
    args = []
    args = sys.argv
    args[2] = int(args[2])
    args[3] = int(args[3])
    args[4] = int(args[4])
    args[5] = int(args[5])
    if len(args) != 6:
        print("You are missing a parameter please enter algorithm type, queue size, and input file.... exiting")
        exit(0)
    q1 = readIn(args[1], 1)
    completeProcess(q1, args[2])
    q2 = readIn(args[1], 2)
    q3 = readIn(args[1], 3)
    q4 = readIn(args[1], 4)
    exit(0)


def readIn(file, process):
    fullQueue = []
    with open(file, 'r') as f:
        for line in f.readlines():
            element = line.rstrip('\n').split(' ')
            pro = int(element[0])
            if pro == process:
                #print(f"{int(element[1])}")
                fullQueue.append(int(element[1]))
    return fullQueue


def addLRU(localQueue, newVal, qSize):
    if (len(localQueue) < qSize):
        print(f"newVal {newVal}")
        element = str(localQueue[newVal]) + ',' + str(5)
        localQueue.append(element)
    return element


def hitLRU(localQueue, qSize, index):
    maxVal = qSize
    localQueue[index] = addLRU(localQueue, index, qSize)
    return localQueue
    

#def parsePage():

#def parseLRU():

#def updateLRU(localQueue, qSize, index):
    #parseLRU()
    #for page in localQueue:
        #parseLRU()

def checkHit(queue, localQueue, qSize, index):
    count = 0
    if (len(localQueue) > 0):
        for val in localQueue:
            if val == queue[index]:
                hitLRU(localQueue, qSize, count)
                print(f"count in checkHit {count}")
            count += 1
    else:
        addLRU(localQueue, count, qSize)
                
                
        


def completeProcess(queue, qSize):
    totalLoads = len(queue)
    count = 0
    q = []
    while True:
        if (count <= totalLoads):
            q = checkHit(queue, q, qSize, count)
            print(f"{q[0]}")
        else:
            break



main()