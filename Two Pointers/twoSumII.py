def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    pointer_1 = 0
    pointer_2 = len(numbers) - 1
    while pointer_1 < pointer_2:
        if ((numbers[pointer_1] + numbers[pointer_2]) > target):
            pointer_2 -= 1
        if ((numbers[pointer_1] + numbers[pointer_2]) < target):
            pointer_1 += 1
        if ((numbers[pointer_1] + numbers[pointer_2]) == target):
            return [pointer_1 + 1, pointer_2 + 1]
        
numbers = [1,2,11,15]
target = 13
twoSum(numbers, target)