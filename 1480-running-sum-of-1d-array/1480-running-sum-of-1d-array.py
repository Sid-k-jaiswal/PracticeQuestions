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
            
            
	# def runningSum(self, nums: List[int]) -> List[int]:
	# runSum = [nums[0]] #our answer array starts with nums[0], which is the 0th running sum
	# for i in range(1,len(nums)):
	# 	runSum.append(runSum[i-1]+nums[i]) #the running sum up to index i is the sum of nums[i] and the running sum up to index i-1
	# return runSum
# The key insight here is that the running sum up to index i is the sum of nums[i] and the running sum up to index i-1. Here is a more detailled explanation:
# We know that runningSum[i] = nums[0] + nums[1] + ... + nums[i-1] + nums[i].
# However, runningSum[i-1] = nums[0] + nums[1] + ... + nums[i-1], so we can rewrite the first expression to get that runningSum[i] = runningSum[i-1] + nums[i]!

# This code has a time complexity of O(N) since it only takes one pass, which will make the program run much faster when given a very large nums array. However, there is still a way to optimize the space we use.

#         sum = 0
#         output = []
#         for i in range(len(nums)):
#             sum = sum+nums[i]
#             output.append(sum)
        
#         return output
    