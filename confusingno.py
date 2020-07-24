'''
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
'''
class Solution:        
    def confusingNumber(self, N: int) -> bool:
        pair = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        
        rnum = 0
        before = N
        
        while N != 0:
            num = N % 10
            print(num)
            if num not in pair.keys():
                print("returning false")
                return False
            rnum = rnum*10 + pair[num]
            N = N//10
            
        # flip all nums with their pair
        if before == rnum:
            return False
        
        return True
