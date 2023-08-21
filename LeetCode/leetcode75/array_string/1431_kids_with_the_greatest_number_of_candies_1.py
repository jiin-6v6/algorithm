class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyFlagCount = 0
        for candy in candies:
            if candy > candyFlagCount:
                candyFlagCount = candy
        candyFlagCount -= extraCandies

        result = []
        for candy in candies:
            result.append(candy >= candyFlagCount)
        return result