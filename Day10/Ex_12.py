import math


def is_prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


count = 1
i = 3
while True:
    if is_prime(i):
        count += 1
        if count == 10001:
            print(i)
            break
    i += 2
