import random 

def randomList():
    length = random.randint(1,20)
    list = []
    for i in range(length):
        i = random.randint(1,200)
        list.append(i)
    return list 

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)
    
def selectionSort(list):
    goalLength = len(list)
    sortedList = []
    while len(sortedList) < goalLength:
        max = greatest(list)
        sortedList.append(max)
        list.remove(max)
    return sortedList

def greatest(list):
    max = 0 
    for i in list:
        if i>max:
            max = i
    return max

def length(list):
    if not list:
        return 0
    return 1 + length(list[1:])

def sum(list):
    if len(list) == 0:
        return 0 
    if len(list) == 1:
        return list[0]
    return list[0] + sum(list[1:])
