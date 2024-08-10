class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,0,1,1,1,2,2,3,3,4]
        # op:- [0,1,2,3,4]
        
        # [1,1,2] --> [1,2,2]
        
        unique = 0
        
        for i in range(1,len(nums)):
            
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
        
        return unique + 1
            
        
# 2nd ...

#         count = 1
        
#         for i in range(1, len(nums)):
            
#             if nums[i-1] != nums[i]:
#                 nums[count] = nums[i]
#                 count += 1
            
#         print(nums)
        
#         return count