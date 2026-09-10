class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x, n):
            if n == 0:
                return 1
            elif x == 0:
                return 0
            
            result = calculate(x, n // 2)
            result = result * result
            return result if n % 2 == 0 else result * x

        result = calculate(x, abs(n))
        return result if n >= 0 else 1/result
