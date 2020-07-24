'''
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        vowels = "aeiou"
        max_vowel_cnt = 0
        vowel_cnt = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_cnt += 1
        
        max_vowel_cnt = vowel_cnt
        for j in range(k,len(s)):
            if vowel_cnt > 0 and s[j-k] in vowels:
                vowel_cnt -= 1
            if s[j] in vowels:
                vowel_cnt += 1
            max_vowel_cnt = max(max_vowel_cnt, vowel_cnt)
        
        return max_vowel_cnt
        
