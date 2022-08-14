lst = [1, 2, 3, 4, 4, 3, 4, 7]
dic = {}
for i in lst:
    dic[i] = lst.count(i)
print(dic)
