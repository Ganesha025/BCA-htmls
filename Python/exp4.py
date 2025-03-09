marks = []  
for i in range(5):  
    mark = float(input(f"Enter marks for subject {i+1}: "))  
    marks.append(mark)  

avg = sum(marks) / 5  

if avg >= 90: grade = "A"  
elif avg >= 80: grade = "B"  
elif avg >= 70: grade = "C"  
elif avg >= 60: grade = "D"  
else: grade = "F"  

print(f"Average: {avg:.2f}, Grade: {grade}")  