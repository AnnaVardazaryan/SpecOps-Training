num = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        x = i * j
        if x > num:
            s = str(i * j)
            if s == s[::-1]:
                num = i * j
print(num)