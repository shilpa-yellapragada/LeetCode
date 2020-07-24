'''
Given a binary array, find the maximum number of consecutive 1s in this array.
'''
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        m = 0
        for j in range(len(nums)):
            if nums[j] == 1 :
                count += 1
                m = max(m, count)
            else :
                count = 0
        
        return m
