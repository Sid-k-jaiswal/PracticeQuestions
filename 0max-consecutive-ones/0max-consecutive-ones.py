class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 and nums[0] == 1:
            return 1
        
        # [1,1,0,1,1,1] --> 3
        # [1,0,1,1,0,1] --> 2
        # [0,0,1,0,1,1] --> 2

            
        count = 0
        maxCount = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                #cache<- 1+
                count += 1
            else:
                #initialize cache -> 0
                count = 0
            
            maxCount = max(count, maxCount)
            
            
        return maxCount
        
            
            