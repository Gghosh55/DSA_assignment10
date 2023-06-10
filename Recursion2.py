def lastRemaining(n):
    if n == 1:
        return 1

    if n % 2 == 1:
        return lastRemaining(n - 1)
    else:

        return n - lastRemaining(n // 2) + 1
print(lastRemaining(9))
print(lastRemaining(1))
