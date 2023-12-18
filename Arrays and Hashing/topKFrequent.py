

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # count len(nums)
    """
        1st
        {
            0:0
            1:3
            2:2
            3:1
            4:0
            5:0
            6:0
        }

        2nd
        {
            1: 3
            2: 2
            3: 1
        }

        go through the values in 2nd dict and add the key to respective 1st dict 

        go through 1st dict backwards and values 
    """
    counts = {}
    values = {}

    for n in range(len(nums) + 1):
        counts[n] = 0
    
    for n in nums: 
        values[n] = values.get(n, 0) + 1
    
    for key in values:
        counts[values[key]] = key
    
    counter = 0
    result = []
    if k == 0:
        return result
    
    for key in reversed(range(len(nums) + 1)):
        if counter == k:
            break
        if counts[key] == 0:
            continue
        else:
            result.append(counts[key])
        counter += 1
    return result
topKFrequent([1,1,8,1,2,2], 2)