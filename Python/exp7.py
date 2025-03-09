arr = list(map(int, input("Enter numbers: ").split()))  
size = len(arr)  
temp = [[num] for num in arr]  

while len(temp) > 1:  
    merged = []  
    for i in range(0, len(temp) - 1, 2):  
        merged.append(sorted(temp[i] + temp[i + 1]))  
    if len(temp) % 2:  
        merged.append(temp[-1])  
    temp = merged  

print("Sorted array:", temp[0])  
