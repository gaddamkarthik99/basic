# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main function
def main():
    # Ask user for a number
    number = int(input("Enter a number: "))

    # Calculate and display the factorial
    fact = factorial(number)
    print(f"Factorial of {number} is {fact}")

    # Check if the number is prime
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Execute the main function
if __name__ == "__main__":
    main()
