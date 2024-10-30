class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Input: nums = [0,1,0,3,12]
        # Output: [1,3,12,0,0]
        
#         pointer = 0
        
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[pointer],nums[i] = nums[i],nums[pointer]
#                 pointer += 1
        
        # reducing swaps!
        
        next_zero_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_zero_index] = nums[i]
                next_zero_index += 1
        
        for i in range(next_zero_index,len(nums)):
            nums[i] = 0
        
                
        
        