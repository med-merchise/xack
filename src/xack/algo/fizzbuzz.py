"""Fizz-Buzz problem.

FizzBuzz is a common coding task given during interviews that tasks candidates
to write a solution that prints integers one-to-N, labeling any integers
divisible by three as "Fizz", integers divisible by five as "Buzz" and
integers divisible by both three and five as "FizzBuzz".

Given an integer N, return a string array answer (1-indexed) where:

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.

- answer[i] == "Fizz" if i is divisible by 3.

- answer[i] == "Buzz" if i is divisible by 5.

- answer[i] == i (as a string) if none of the above conditions are true.

See https://leetcode.com/problems/fizz-buzz/

"""


def fizz_buzz_1(n: int) -> list[str]:
    """Fizz-Buzz version 1."""
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res


def fizz_buzz_2(n: int) -> list[str]:
    """Fizz-Buzz version 2."""
    res = []
    for i in range(1, n + 1):
        aux = "Fizz" if i % 3 == 0 else ""
        if i % 5 == 0:
            aux += "Buzz"
        elif not aux:
            aux = str(i)
        res.append(aux)
    return res


def fizz_or_buzz(i: int) -> str:
    """Return the 'Fizz' or 'Buzz' string version of an integer argument.

    Saving a division.

    """
    res = "Fizz" if i % 3 == 0 else ""
    if i % 5 == 0:
        res += "Buzz"
    elif not res:
        res = str(i)
    return res


def fizz_buzz_3(n: int) -> list[str]:
    """Fizz-Buzz version 3.

    Using list comprehension and an auxiliary function.

    """
    return [fizz_or_buzz(i) for i in range(1, n + 1)]


def fizz_buzz_4(n: int) -> list[str]:
    """Fizz-Buzz version 4.

    Using list comprehension and no auxiliary function.

    """
    return [
        (
            ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
            or str(i)
        )
        for i in range(1, n + 1)
    ]


if __name__ == "__main__":
    from random import randint

    print("Welcome to Fizz-Buzz")
    n = int(input("Enter n: "))
    match randint(1, 4):  # We select a random function.
        case 1:
            fn = fizz_buzz_1
        case 2:
            fn = fizz_buzz_2
        case 3:
            fn = fizz_buzz_3
        case 4:
            fn = fizz_buzz_4
    print(f"Using function {fn.__name__}", fn(n))
