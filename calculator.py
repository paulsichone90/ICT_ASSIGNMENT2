# Global variables
history = []
operations_count = 0
memory = 0

# Part 1: Implement Basic Arithmetic Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero ")
        return "Error: Division by zero "
    return num1 / num2

def modulus(num1, num2):
    if num2 == 0:
        print("Error: Modulus by zero")
        return "Error: Modulus by zero"
    return num1 % num2

# Part 2: Implement Input Handling
def get_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")
#part 3: implement history tracking 
def update_history(num1, operation, num2,result):
    history.append(f"{num1} {operation} {num2} = {result}")
    global operations_count
    operations_count += 1

def display_history():
    if not history:
        print("History is empty.")
    else:
        for entry in history:
            print(entry)

# Part 4: Test Your Calculator
def test_calculator():
    # Test operations
    print("Testing operations...")
    result1 = add(2, 3)
    print(result1)
    update_history(2, '+', 3, result1)
    
    result2 = subtract(5, 2)
    print(result2)
    update_history(5, '-', 2, result2)
    
    result3 = multiply(4, 5)
    print(result3)
    update_history(4, '*', 5, result3)
    
    result4 = divide(10, 2)
    print(result4)
    if result4 is not None and not isinstance(result4, str):
        update_history(10, '/', 2, result4)
    
    result5 = modulus(10, 3)
    print(result5)
    update_history(10, '%', 3, result5)

    # Test division by zero handling
    print(divide(10, 0))
    
    # Verify history
    display_history()
    
    # Confirm operations count
    print(f"Operations count: {operations_count}")

# Bonus features
def clear_history():
    global history
    global operations_count
    history = []
    operations_count = 0

def memory_operations(op):
    global memory
    if op == 'M+':
        try:
            num = get_number_input("Enter number to add to memory: ")
            memory += num
            print(f"Memory updated. Current memory: {memory}")
        except Exception as e:
            print(f"Error: {e}")
    elif op == 'M-':
        try:
            num = get_number_input("Enter number to subtract from memory: ")
            memory -= num
            print(f"Memory updated. Current memory: {memory}")
        except Exception as e:
            print(f"Error: {e}")
    elif op == 'MR':
        print(f"Memory: {memory}")
    elif op == 'MC':
        global memory
        memory = 0
        print("Memory cleared.")
def advanced_operations():
    num = get_number_input("Enter number for advanced operation: ")
    op = input("Enter operation (exp for exponent, sqrt for square root): ")
    if op == 'exp':
        power = get_number_input("Enter power: ")
        result = num ** power
        print(f"Result: {result}")
        update_history(num, f"^{power}", "", result)
    elif op == 'sqrt':
        if num < 0:
            print("Error: Square root of negative number.")
        else:
            result = num ** 0.5
            print(f"Result: {result}")
            update_history(num, "sqrt", "", result)
    else:
        print("Invalid operation.")
def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Perform basic operation")
        print("2. Display history")
        print("3. Clear history")
        print("4. Memory operations")
        print("5. Advanced operations")
        print("6. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            num1 = get_number_input("Enter first number: ")
            op = input("Enter operation (+, -, *, /, %): ")
            num2 = get_number_input("Enter second number: ")
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            elif op == '%':
                result = modulus(num1, num2)
            else:
                print("Invalid operation.")
                continue
            if result is not None and not isinstance(result, str):
                print(f"Result: {result}")
                update_history(num1, op, num2, result)
        elif choice == '2':
            display_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            op = input("Enter memory operation (M+, M-, MR, MC): ")
            memory_operations(op)
        elif choice == '5':
            advanced_operations()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
