#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < n:
            next_number = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_number)
        return fibonacci

# Test the function with the provided examples
if __name__ == "__main__":
    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))