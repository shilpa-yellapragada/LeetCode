'''
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''
class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
    
        odd = 0
        even = 0
        
        while num > 0:
            if num%2 == 1:
                odd += 1
                num -= 1
            else :
                even += 1
                num /= 2
        return odd+even
        
