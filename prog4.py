import sys

hit = 0
miss = 0

"""
This is the main function that takes parameters of the file to compute hit rate for four processes. 
The input should look like such: python3 prog4 file 5 5 5 5 
Each value you enter is the size of the page table for the process
This will take arguments when initializing the program via the system command line. 
"""
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

"""
This process readsIn a file and compiles a list of all pages to process in order of acending order
Params:
file - This is the input file object that will be read in and parsed for each procees.
process - This is the integer value of the process that we are parsing into a list of pages
returns:
localQueue - This is the list of all pages that the process will use
"""
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

"""
addLRU process the first value for each process and puts it into a list
Params:
fullQueue - all items in the process queue
localQueue - all local queue items being that of the maximum page table size
page - the page we are going to append to the page table
qSize - the maximum page table size
returns:
localQueue - the page table with the first entry in it
"""
def addLRU(fullQueue, localQueue, page, qSize):
    if (len(localQueue) == 0):
        localQueue.append(str(fullQueue[0]) + ',' + str(qSize))
    return localQueue

"""
missPage does all of the calculations for adding a new page and calculating new lru values for each page
in the table
Params:
fullQueue - all items in the process queue
localQueue - all local queue items being that of the maximum page table size
index - the value of the item we need to take from fullQueue and add to localQueue
qSize - the maximum page table size
returns:
retLocalQueue - This returns the localQueue after a missPage value has been calculated
"""
def missPage(fullQueue, localQueue, qSize, index):
    global miss
    miss += 1
    retLocalQueue = []
    count = 0
    if (len(localQueue) == 0):
        page = fullQueue[0]
        retLocalQueue = addLRU(fullQueue, localQueue, page, qSize)
    elif (len(localQueue) > 0 and (len(localQueue) < qSize)):
        for i in localQueue:
            newLru = parseLRU(i) - 1
            retainPage = parsePage(i)
            retLocalQueue.append(createTableEntry(retainPage, newLru))
        retLocalQueue.append(createTableEntry(fullQueue[index], qSize))
    else:
        for i in localQueue:
            if (parseLRU(i) == 1):
                localQueue.pop(count)
                retLocalQueue = updateLRU(localQueue, qSize)
                retLocalQueue.append(createTableEntry(fullQueue[index], qSize))
                break
            count += 1
    return retLocalQueue

"""
This function creates an entry into the page table with an lru value
Params:
page - this is the page we are going to add to the table
lru - this is the value we are appending to the entry
returns:
element - This is the table entry we are going to append to our list
"""
def createTableEntry(page, lru):
    element = str(page) + ',' + str(lru)
    return element

"""
This funciton computers the new lru values if we hit a page in a page table
Params:
localQueue - This is the page table we are going to update lru values for on a page hit
qSize - This is the maximum size of the page table we are using
index - This is the locaiton of the page we hit in the page table for processing
returns:
localQueue - This is an updated queue with new lru values based on the page hit
"""
def hitPage(localQueue, qSize, index):
    global hit 
    retLocalQueue = []
    count = 0
    maxVal = qSize
    lru = parseLRU(localQueue[index])
    pageHit = parsePage(localQueue[index])
    localQueue.pop(index)
    totalVals = len(localQueue)
    while count < totalVals:
        if (lru < parseLRU(localQueue[count])):
            page = parsePage(localQueue[count])
            newlru = parseLRU(localQueue[count]) - 1
            retLocalQueue.append(createTableEntry(page, newlru))
        else:
            retLocalQueue.append(localQueue[count])
        count += 1
    retLocalQueue.append(createTableEntry(pageHit, maxVal))
    localQueue = retLocalQueue
    return localQueue
    
"""
Due to how we are storing our values in our list with each element being a page then lru value this 
will parse the page out of the element
Params:
element - This is the element we will disect for the page
returns:
page - This is the integer of the page
"""
def parsePage(element):
    item = element.split(',')
    page = int(item[0])
    return page

"""
Due to how we are storing our values in our list with each element being a page then lru value this 
will parse the lru value out of the element
Params:
element - This is the element we will disect for the lru value
returns:
lru - the integer value of the lru
"""
def parseLRU(element):
    item = str(element).split(',')
    lru = int(item[1])
    return lru


"""
This function updates the values in a full page table when a missPage occurs. Each element's lru will be
negated by one.
Params:
localQueue - The page table we are using to update our lru values
returns:
updatedQ - the page table with updated lru values
"""
def updateLRU(localQueue, qSize):
    updatedQ = []
    for i in localQueue:
        lru = parseLRU(i) - 1
        page = parsePage(i)
        updatedQ.append(createTableEntry(page, lru))
    return updatedQ


"""
This function will check for a hit or miss when analyizing the next page to load into the table.
If it hits it will call the hitPage() function and if it misses it will call the missPage() function
Params:
fullQueue - The entire list of pages the process will need to load
localQueue - The page table we are using to retain in use or used pages
qSize - The maximum size of the page table
index - the location of the next page in the fullQueue
returns:
localQueue - The new updated page table after a hitPage() or missPage()
"""
def checkHit(fullQueue, localQueue, qSize, index):
    count = 0
    found = False
    if (len(localQueue) > 0):
        for val in localQueue:
            if parsePage(val) == fullQueue[index]:
                global hit
                hit += 1
                localQueue = hitPage(localQueue, qSize, count)
                found = True
                break
            count += 1
        if (found == False):
            localQueue = missPage(fullQueue, localQueue, qSize, index)
    elif (len(localQueue) == 0):
        localQueue = missPage(fullQueue, localQueue, qSize, count)
    return localQueue
                
                
"""
This function will complete all processing of pages that are provided by the input file for a specific process
It will check for a hit every new page that is loaded from the queue
Params:
queue - This is the full queue with every page that will need to be loaded in the life of the process
qSize - This is the maximum page table size for the process
returns:
None
"""
def completeProcess(queue, qSize):
    totalLoads = len(queue)
    count = 0
    localQueue = []
    while True:
        if (count < totalLoads):
            localQueue = checkHit(queue, localQueue, qSize, count)
            count += 1
        else:
            break


if __name__ == "__main__":
    main()