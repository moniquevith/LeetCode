# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)): 
            return False 
        
        # count occurance of each character in string S and T 
        countS, countT = {}, {}

        # time: O(s+t) = O(n)
        # space: O(s+t) = O(n)
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # if this key doesnt exist in hashmap, return 0 (will be 1 anyways cos we added 1)
            countT[t[i]] = 1 + countT.get(t[i], 0) 

        # get each letter in countS
        for c in countS: 
            # if the count of that letter not equal to count in countT return false 
            if countS[c] != countT.get(c,0): # if key doesnt exist in countT 
                return False
        
        return True 

        # solution that doesnt take memory? 
        # use sort both strings and if strings match return true else false 
        # time: O(nlogn)
  

isAnagram("anagram", "nagaram")