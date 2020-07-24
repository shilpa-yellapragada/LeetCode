'''
Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
'''
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        count = 0
        dic = {}
        flag = False
        i, j = 0,0
        
        while i < len(S)-K+1:
            while j < (i+K) and j < len(S):
                if S[j] in dic.keys():
                    break
                else:
                    dic[S[j]] = j
                j += 1
            if len(dic) != K:
                i = dic[S[j]]+1
                j = i
                dic.clear()
            else:
                del dic[S[i]]
                i += 1
                count += 1
                
        return count
