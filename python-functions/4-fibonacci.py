#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []  
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers