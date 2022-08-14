def primeFactors(n):
    c = 2
    lst = []
    while n > 1:
        if n % c == 0:
            n /= c
            lst.append(c)
        else:
            c = c + 1
    return lst

def prime(num):
    prod = 1
    dic = {}
    while num:
        for i in primeFactors(num):
            dic[i] = max(primeFactors(num).count(i), dic.get(i, 0))
        num -= 1
    for i in dic.keys():
        prod  *= (int(i)**dic[i])
    return prod
print(prime(20))