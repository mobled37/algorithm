def power(x: int, n: int) -> int:
    if n == 0:  # base case
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    x = int(input("enter x: "))
    n = int(input("enter n: "))
    print("our answer: ", power(x, n))
