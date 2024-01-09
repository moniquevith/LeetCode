
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hashset = set(nums)
    longest_sequence = 0
    for n in nums: 
        # check if n is the start of a sequence
        if (n - 1) not in hashset:
            length = 0
            while (n + length) in hashset:
                length += 1
            longest_sequence = max(length, longest_sequence)
    return longest_sequence
        
nums = [0,3,7,2,5,8,4,6,0,1]
longestConsecutive(nums)