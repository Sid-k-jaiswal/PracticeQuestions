class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = [nums[0]]
        for i in range(1,len(nums)):
            sum.append(sum[i-1]+nums[i])
            
        return sum

    # 2nd ...
    
#         sum = [0]*len(nums)
#         sum[0] = nums[0]

#         for i in range(1,len(nums)):
#             sum[i] = sum[i-1]+nums[i]

#         return sum
    
    # 3rd ...
    
#         sum = 0
#         output = []
#         for i in range(len(nums)):
#             sum = sum+nums[i]
#             output.append(sum)
        
#         return output
    