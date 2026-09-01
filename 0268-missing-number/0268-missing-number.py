class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        actualSum = n*(n+1)//2
        return actualSum-total