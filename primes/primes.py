# digits/primes/primes.py

import math

def get_prime_factors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2),
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors

def get_components(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
