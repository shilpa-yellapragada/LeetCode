'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        inon = 0
        current = 0
        
        if (len(nums) == 1):
            return 
        while inon < len(nums):
            if nums[inon] != 0:
                nums[current] = nums[inon]
                current += 1
            inon += 1

        while current < len(nums):
            nums[current] = 0
            current += 1
