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


def addLRU(fullQueue, localQueue, page, qSize):
    if (len(localQueue) == 0):
        localQueue.append(str(fullQueue[0]) + ',' + str(qSize))
    return localQueue
    """
    count = 0
    localQueue.append()
    for i in localQueue:

        lru = parseLRU(i)

        #localQueue.pop(count)
        count += 1
    
    if (len(localQueue) < qSize):
        print(f"newVal {newVal}")
        element = str(localQueue[newVal]) + ',' + str(5)
        localQueue.append(element)
    return element
    """

def missPage(fullQueue, localQueue, qSize, index):
    count = 0
    if (len(localQueue) == 0):
        #localQueue.append(fullQueue[index])
        page = fullQueue[0]
        localQueue = addLRU(fullQueue, localQueue, page, qSize)
        print(f"When local queue is 0 our value is {localQueue[0]}")
        #print(f"q size in miss: {qSize}")
    elif (len(localQueue) > 0 and len(localQueue) < qSize):
        #print(f"Our localQueue len is: {len(localQueue)}")
        localQueue.append(createTableEntry(fullQueue[index], (qSize - len(localQueue))))
        print(f"Still filling array {localQueue[(len(localQueue) - 1)]}")
    else:
        for i in localQueue:
            if (parseLRU(i) == 1):
                print("Are we hitting missPage once full?")
                localQueue.pop(count)
                localQueue = updateLRU(localQueue, qSize)
                localQueue.append(fullQueue[index])
                count += 1
                break
    return localQueue


def createTableEntry(page, lru):
    element = str(page) + ',' + str(lru)
    return element

def hitPage(localQueue, qSize, index):
    count = 0
    maxVal = qSize
    lru = parseLRU(localQueue[index])
    print(f"Index {index} In hitpage Page {parsePage(localQueue[index])} lru {parseLRU(localQueue[index])}")
    pageHit = parsePage(localQueue[index])
    localQueue.pop(index)
    for i in localQueue:
        if (lru < parseLRU(i)):
            page = parsePage(i)
            lru = parseLRU(i) - 1
            print(f"page {page} new lru {lru}")
            localQueue.pop(count)
            localQueue.append(createTableEntry(page, i))
            count += 1
    localQueue.append(createTableEntry(pageHit, maxVal))
    #for i in localQueue:
        #print(f"After hitPage before return {i}")
    return localQueue
    

def parsePage(element):
    item = element.split(',')
    page = int(item[0])
    return page


def parseLRU(element):
    item = str(element).split(',')
    lru = int(item[1])
    return lru

def updateLRU(localQueue, qSize):
    updatedQ = []
    for i in localQueue:
        lru = parseLRU(i) - 1
        page = parsePage(i)
        updatedQ.append(createTableEntry(page, lru))
    return updatedQ
    #parseLRU()
    #for page in localQueue:
        #parseLRU()

def checkHit(fullQueue, localQueue, qSize, index):
    count = 0
    found = False
    if (len(localQueue) > 0):
        for val in localQueue:
            if parsePage(val) == fullQueue[index]:
                #print(f"localQueue page {parsePage(val)} fullQueue page {fullQueue[index]}")
                localQueue = hitPage(localQueue, qSize, count)
                #print(f"count in checkHit {count}")
                found = True
                break
            count += 1
        #print(found)
        if (found == False):
            localQueue = missPage(fullQueue, localQueue, qSize, index)
    elif (len(localQueue) == 0):
        #addLRU(fullQueue, localQueue, count, qSize)
        localQueue = missPage(fullQueue, localQueue, qSize, count)
        #print(localQueue[0])
    for i in localQueue:
        print(f"After checkHit before return {i}")
    return localQueue
                
                

def completeProcess(queue, qSize):
    totalLoads = len(queue)
    count = 0
    localQueue = []
    while True:
        if (count <= totalLoads):
            #print(f"len value for localQueue {len(localQueue)}")
            #print(count)
            localQueue = checkHit(queue, localQueue, qSize, count)
            #print(f"{localQueue[count]}")
            count += 1
        else:
            break



main()