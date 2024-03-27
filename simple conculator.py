def add(num1, num2): 
    return num1 + num2 
 
def minus(num1, num2): 
    return num1 - num2 
 
def divide(num1, num2): 
    return num1 / num2 
 
def multiply(num1, num2): 
    return num1 * num2 
 
 
while True: 
    num1 = int(input("Enter your first number: ")) 
    num2 = int(input("Enter your second number: ")) 
 
    operators = ["", "Choose an operator", "1. Add.", "2. Minus.", "3. Divided.", "4. Multiply", 
                 "// It has to be a number (1-4)", " "] 
    for x in operators: 
        print(x) 
    number = int(input("Your operator: ")) 
 
    if number == 1: 
        print(num1, "+", num2, "=", add(num1, num2)) 
 
 
    elif number == 2: 
        print(num1, "-", num2, "=", minus(num1, num2)) 
 
 
    elif number == 3: 
        if ((divide(num1, num2)) % 2) == 0: 
            int_number = int(divide(num1, num2)) 
            print(num1, "/", num2, "=", int_number) 
        else: 
            print(num1, "/", num2, "=", divide(num1, num2)) 
 
 
    elif number == 4: 
        print(num1, "*", num2, "=", multiply(num1, num2)) 
 
    else: 
        print("There's no operator like this from the list :(") 
