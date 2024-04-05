import math


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("correct answer: ", math.factorial(n))
    print("our answer: ", factorial(n))
