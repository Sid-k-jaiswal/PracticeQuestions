class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # [3,2,2,3] , val = 3
        
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        
        print(nums)
        
        return i

        