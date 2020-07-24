'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and x != 0):
            # negative number or last digit is 0
            return False
        if x < 10 :
            return True
        
        n = x
        reverse = 0
        
        while n > reverse:
            reverse = reverse*10 + n%10
            n /= 10
            
        if n == reverse or reverse/10 == n:
            return True
        else :
            return False
