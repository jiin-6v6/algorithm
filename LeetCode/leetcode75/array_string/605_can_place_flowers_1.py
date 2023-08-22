# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed) // 2 + 1:
            return False

        if 1 not in flowerbed:
            return n <= (len(flowerbed) + 1) // 2

        canBePlantedCount = 0
        between = 0
        startFlag = True
        for flower in flowerbed:
            if flower == 0:
                between += 1
            else:
                if startFlag:
                    canBePlantedCount += between // 2
                    startFlag = False
                elif between > 0:
                    canBePlantedCount += (between - 1) // 2
                between = 0
        if between > 0:
            canBePlantedCount += between // 2

        return n <= canBePlantedCount
