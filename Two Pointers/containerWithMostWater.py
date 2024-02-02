def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_volume = 0
    pointer1 = 0
    pointer2 = len(height) - 1
    while (pointer1 < pointer2):
        h = min(height[pointer1], height[pointer2])
        w = pointer2 - pointer1
        v = h * w
        max_volume = max(max_volume, v)
        if height[pointer1] < height[pointer2]:
            pointer1 += 1
        else:
            pointer2 -= 1
    
    return max_volume

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)