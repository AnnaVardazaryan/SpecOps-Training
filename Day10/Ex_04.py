def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor
print(singleNumber([2,2,1]))