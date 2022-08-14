nums = [5, 6, 7, 7, 8, 8, 10]
target = 7
def binary_search(nums, target):
    lst = []
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[start] == nums[end] == target:
            return [start, end]
        elif nums[mid] < target:
            start = mid + 1
        else:
            if nums[start] != target:
                start += 1
            if nums[end] != target:
                end -= 1
    return [-1, -1]
print(binary_search(nums, target))

