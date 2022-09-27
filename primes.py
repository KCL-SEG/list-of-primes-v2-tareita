"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("must be positive")
    list = []
    i = 1
    while len(list) < number_of_primes:
        is_prime = True 
        for j in range(2, i-1):
            if i / j == i // j:
                is_prime = False
        if is_prime:
            list.append(i)
        i += 1
    return list
