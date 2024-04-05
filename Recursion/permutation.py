from typing import List

"""
Problem:
- design an algorithm to print all permutations of a string.
- For simplicity, assume all characters are unique.

input: "abc"
output: ["cab", "acb", "abc", "cba", "bca", "bac"]
"""


def permute(s: str) -> List[str]:
    # base case
    if len(s) == 1:
        return s

    output = []
    for i in range(len(s)):
        rest = s[:i] + s[i + 1 :]  # slicing
        for p in permute(rest):
            output.append(s[i] + p)

    return output


if __name__ == "__main__":
    s = str(input("enter string: "))
    print(permute(s))
