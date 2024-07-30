class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
#         answer = []
        
#         for i in range(1,n+1):
            
#             # using ternary operator
#             # answer.append("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)) 
            
#             # normal ..
            
#             if i%3 == 0 and i%5 == 0 :
#                 answer.append("FizzBuzz")
#             elif i%3 == 0:
#                 answer.append("Fizz")
#             elif i%5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
    
#         return answer
    
    # 2nd ...
        
        answer = []
        
        for i in range(1,n+1):
            
            string = ""

            if i%3 == 0 :
                string += "Fizz"
            if i%5 == 0 :
                string += "Buzz"
            if string == "" :
                answer.append(str(i))
            else :
                answer.append(string)
                
        return answer