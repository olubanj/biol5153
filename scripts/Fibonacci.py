#! /usr/bin/env python3

def get_input():
    """Get user input for the Fibonacci number to calculate."""
    number = input("Enter the number: ")
    return int(number)

def calculate_fibonacci(n):
    """Calculate the Fibonacci number for the given input."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def print_output(number, fibonacci_number):
    """Print the Fibonacci number."""
    print('The Fibonacci number for', number, 'is:', fibonacci_number)

def main():
    """Main function to execute the Fibonacci script."""
    number = get_input()
    fibonacci_number = calculate_fibonacci(number)
    print_output(number, fibonacci_number)

if __name__ == '__main__':
    main()

