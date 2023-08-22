# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        list_str = list(s)

        fromStart = 0
        fromEnd = len(s) - 1
        while fromStart <= fromEnd:
            if s[fromStart] in vowels and s[fromEnd] in vowels:
                list_str[fromStart] = s[fromEnd]
                list_str[fromEnd] = s[fromStart]
                fromStart += 1
                fromEnd -= 1
            elif s[fromStart] in vowels and s[fromEnd] not in vowels:
                fromEnd -= 1
            elif s[fromStart] not in vowels and s[fromEnd] in vowels:
                fromStart += 1
            else:
                fromStart += 1
                fromEnd -= 1

        return ''.join(list_str)

