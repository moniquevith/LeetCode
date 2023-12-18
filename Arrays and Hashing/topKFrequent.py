

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
        counts[n] = []
    
    for n in nums: 
        values[n] = values.get(n, 0) + 1
    
    for key in values:
        curr_value = counts[values[key]] 
        counts[values[key]] = curr_value + [key]

    result = []
    if k == 0:
        return result
    
    counter = 0
    for key in reversed(range(len(nums) + 1)):
        if counts[key] == []:
            continue
        if len(counts[key]) == 1:
            result.append(counts[key][0])
            counter += 1
        else:
            for n in counts[key]:
                if (counter == k):
                    break
                result.append(n)
                counter += 1
        if counter == k: 
            break
    return result
topKFrequent([1,1,1,2,2,3], 2)