"""
최대공약수 gcd
m>n인 두 양의 정수 m과 n에 대해서 m이 n의 배수이면 gcd(m, n)=n이고,
그렇지 않으면 gcd(m, n)= gcd(n, m%n)이다.
"""


def gcd(m, n):
    # condition
    if m < n:
        temp = m
        m = n
        n = temp

    # base case
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


if __name__ == "__main__":
    m = int(input("enter m: "))
    n = int(input("enter n: "))
    print("our answer: ", gcd(m, n))
