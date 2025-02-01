class Solution:
    # Time Complexity: O(logn)
    # Input Size: O(logx + logn)
    # This is the VERY FIRST TIME IN MY LIFE that I write a WEAKLY-POLYNOMIAL algorithm!!!
    def myPow(self, x: float, n: int) -> float:
        if n <= 1:
            if n == 1:
                return x
            if n == 0:
                # We're told that either x is not zero or n > 0. So here we can safely return 1,
                # but just in case I wanted to demonstrate that in languages like Java, Math.Pow(0, 0)
                # actually DOESN'T throw an exception, but rather defaults to value 1! The reason for
                # this is probably the fact that lim_{x->0+} (x^x) == 1. Here's a proof of this below:
                """
                PROOF:
                    lim_{x->0+} x^x
                 == lim_{x->0+} (e^ln(x))^x
                 == lim_{x->0+} e^(xln(x))
                 == e^(lim_{x->0+} xln(x))
                 == e^(lim_{x->0+} ln(x)/(1/x))
                 == e^(lim_{x->0+} (1/x) / (-1/x^2)), by L'Hopitals Rule, since
                                                      lim_{x->0+} ln(x) == -INF,
                                                      lim_{x->0+} 1/x == INF
                 == e^(lim_{x->0+} (1/x) * -x^2)
                 == e^(lim_{x->0+} -x)
                 == e^(-0)
                 == e^0
                 == 1
                """
                return 1
            
            # Otherwise, n < 0, so need to make x the reciprocal of itself, and make n positive!
            return self.myPow(1 / x, -n)

        res = self.myPow(x, n // 2)
        res *= res
        if n % 2 == 1:
            res *= x
        return res
