'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in m:
                result.append(i)
                result.append(m[complement])
                return result
            m[nums[i]] = i
