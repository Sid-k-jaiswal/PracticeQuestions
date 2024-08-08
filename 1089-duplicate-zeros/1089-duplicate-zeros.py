class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        # inp-> [0,3,4]
        # op->  [0,0,3]
        
        zeroes = arr.count(0)
        n = len(arr)
        
        l = n-1
        
        while l >= 0:
            
            if l + zeroes < n:
                arr[l + zeroes] = arr[l]
            
            if arr[l] == 0:
                zeroes -= 1
                
                if l + zeroes < n:
                    arr[l + zeroes] = 0
                    
            l -= 1
            

# 2nd ...
#         queue = []
        
#         for i in range(len(arr)):
#             queue.append(arr[i])
            
#             if arr[i] == 0:
#                 queue.append(0)
            
#             arr[i] = queue.pop(0)

# 3rd ...

#         i = 0
            
#         while i < len(arr):
#             if arr[i]==0:
#                 j = len(arr) - 1
#                 while j > i:
#                     arr[j] = arr[j-1]
#                     j -= 1
#                 i += 1
#             i += 1
    