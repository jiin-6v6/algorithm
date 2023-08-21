class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        if len(word2) <= len(word1):
            for index in range(len(word1)):
                if index >= len(word2):
                    result = result + word1[index:]
                    break
                result = result + word1[index] + word2[index]
        else:
            for index in range(len(word2)):
                if index >= len(word1):
                    result = result + word2[index:]
                    break
                result = result + word1[index] + word2[index]
        return result
