'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        
        leftsum = 0
        rightsum = total
        
        for i in range(len(nums)):
            rightsum -= nums[i]
            if i >= 1:
                leftsum += nums[i-1]
            if leftsum == rightsum:
                return i
            
        return -1
