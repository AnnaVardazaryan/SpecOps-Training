target = [1, 3]
n = 3
lst = []
for i in range(1, n + 1):
    if i > target[-1]:
        break
    if i in target:
        lst.append("push")
    else:
        lst.append("push")
        lst.append("pop")
print(lst)








