'''
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 
Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
'''

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        left = 0 
        ans = 0
        zeros = 0
        if len(A) < K:
            return 0
        
        for i in range(len(A)):
            if (A[i] == 0):
                zeros += 1
            while(left <= i and zeros > K):
                if A[left] == 0 :
                    zeros -= 1
                left += 1
                
            ans = max(ans,i - left + 1)
        
        return ans
