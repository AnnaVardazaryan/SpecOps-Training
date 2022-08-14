def findMaxConsecutiveOnes(nums):
    lst = []
    string = ''
    for i in nums:
        if i == 1:
            string += "1"
        if i == 0:
            lst.append(len(string))
            string = ''
    lst.append(len(string))
    return max(lst)
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))