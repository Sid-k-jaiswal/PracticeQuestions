class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        while num != 0:
            if num%2 == 0:
                num = num/2
                count += 1
            else:
                num = num - 1
                count += 1
        
        return count

# 2nd ...

#         if num == 0:
#             return 0
#         if num % 2 == 0:
#             num = 1 + self.numberOfSteps(num/2)
#         else:
#             num = 1 + self.numberOfSteps(num-1)
        
#         return num

        