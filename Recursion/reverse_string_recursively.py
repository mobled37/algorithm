def reverse(s: str) -> str:
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


# 처음의 s[0]가 계속 살아있다는 것을 명심

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("correct answer: ", s[::-1])
    print("our answer: ", reverse(s))
