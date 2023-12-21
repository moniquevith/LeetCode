def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # not O(n) :(
    result = []
    counter = 0
    while (counter < len(nums)):
        # make a copy of the list DO NOT do new_lst = nums, it sets referemce to variable
        new_lst = nums[:]
        del new_lst[counter]

        product = 1
        for idx in new_lst:
            product *= idx
        result.append(product)

        counter += 1
    return result 

# can do it via division: multiply list, divide it by current index in nums 


productExceptSelf([1,2,3,4])