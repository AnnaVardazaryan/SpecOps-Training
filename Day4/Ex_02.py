nums1 = [1, 2, 3, 2, 1]
nums2 = [2, 2]
lst = []
for i in nums1:
    if i in nums2 and not i in lst:
        lst.append(i)
print(lst)

