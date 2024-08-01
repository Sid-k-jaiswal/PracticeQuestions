class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        while num > 0:
            if num & 1 == 0:    # 1 in binary is 00000001
                num = num >> 1  # >> means right shift all the bits by one place
            else:
                num = num-1
            count += 1
        
        return count
    
#         count = 0
        
#         while num != 0:
#             if num%2 == 0:
#                 num = num/2
#             else:
#                 num = num - 1
#             count += 1

#         return count

# 2nd ...

#         if num == 0:
#             return 0
#         if num % 2 == 0:
#             num = 1 + self.numberOfSteps(num/2)
#         else:
#             num = 1 + self.numberOfSteps(num-1)
        
#         return num

# 3rd ...



        