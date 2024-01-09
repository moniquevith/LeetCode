
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    temp = s.replace(" ", "") # remove spaces 
    new_s = ""
    str_len = 0
    for s in temp:
        if s.isalpha() or s.isnumeric(): # get only letters and numbers
            temp = s.lower() # convert to lowercase
            new_s += temp
            str_len += 1
            
    if new_s == "":
        return True

    pointer_1 = 0
    pointer_2 = str_len - 1
    while (pointer_1 < pointer_2):
        if new_s[pointer_1] == new_s[pointer_2]:
            pointer_1 += 1
            pointer_2 -= 1
        else:
            print("false")
            return False
        
    return True

s = "0P"
isPalindrome(s)