'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
class Solution(object):
    '''
    def trim(self, s):
        ans = []
        for c in s:
            if c != '#':
                ans.append(c)
            elif len(ans):
                ans.pop()
        "".join(ans)
        
        return ans
    '''
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        l1 = len(S)
        l2 = len(T)
        i = l1 - 1
        j = l2 - 1
        
        count1 = 0
        count2 = 0
        while i >= 0 and j >= 0:
            if S[i] == '#':
                count1 += 1 
                continue
            elif count1 > 0:
                count1 -= 1
                
            if T[j] == '#':
                count2 += 1
                continue
            elif count2 > 0:
                count2 -= 1
            
            if count1 > 0 or count2 > 0 :
                continue
            elif S[i] != T[j]:
                return False
                
            i -= 1
            j -= 1
            
        #return self.trim(S) == self.trim(T)
    
       
