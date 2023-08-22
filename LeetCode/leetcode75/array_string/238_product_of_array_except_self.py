# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        only_zero = [zero for zero in nums if zero == 0]
        non_zero = [num for num in nums if num != 0]
        if len(only_zero) > 1 :
            return [0] * len(nums)
        elif len(only_zero) == 1:
            result2 = []
            product2 = 1
            for num in non_zero :
                product2 *= num
            for num in nums :
                if num != 0 :
                    result2.append(0)
                else :
                    result2.append(product2)
            return result2
        else :
            result3 = []
            product3 = 1
            for num in nums :
                product3 *= num
            for num in nums :
                result3.append(product3//num)
            return result3
