# Given an integer array nums
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # hashing: 
        # time: O(n)
        # space: O(n)

        # if we used arrays: 
        # time: O(n^2)
        # space: O(1)
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        
        return False