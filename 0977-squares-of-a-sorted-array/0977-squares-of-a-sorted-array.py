class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        first = 0
        last = lastPointer = len(nums) - 1
        
        output = [0]*len(nums)
        
        while first <= last :
            
            firstSquare = nums[first]*nums[first]
            lastSquare = nums[last]*nums[last]
            
            if firstSquare > lastSquare:
                output[lastPointer] = firstSquare
                
                lastPointer -= 1
                first += 1
            else:
                output[lastPointer] = lastSquare
                lastPointer -= 1
                last -= 1
        
        return output
        
        
        
#         squares = []
        
#         for i in range(len(nums)):
#             squares.append(nums[i]*nums[i])
        
#         squares.sort()
    
#         return squares