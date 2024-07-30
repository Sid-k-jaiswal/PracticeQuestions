class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
# # python ternary operator
# min = "a is minimum" if a < b else "b is minimum"

        answer = []
        
        for i in range(1,n+1):
            
            answer.append("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i))

            # if i%3 == 0 and i%5 == 0 :
            #     answer.append("FizzBuzz")
            # elif i%3 == 0:
            #     answer.append("Fizz")
            # elif i%5 == 0:
            #     answer.append("Buzz")
            # else:
            #     answer.append(str(i))
    
        return answer