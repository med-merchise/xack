"""Generating a list of prime numbers up to N.

See https://rebrained.com/?p=458

"""


def primes(n):
    """Prime numbers up to 'n'."""
    import math

    res = set(range(2, n + 1))
    for i in range(2, round(math.sqrt(n))):
        if i in res:
            for j in range(i + i, n + 1, i):
                if j in res:
                    res.discard(j)
    return res


if __name__ == '__main__':
    print("Welcome to prime numbers.")
    n = int(input("Enter n: "))
    print(primes(n))
