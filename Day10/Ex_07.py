def arrayPairSum(nums):
    nums.sort()
    return sum([nums[i] for i in range(0, len(nums), 2)])
print(arrayPairSum([1,4,3,2]))