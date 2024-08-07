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


#        int len = nums.length;
        
#         int i = 0, j = len-1, k = len-1;
        
#         int a[] = new int[len];
        
#         while (i <= j)
#         {
#             int s1 = nums[i]*nums[i];
#             int s2 = nums[j]*nums[j];
            
#             if (s1 > s2) {
#                 a[k--] = s1;
#                 i++;
#             }
#             else {
#                 a[k--] = s2;
#                 j--;
#             }
#         }
