import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longerStr = ''
        shorterStr = ''
        result = ""

        if len(str1) >= len(str2) :
            longerStr = str1
            shorterStr = str2
        else :
            longerStr = str2
            shorterStr = str1

        stringLengthGcd = math.gcd(len(longerStr), len(shorterStr))
        for i in range(stringLengthGcd, 0, -1) :
            if stringLengthGcd % i == 0 :
                tempStr = shorterStr[:i]
                if shorterStr == tempStr * (len(shorterStr)//i) and longerStr == tempStr * (len(longerStr)//i) :
                    result = tempStr
                    break
        return result
