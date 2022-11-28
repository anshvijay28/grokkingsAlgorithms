def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        lower = [i for i in list[1:] if i <= pivot]
        upper = [i for i in list[1:] if i > pivot]
        return quicksort(lower) + [pivot] + quicksort(upper)

print(quicksort([1,2,5433,6,45,2,6]))