size = int(input("Enter the size of the list: "))  
arr = []  

print("Enter the elements of the list:")  
for i in range(size):  
    arr.append(int(input()))  

target = int(input("Enter the number to search: "))  

for i in range(size):  
    if arr[i] == target:  
        print(f"Element found at index {i}")  
        break  
else:  
    print("Element not found")