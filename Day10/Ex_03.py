def containsDuplicate(nums):
    dic = {}
    for i in nums:
        if dic.get(i):
            return True
        dic[i] = 1
    return False
print(containsDuplicate([1, 2, 3 ,1]))