'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sl = []

        for i in range(len(s)):
            if s[i] not in sl and (s.count(s[i]) == 1):
                return i
            sl.append(s[i])
        return -1
