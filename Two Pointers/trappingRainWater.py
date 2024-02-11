def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    pointer1 = 0
    pointer2 = pointer1 + 1
    output = 0
    while (pointer1 != (len(height) - 1)):
        if height[pointer2] >= height[pointer1]: # check for next largest height (must be larger or equal to p1)
            h = min(height[pointer1], height[pointer2])
            w = pointer2 - pointer1 - 1
            blocks_inbetween = 0
            for idx in range(pointer1, pointer2):
                if idx == pointer1 or idx == pointer2:
                    continue
                blocks_inbetween += height[idx]
            v = h * w - blocks_inbetween
            output += v
            pointer1 = pointer2
            pointer2 += 1
        elif pointer2 == (len(height) - 1): # if there are no heights that are larger, find next largest of the remaining blocks
            # print(pointer1, pointer2)
            max_height = 0
            height_index = 0  # Initialize the index of the maximum height
            for idx in range(pointer1 + 1, pointer2 + 1):
                if height[idx] > max_height and idx != pointer1 + 1: # dont want the blocks to be next to each other
                    max_height = height[idx]
                    height_index = idx
            h = max_height
            w = height_index - pointer1 - 1
            blocks_inbetween = 0
            for idx in range(pointer1, height_index):
                if idx == pointer1 or idx == height_index:
                    continue
                elif height[idx] > max_height: # if block next to it is greater than p1, dont count the extra blocks when subtracting (find blocks between)
                    blocks_inbetween += max_height
                else:
                    blocks_inbetween += height[idx]
            v = h * w - blocks_inbetween
            output += v
            pointer1 = pointer2
            pointer2 += 1
        else:
            pointer2 += 1
    print(output)
# height = [0, 1, 0, 2, 1, 0, 1, 3]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height = [4,2,3]
height = [5,4,1,2]
trap(height)