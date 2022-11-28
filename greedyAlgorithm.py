statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

finalStations = set()

bestStation = None
statesCovered = set()

while statesNeeded:
    for station, statesForStation in stations.items(): #stations.items() returns a list of tuples
        covered = statesNeeded & statesForStation
        if len(covered) > len(statesCovered):
            bestStation = station
            statesCovered = covered


    finalStations.add(bestStation)
    statesNeeded -= statesCovered

print(finalStations)