def binarySearch(list, target):
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        guess = (lower + upper)//2
        if list[guess] == target:
            return guess 
        elif list[guess] > target:
            upper = guess - 1
        else:
            lower = guess + 1

list = [1,2,3,4,5,6,7,8,9]






class Human():
    def __init__(self, height, weight, age, name):
        self.height = height 
        self.weight = weight
        self.age = age
        self.name = name
    def isOverWeight(self, weight):
        if self.weight > 300:
            return True
        return False

ansh = Human(6, 150, 18, "Ansh")

print(ansh.age)

















