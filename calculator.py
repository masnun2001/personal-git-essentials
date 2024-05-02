value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))
function = input("Enter the function: ")    
if function == "+":
    print(value1 + value2)  
elif function == "-":
    print(value1 - value2)
elif function == "*":
    print(value1 * value2)
elif function == "/":
    print(value1 / value2)
else: 
    print("Invalid function")
