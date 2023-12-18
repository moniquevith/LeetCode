
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # time: O(m*n)
    # space: O(n)
    # hashmap = {}

    # for s in strs: 
    #     count = [0] * 26 # a .. z
    #     for c in s: 
    #         count[ord(c) - ord("a")] += 1 # get index for letter and add 1 (count how many times that letter appears)

    #     key = tuple(count) # lists cannot be keys
    #     if key in hashmap:
    #         hashmap[key].append(s) # count: [str, str..]
    #     else:
    #         hashmap[key] = [s]
            
    # return list(hashmap.values())

    # reattempt question
    hashmap = {}
    '''
        {
            eat: ["eat", "tea", "ate"]
        }
    '''
    # same length and same letters 
    for s in strs:
        temp = ''.join(sorted(s))
        if temp in hashmap:
            new_list = hashmap.get(temp) + [s]
            hashmap[temp] = new_list
            continue
        hashmap[temp] = [s]
    
    result = []

    if hashmap == {}:
        result = [[""]]

    for key in hashmap:
        result.append(hashmap.get(key))

    return result

groupAnagrams(["eat","tea","tan","ate","nat","bat"])