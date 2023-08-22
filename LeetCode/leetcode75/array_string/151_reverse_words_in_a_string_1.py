# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))