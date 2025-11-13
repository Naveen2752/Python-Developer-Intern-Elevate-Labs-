def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def main():
    print("\n===== Simple CLI Calculator =====")
    while True:
        try:
            print("\nSelect Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            # Get user input
            expression = input("Enter a mathematical expression (or type 'exit' to quit): ")

            if expression.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            # Define variables for evaluation
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Evaluate the expression
            if expression == '+':
                result = add(num1, num2)
            elif expression == '-':
                result = subtract(num1, num2)
            elif expression == '*':
                result = multiply(num1, num2)
            elif expression == '/':
                result = divide(num1, num2)
                
               # Display the result
            print(f"The result is: {result}")
    
        except Exception as e:
            print(f"Error: {e}. Please enter a valid mathematical expression.")


if __name__ == "__main__":
    main()
