lst = [1, 2, 3, 5, 5, 6]
sum_of_uniques = 0
for i in lst:
    if lst.count(i) == 1:
        sum_of_uniques += i
print(sum_of_uniques)