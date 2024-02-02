def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_volume = 0
    for n in range(len(height)):
        pointer1 = n
        pointer2 = len(height) - 1
        while (pointer1 < pointer2):
            h = min(height[pointer1], height[pointer2])
            w = pointer2 - pointer1
            v = h*w
            if v > max_volume:
                max_volume = v
            pointer2 -= 1
    
    return max_volume

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)