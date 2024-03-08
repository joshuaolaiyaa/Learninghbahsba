# Simple Python code to calculate the sum of two numbers

def add_numbers(a, b):
    return a + b

def main():
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    result = add_numbers(num1, num2)

    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
