class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # [0,1,2]
        # output = [0,0,1]
        
        i = 0
            
        while i < len(arr):
            if arr[i]==0:
                j = len(arr) - 1
                while j > i:
                    arr[j] = arr[j-1]
                    j -= 1
                i += 1
            i += 1