class Counter:  
    count = 0  
    def __init__(self):  
        Counter.count += 1
obj1 = Counter()  
obj2 = Counter()  
obj3 = Counter()  

print("Total objects created:", Counter.count)  