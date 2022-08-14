def bubble_sort(lst):
    swapped = False
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
                if not swapped:
                    break
    return lst
lst = [1, 2, 3, 6, 8, 1]
print(bubble_sort(lst))