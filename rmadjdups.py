'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

'''
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        top = -1
        for i in range(len(S)):
            if top != -1 and stack[top] == S[i] :
                stack.pop()
                top -= 1
            else:
                stack.append(S[i])
                top += 1
            
            
        output = ""
        for i in range(len(stack)):
            output += stack[i]
        return output
