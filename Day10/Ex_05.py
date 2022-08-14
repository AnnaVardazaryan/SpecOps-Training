def missingNumber(nums):
    return int((len(nums) * (len(nums) + 1)) / 2 - sum(nums))
print(missingNumber([3,0,1]))