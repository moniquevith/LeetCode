def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()
    for idx, val in enumerate(nums):
        if idx > 0 and val == nums[idx - 1]:
            continue

        target = - val
        pointer1 = idx + 1
        pointer2 = len(nums) - 1
        while (pointer2 > pointer1):
            if (nums[pointer1] + nums[pointer2]) > target:
                pointer2 -= 1
            elif (nums[pointer1] + nums[pointer2]) < target:
                pointer1 += 1
            else:
                results.append([-target, nums[pointer1], nums[pointer2]])
                # break
                pointer1 += 1
                # print(pointer1, pointer2)
                # while (nums[pointer1] == nums[pointer1 - 1] and pointer1 < pointer2):
                #     # print(pointer1, pointer2)
                #     pointer1 += 1
    print(results)
    return results

# nums = [0,0,0,0]
nums = [-1, 0, 1, 2, -1, -4]
threeSum(nums)