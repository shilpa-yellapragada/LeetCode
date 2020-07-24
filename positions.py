'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.
'''
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) <= 2:
            return []

        j = 0
        output = []
        for i in range(len(S)):
            if i == len(S)-1 or S[i] != S[i+1] :
                if i-j+1 >= 3:
                    output.append([j,i])
                j = i+1
        
        return output
