def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    pointer_1 = 0
    pointer_2 = pointer_1 + 1
    while pointer_1 != len(numbers):
        for idx in range(pointer_2, len(numbers), 1):
            if (numbers[pointer_1] + numbers[idx] == target):
                return [pointer_1 + 1, idx + 1]
        pointer_1 += 1
        pointer_2 += 1

numbers = [1,2,11,15]
target = 13
twoSum(numbers, target)