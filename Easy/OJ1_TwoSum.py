"""
Problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

"""
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum_solution_one(nums, target):
    """Solution 1: use 2 loops"""
    m = dict()
    results = list()
    for i in range(0, len(nums)):
        m[nums[i]] = i
    i = 0
    while i < len(nums):
        t = target - nums[i]
        if (t in m.keys()) and m[t] != i:
            result = (i, m[t])
            del nums[m[t]], m[t]
            results.append(result)
            continue
        i += 1
    return results


def two_sum_solution_two(nums, target):
    """Solution 2: use 1 loop"""
    m = dict()
    results = list()
    for i in range(0, len(nums)):
        if (target - nums[i]) in m.keys():
            result = (i, m[target - nums[i]])
            results.append(result)
            continue
        m[nums[i]] = i
    return results


if __name__ == "__main__":
    print(two_sum_solution_two([1, 2, 7, 11, 15, 8], 9))
