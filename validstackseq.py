'''
946. Validate Stack Sequences
Medium

855

27

Add to List

Share
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
'''

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not len(pushed) :
            return True
        
        top = 0
        i = 0
    
        while len(pushed) and i < len(pushed):
            if pushed[top] != popped[0]:
                top += 1
                i += 1
            else:
                popped.pop(0)
                del pushed[i]
                if top >= 0 and i >= 0:
                    top -= 1
                    i -= 1
            
        if not len(pushed) :
            return True
        
        return False
                
