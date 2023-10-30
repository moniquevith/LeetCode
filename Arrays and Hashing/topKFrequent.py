

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    hashmap = {}

    for n in nums: 
        hashmap[n] = 1 + hashmap.get(n, 0)

    # get k most frequent 
    # for i in range(len(nums)):
    #     hashmap[i] = 
topKFrequent([1,1,8,1,2,2,3], 2)