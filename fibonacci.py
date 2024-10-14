import sys

def find_last_fibonacci(number: int):
    if number < 0:
        raise ValueError("The number must be positive.")
    elif number == 0:
        return 0
    elif number == 1:
        return 1

    a, b = 0, 1
    while b <= number:
        a, b = b, a + b
    return a

if __name__ == "__main__":
    import sys
    try:
        number = int(input("Enter a number to receive the largest Fibonacci number less than or equal to it: "))
        last_fib = find_last_fibonacci(number)
        print(last_fib)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
