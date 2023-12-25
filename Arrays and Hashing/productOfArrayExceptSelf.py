def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # not O(n) :(, this is O(n^2)
    # result = []
    # counter = 0
    # while (counter < len(nums)):
    #     # make a copy of the list DO NOT do new_lst = nums, it sets referemce to variable
    #     new_lst = nums[:]
    #     del new_lst[counter]

    #     product = 1
    #     for idx in new_lst:
    #         product *= idx
    #     result.append(product)

    #     counter += 1
    # return result 

    # yay works, O(2n) time complexity => O(n)
    postfix = 1 
    prefix = 1
    results = []
    for idx in range(len(nums)):
        results.append(prefix)
        prefix = prefix * nums[idx]
        if len(results) == len(nums):
            break
    
    for idx in range(len(nums)-1, -1, -1):
        results[idx] = results[idx] * postfix
        postfix = postfix * nums[idx]
    print(results)

# can do it via division: multiply list, divide it by current index in nums 

productExceptSelf([-1, 1, 0, -3, 3])