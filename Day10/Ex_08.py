def primeFactors(num):
    c = 2
    while num > 1:
        if num % c == 0:
            num /= c
        else:
            c = c + 1
    return c
num = 600851475143
print(primeFactors(num))
