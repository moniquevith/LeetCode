def solution(a, k):
    remainder_freq = {}
    num_of_pairs = 0
    
    # Count the frequency of remainders
    for num in a:
        remainder = num % k
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
    
    # Calculate pairs
    for num in a:
        remainder = num % k
        complement = (k - remainder) % k
        if complement in remainder_freq:
            if complement == remainder:
                num_of_pairs += max(remainder_freq[complement] - 1, 0)
            else:
                num_of_pairs += remainder_freq[complement]
    
    return num_of_pairs // 2  # Divide by 2 to avoid counting pairs twice

result = solution([1, 2, 3, 4, 5], 3)
print("Number of pairs divisible by k:", result)
