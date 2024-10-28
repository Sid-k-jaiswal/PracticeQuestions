class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)
        for i in range(length):
            num += digits[i] * 10**(length-i-1)
        
        num += 1
        
        num = str(num)
        
        result = []
        
        length = len(num)
        
        for i in range(length):
            result.append(int(num[i]))
        
        print(result)
        
        return result
        
            
        
        