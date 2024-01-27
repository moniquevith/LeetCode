def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    hashmap = {}
    for idx in range(len(nums)): # 0 - 5
        target = - nums[idx] # 1
        pointer1 = idx + 1 
        pointer2 = len(nums) - 1
        while (pointer1 < pointer2):
            if (target - nums[pointer1] in hashmap):
                results.append([-target, nums[pointer1], hashmap.get(target - nums[pointer1])])
            hashmap[nums[pointer1]] = nums[pointer1]
            pointer1 += 1

nums = [-1,0,1,2,-1,-4]
threeSum(nums)