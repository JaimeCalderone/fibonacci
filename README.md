# Fibonacci Sequence Generator

This is a simple command-line application written in Python that calculates and returns the largest Fibonacci number less than or equal to a given input number. The program prompts the user to enter a number and then outputs the corresponding Fibonacci number.

## Features

- **Efficient Calculation**: Uses an iterative approach without storing the entire Fibonacci sequence.
- **User-Friendly Interface**: Prompts the user for input with a clear message.
- **Error Handling**: Validates user input and handles negative numbers and non-integer inputs gracefully.

## Requirements

- Python 3.x installed on your system.

## How to Run the Program

1. **Clone or Download the Script**

   You can download the `fibonacci.py` script from this repository or clone it using git:

   ```bash
   git clone https://github.com/JaimeCalderone/fibonacci.git
   cd fibonacci
   ```

2. **Run the script**

    Open a terminal or command prompt in the directory containing fibonacci.py and run:

    ```bash
    python3 fibonacci.py
    ```

3. **Enter the number when prompted**

    ```bash
    Enter a number to receive the largest Fibonacci number less than or equal to it:
    ```

## Example Usage

```bash
$ python fibonacci.py
Enter a number to receive the largest Fibonacci number less than or equal to it: 100
89
```

## Code Overview

The program consists of a function find_last_fibonacci(number) that calculates the largest Fibonacci number less than or equal to the input number. Here's a brief explanation:

 - **Input Validation**: Checks if the input is a non-negative integer.
 - **Fibonacci Calculation**: Iteratively computes Fibonacci numbers using two variables to store the last two numbers in the sequence.
 - **Output**: Prints the result directly to the console.

 ## Error Handling

 If an invalid input is provided (e.g., a negative number or non-integer), the program will display an error message:

 ```bash
$ python fibonacci.py
Enter a number to receive the largest Fibonacci number less than or equal to it: -5
Error: The number must be positive.
```