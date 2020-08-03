# Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 45.
# Output Format. Output 𝐹𝑛.


def calculate_fibo(limit):
    if limit <= 1:
        return limit
    else:
        first = 0
        second = 1
        for i in range(1, limit):
            third = first + second
            first = second
            second = third
        return third


n = int(input())
if 0 <= n <= 45:
    fibo_n = calculate_fibo(n)  # Returns the nth Fibonacci number
    print(fibo_n)
