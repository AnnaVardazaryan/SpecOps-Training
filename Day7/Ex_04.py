def sort(lst1, lst2):
    print("Array1: ", lst1)
    print("Array2: ", lst2)
    print("==================")
    result = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1

    while j < len(lst2):
        result.append(lst2[j])
        j += 1

    while i < len(lst):
        result.append(lst1[i])
        i += 1

    return result


def devide(lst):
    if len(lst) < 2:
        return lst
    else:
        middle = len(lst) // 2
        array1 = devide(lst[0:middle])
        array2 = devide(lst[middle:])
        return sort(lst1, lst2)


lst = [8, 5, 2, 7, 6, 4, 9, 1, 3]