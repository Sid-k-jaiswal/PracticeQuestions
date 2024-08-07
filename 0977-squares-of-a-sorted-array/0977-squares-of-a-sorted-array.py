class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []
        
        for i in range(len(nums)):
            squares.append(nums[i]*nums[i])
        
        squares.sort()
    
        return squares