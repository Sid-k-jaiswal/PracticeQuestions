class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
    
        return count
    
# 2nd ...
#         output = 0
        
#         for i in nums:
            
#             count = 0
            
#             while i > 0:
#                 i = i/10
#                 count += 1
            
#             if count % 2 == 0:
#                 output += 1
                
#         return output