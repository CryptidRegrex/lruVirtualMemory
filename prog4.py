import sys

hit = 0
miss = 0


def main():
    totalHit = 0
    allPages = 0
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
    totals = []
    global hit
    global miss
    #Process 1
    q1 = readIn(args[1], 1)
    completeProcess(q1, args[2])
    totalHit += hit
    allPages += hit + miss
    totalP = hit + miss
    totals.append(hit/totalP * 100)
    hit = 0
    miss = 0
    #Process 2
    q2 = readIn(args[1], 2)
    completeProcess(q2, args[3])
    totalHit += hit
    allPages += hit + miss
    totalP = hit + miss
    totals.append(hit/totalP * 100)
    hit = 0
    miss = 0
    #Process 3
    q3 = readIn(args[1], 3)
    completeProcess(q3, args[4])
    totalHit += hit
    allPages += hit + miss
    totalP = hit + miss
    totals.append(hit/totalP * 100)
    hit = 0
    miss = 0
    #Process 4
    q4 = readIn(args[1], 4)
    completeProcess(q4, args[5])
    totalHit += hit
    allPages += hit + miss
    totalP = hit + miss
    totals.append(hit/totalP * 100)
    #Print final values
    print(f"P1: {totals[0]} P2: {totals[1]} P3: {totals[2]} P4: {totals[3]} PT: {totalHit/allPages * 100}")
    #print(hit)
    #print(miss)
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
    global miss
    miss += 1
    #print(f"SIZE of our localQueue at the beginning of missPage function: {len(localQueue)}")
    #print(fullQueue[index])
    retLocalQueue = []
    count = 0
    if (len(localQueue) == 0):
        #localQueue.append(fullQueue[index])
        page = fullQueue[0]
        retLocalQueue = addLRU(fullQueue, localQueue, page, qSize)
        #print(f"When local queue is 0 our value is {localQueue[0]}")
        #print(f"q size in miss: {qSize}")
    elif (len(localQueue) > 0 and (len(localQueue) < qSize)):
        #print(f"Our localQueue len is: {len(localQueue)}")
        #for i in localQueue:
            #print(f"What are we about to look through in missPage before the queue is full? {i}")
        for i in localQueue:
            #print(f"Our value being analyized in missPage is {i}")
            newLru = parseLRU(i) - 1
            retainPage = parsePage(i)
            #localQueue.pop(count)
            retLocalQueue.append(createTableEntry(retainPage, newLru))
            #count += 1
        retLocalQueue.append(createTableEntry(fullQueue[index], qSize))
        #print(f"After our elif statement our retlocalQueue is size: {len(retLocalQueue)}")
        #print(f"Still filling array {localQueue[(len(localQueue) - 1)]}")
    else:
        for i in localQueue:
            #for x in localQueue:
                #print(f"Our values in the localQueue before checking if lru == 1 {x}")
            #print(f"ELSE statement in missPage function size of local queue {len(retLocalQueue)}")
            if (parseLRU(i) == 1):
                #print("Are we hitting missPage once full?")
                #print(parseLRU(i))
                localQueue.pop(count)
                retLocalQueue = updateLRU(localQueue, qSize)
                retLocalQueue.append(createTableEntry(fullQueue[index], qSize))
                #print(f"ELSE statement in missPage function size of local queue {len(retLocalQueue)}")
                break
            count += 1
        #for x in retLocalQueue:
            #print(f"Our values when returning from missPage ELSE: {x}")    
    #print(f"When returning our localQueue in missPage function the size is: {len(retLocalQueue)}")
    return retLocalQueue


def createTableEntry(page, lru):
    element = str(page) + ',' + str(lru)
    return element

def hitPage(localQueue, qSize, index):
    global hit 
    #hit += 1
    retLocalQueue = []
    count = 0
    maxVal = qSize
    lru = parseLRU(localQueue[index])
    #print(f"Index {index} In hitpage Page {parsePage(localQueue[index])} lru {parseLRU(localQueue[index])}")
    pageHit = parsePage(localQueue[index])
    localQueue.pop(index)
    #for i in localQueue:
        #print(f"After popping the value we have these in the localQ {i} and our len of localQ is {len(localQueue)}")
    totalVals = len(localQueue)
    while count < totalVals:
    #for i in localQueue:
        if (lru < parseLRU(localQueue[count])):
            page = parsePage(localQueue[count])
            newlru = parseLRU(localQueue[count]) - 1
            #print(f"page {page} new lru {lru}")
            #print(f"localQueue with count before pop {localQueue[count]}")
            #localQueue.pop(count)
            #localQueue.append(createTableEntry(page, newlru))
            retLocalQueue.append(createTableEntry(page, newlru))
        else:
            retLocalQueue.append(localQueue[count])
        count += 1
    retLocalQueue.append(createTableEntry(pageHit, maxVal))
    localQueue = retLocalQueue
    #for i in localQueue:
        #print(f"After hitPage before return {i}")
    #print(f"When returning our localQueue in hitPage function the size is: {len(localQueue)}")
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
    #print(f"When returning our localQueue in updateLRU function the size is: {len(localQueue)}")
    return updatedQ
    #parseLRU()
    #for page in localQueue:
        #parseLRU()

def checkHit(fullQueue, localQueue, qSize, index):
    count = 0
    found = False
    if (len(localQueue) > 0):
        for val in localQueue:
            #print(f"localQueue page {parsePage(val)} fullQueue page {fullQueue[index]}")
            if parsePage(val) == fullQueue[index]:
                global hit
                hit += 1
                #print(f"The size of our localQueue before a hitPage call is: {len(localQueue)}")
                localQueue = hitPage(localQueue, qSize, count)
                #print(f"WE FOUND OUR VALUE | localQueue page {parsePage(val)} fullQueue page {fullQueue[index]}")
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
    #for i in localQueue:
        #print(f"After checkHit before return {i}")
    #print("checkHit is finished")
    return localQueue
                
                

def completeProcess(queue, qSize):
    totalLoads = len(queue)
    count = 0
    localQueue = []
    while True:
        if (count < totalLoads):
            #print(f"len value for localQueue {len(localQueue)}")
            #print(count)
            localQueue = checkHit(queue, localQueue, qSize, count)
            #print(f"{localQueue[count]}")
            count += 1
        else:
            break



main()