def is_prime(num):
    """Checks if a number is prime and returns True or False."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    """Generates a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]