lst = [1, 2, 3, 4, 5, 4]
lst_evens = []
for i in lst:
    if i % 2 == 0:
        lst_evens.append(i)
        lst.remove(i)
print(lst_evens + lst)