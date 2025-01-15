def not_zero(a):
    return 1 if a == 0 else a

class Solution:
    def productExceptSelf(self, nums):
        left_prod = 1
        right_prod = 1

        n = len(nums)
        answ = [1] * n

        for i in range(n):
            answ[i] = left_prod
            left_prod *= nums[i]

        for i in range(n-1, -1,-1):
            answ[i] *= right_prod
            right_prod *= nums[i]
        
        return answ