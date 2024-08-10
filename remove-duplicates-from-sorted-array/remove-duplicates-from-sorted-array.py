class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,0,1,1,1,2,2,3,3,4]
        # op:- [0,1,2,3,4]
        
        # [1,1,2]
        
        count = 1
        
        for i in range(1, len(nums)):
            
            if nums[i-1] != nums[i]:
                nums[count] = nums[i]
                count += 1
            
        print(nums)
        
        return count