class Solution:
    def fractionAddition(self, expression: str) -> str:
        if len(expression) == 0:
            return "0/1"
        # a/b + x/y
        # ay/by + bx/by
        # (ay + bx) / by
        # 4 / 6 --> 2 / 3

        # "1/3-1/2" --> "1/3+-1/2"

        exp = "".join(c if c != "-" else "+-" for c in expression)
        stack = exp.split("+")
        if expression[0] == "-":
            stack = stack[1:]
        
        assert len(stack) >= 1
        print(stack)
        while len(stack) > 1:
            frac1, frac2 = stack.pop(), stack.pop()
            frac = self.addFractions(frac1, frac2)
            stack.append(frac)
            print(stack)

        return self.reduceFraction(stack[0])
    
    def addFractions(self, frac1, frac2):
        # frac1 == a/b
        # frac2 == x/y
        # frac1 + frac2 == a/b + x/y == ay/by + bx/by == (ay + bx) / by
        a, b = self.parseFraction(frac1)
        x, y = self.parseFraction(frac2)

        if b == y:
            num = a + x
            return f"{num}/{b}"
        
        num = (a * y) + (b * x)
        den = b * y

        fraction = f"{num}/{den}"
        return self.reduceFraction(fraction)
    
    def parseFraction(self, frac):
        numerator, denominator = frac.split("/")
        numerator, denominator = int(numerator), int(denominator)

        assert denominator != 0
        print(f"parseFraction: {frac} == {numerator}, {denominator}")
        return (numerator, denominator)


    
    def reduceFraction(self, frac):
        # return frac
        
        num, den = self.parseFraction(frac)
        print(f"{num=}, {den=}")
        assert den != 0
        if num == 0:
            return f"0/1"
        
        if abs(num) == 1:
            return frac
        
        factor = math.gcd(num, den)
        assert factor != 0
        print(factor, num, den)

        return f"{num // factor}/{den // factor}"