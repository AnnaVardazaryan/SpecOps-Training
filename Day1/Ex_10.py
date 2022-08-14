def odd_nums(a, b):
    count = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            count += 1
    return count
print(odd_nums(3, 7))
