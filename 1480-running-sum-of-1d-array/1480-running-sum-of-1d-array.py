class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        output = []
        for i in range(len(nums)):
            sum = sum+nums[i]
            output.append(sum)
        
        return output

        