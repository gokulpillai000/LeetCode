class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[left] == 0:
                nums[left], nums[i] = nums[i], nums[left]

            # wait while we find a non-zero element to
            # swap with you
            if nums[left] != 0:
                left += 1


        

        
        