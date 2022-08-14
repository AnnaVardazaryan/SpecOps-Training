def insertion_sort(lst):
    for i in range(1, len(lst)):
        while lst[i - 1] > lst[i] and i > 0:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
    return lst
print(insertion_sort([3, 5, 2, 16, 0, 1]))
