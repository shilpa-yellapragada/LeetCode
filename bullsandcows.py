'''
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.
'''
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
    
        b = 0
        c = 0
        mm = {}
        out = ""
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
                out += 'A'
                continue
            else:
                if secret[i] in mm.keys():
                    mm[secret[i]] += 1
                else:
                    mm[secret[i]] = 1
            out += secret[i]
        
        for i in range(len(guess)):
            if out[i] != 'A' and guess[i] in out and mm[guess[i]] >= 1:
                c += 1
                mm[guess[i]] -= 1
                
                
            
        return str(b) + "A" + str(c) + "B"
