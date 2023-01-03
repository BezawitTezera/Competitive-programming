class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def fibu(i):
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            if i % 3 == 0:
                return "Fizz"
            
            
            if i % 5 == 0:
                return "Buzz"
            else:
                return str(i)
        
        return [fibu(i) for i in range(1,n+1)]
