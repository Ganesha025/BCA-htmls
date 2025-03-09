try:
    num = int(input("Enter a number: "))
    result = 10 / num  
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Program execution completed.")
