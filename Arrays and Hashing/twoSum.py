
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # using hashmap: 
        # time: O(n)
        # space: O(n)
        # hashmap = {} # value:index
        # for i in range(len(nums)):
        #     if ((target - nums[i]) in hashmap): # check if the difference is in the hashmap
        #         return [hashmap.get((target - nums[i])), i]
        #     hashmap[nums[i]] = i # if it isnt add current value

        # reattempted question
        hashmap = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in hashmap):
                print([ hashmap.get(target - nums[i]), i])
                return [ hashmap.get(target - nums[i]), i]
            hashmap[nums[i]] = i
            
twoSum([2,7,11,15,2], 18) 