def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()
    for n in range(len(nums)):
        target = - nums[n]
        pointer1 = n + 1
        pointer2 = len(nums) - 1
        while (pointer2 > pointer1):
            if (nums[pointer1] + nums[pointer2]) > target:
                pointer2 -= 1
            elif (nums[pointer1] + nums[pointer2]) < target:
                pointer1 += 1
            else:
                results.append([-target, nums[pointer1], nums[pointer2]])
                break
    return results

nums = [-1,0,1,2,-1,-4]
threeSum(nums)