def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_map = {}

    for i in range(len(nums)):
        hash_map[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        print(hash_map[complement])
        if complement in hash_map and hash_map[complement] != i:
            return [i, hash_map[complement]]

print(twoSum([3,3],6))