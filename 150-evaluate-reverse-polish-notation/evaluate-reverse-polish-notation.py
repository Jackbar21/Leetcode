class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                # Must be an integer! (between -200 and 200)
                # assert -200 <= int(token) <= 200
                stack.append(int(token))
                continue

            rNum, lNum = stack.pop(), stack.pop()

            # Handle division case separately, since Python always 
            # rounds DOWN instead of rounding towards 0.
            if token == "/":
                res = lNum // rNum
                if res < 0 and res != lNum / rNum:
                    res += 1
                stack.append(res)
                continue
            
            # Otherwise, straightforward operation!
            stack.append(
                lNum + rNum if token == "+"
                else lNum - rNum if token == "-"
                else lNum * rNum
            )
        
        # assert len(stack) == 1
        return stack[0]
