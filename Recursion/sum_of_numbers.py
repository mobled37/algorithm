from typing import List


# wrong answer
def sum_of_numbers_none_tail_recursion(lst: List[int]) -> int:
    # base case
    if len(lst) == 1:
        return lst[0]
    else:
        return sum_of_numbers_none_tail_recursion(lst[:-1]) + lst[-1]


# correct answer
def sum_of_numbers_tail_recursion(lst: List[int], total: int = 0) -> int:
    # base case
    if len(lst) == 0:
        return total
    else:
        return sum_of_numbers_tail_recursion(lst[:-1], total + lst[-1])


# using helper function
def helper_sum_of_numbers_tail_recursion(lst: List[int]) -> int:
    def helper(lst: List[int], total: int = 0):
        if len(lst) == 0:
            return total
        else:
            return helper(lst[:-1], total + lst[-1])

    return helper(lst, 0)


if __name__ == "__main__":
    lst = [9, 4, 3, 2, 1, 5, 6, 7, 8, 10]
    print("our answer: ", helper_sum_of_numbers_tail_recursion(lst))
    print("correct answer: ", sum(lst))
