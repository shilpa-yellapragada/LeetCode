'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        output = []
        if numRows == 0:
            return output
        output.append([1])
        if numRows >= 2 :
            for i in range(1,numRows):
                prevrow = output[i-1]
                prevlen = len(prevrow)
                newrow = []
                newrow.append(1) 

                if prevlen >= 2:
                    for j in range(1,prevlen):
                        newrow.append(prevrow[j] + prevrow[j-1])

                newrow.append(1)
                output.append(newrow)
        return output
