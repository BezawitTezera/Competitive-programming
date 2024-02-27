class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = n//2 + n% 2

        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x

            res = pow(x, n//2)
            if n % 2 ==0:
                return (res*res) % (10**9+7)
            else:
                return (x*res*res)  % (10**9+7)
        
        val = (pow(5, even) * pow(4, odd)) % (10**9+7)
        return val