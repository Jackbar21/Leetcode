class Solution:
    def fractionAddition(self, expression: str) -> str:
        if len(expression) == 0:
            return "0/1"

        exp = "".join(c if c != "-" else "+-" for c in expression)
        stack = exp.split("+")
        if expression[0] == "-":
            stack = stack[1:]

        assert len(stack) >= 1
        while len(stack) > 1:
            frac1, frac2 = stack.pop(), stack.pop()
            frac = self.addFractions(frac1, frac2)
            stack.append(frac)

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
        # Can reduce fraction here, but numbers will be small enough
        # that we can afford to just recude one time at the end of the summing
        return fraction
    
    def parseFraction(self, frac):
        num, den = frac.split("/")
        num, den = int(num), int(den)
        assert den != 0
        return (num, den)
    
    def reduceFraction(self, frac):
        num, den = self.parseFraction(frac)
        assert den != 0
        if num == 0:
            return f"0/1"
        
        if abs(num) == 1:
            return frac
        
        factor = math.gcd(num, den)
        assert factor != 0

        return f"{num // factor}/{den // factor}"