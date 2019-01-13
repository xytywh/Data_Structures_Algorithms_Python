def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0), factorial(1), factorial(2), factorial(3), factorial(9))
