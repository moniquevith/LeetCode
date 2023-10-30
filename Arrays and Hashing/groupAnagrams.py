
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # time: O(m*n)
    # space: O(n)
    hashmap = {}

    for s in strs: 
        count = [0] * 26 # a .. z
        for c in s: 
            count[ord(c) - ord("a")] += 1 # get index for letter and add 1 (count how many times that letter appears)

        key = tuple(count) # lists cannot be keys
        if key in hashmap:
            hashmap[key].append(s) # count: [str, str..]
        else:
            hashmap[key] = [s]
            
    return list(hashmap.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"])