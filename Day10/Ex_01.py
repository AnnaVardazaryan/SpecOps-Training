def removeDuplicates(nums):
    idx = 1
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == prev:
            continue
        prev = nums[i]
        nums[idx] = nums[i]
        idx += 1
    return idx
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))