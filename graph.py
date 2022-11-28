from collections import deque 
graph =  {}

graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    searchQueue = deque()
    searchQueue += graph[name]
    searched = []
    while searchQueue:
        person = searchQueue.popleft()
        if person not in searched:
            if isMangoSeller(person):
                print(person + " is a mango seller!")
                return True 
            else:
                searched.append(person)
                searchQueue += graph[person]
    return False 

def isMangoSeller(name):
    return name[-1] == 'b'

#print(search("you"))

print(graph)