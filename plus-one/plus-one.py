class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         num = 0
#         length = len(digits)
#         for i in range(length):
#             num += digits[i] * 10**(length-i-1)
        
#         num += 1
        
#         num = str(num)
        
#         result = []
        
#         length = len(num)
        
#         for i in range(length):
#             result.append(int(num[i]))
        
#         print(result)
        
        # return result
        
        
        for i in range(len(digits)-1, -1, -1):
            # If the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digit is not 9, increment it by 1 and return the list
                digits[i] = digits[i] + 1
                return digits
        # If all digits are 9, prepend 1 to the list
        return [1] + digits
            
        
        