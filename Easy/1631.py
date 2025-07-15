class Solution:
    def isValid(self, word: str) -> bool:
        cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        vowel = set("AEIOUaeiou")
        num = set("0123456789")
        sym = set("@#$")

        co = 0
        v = 0
        n = 0

        if len(word) < 3 :
            return False
        for c in word:
            if c in sym:
                return False 
            if c in cons:
                co += 1
            if c in vowel:
                v += 1
            if c in num:
                n += 1

        
        return True if( co and v ) else False 



s = Solution()
w = input("Enter the string : ")
print(s.isValid(w))