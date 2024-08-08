class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        queue = []
        
        for i in range(len(arr)):
            queue.append(arr[i])
            
            if arr[i] == 0:
                queue.append(0)
            
            arr[i] = queue.pop(0)
        
#         i = 0
            
#         while i < len(arr):
#             if arr[i]==0:
#                 j = len(arr) - 1
#                 while j > i:
#                     arr[j] = arr[j-1]
#                     j -= 1
#                 i += 1
#             i += 1
    