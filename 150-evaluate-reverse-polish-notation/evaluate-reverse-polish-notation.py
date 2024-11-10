class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack)
            if token not in ["+", "-", "*", "/"]:
                # Must be an integer between -200 and 200!
                assert -200 <= int(token) <= 200
                stack.append(int(token))
                continue

            rNum, lNum = stack.pop(), stack.pop()
            # if lNum >= 0 and rNum < 0:
            #     lNum *= -1
            #     rNum *= -1
            # if token == "/" and lNum < 0:
            #     # Python rounds DOWN instead of towards 0 with division truncation
            #     lNum += 1
            if token == "/":
                # if rNum < 0:
                #     lNum = -lNum
                #     rNum = -rNum

                res = lNum // rNum
                if res < 0 and res != lNum / rNum:
                    res += 1
                # if res < 0:
                #     res += 1
                stack.append(res)
                continue


            stack.append(
                lNum + rNum if token == "+"
                else lNum - rNum if token == "-"
                else lNum * rNum if token == "*"
                else lNum // rNum
            )


            # if token == "+":
                
            #     stack.append(lNum + rNum)
            # elif token == "-":
            #     rNum, lNum = stack.pop(), stack.pop()
            #     stack.append(lNum - rNum)
            # elif token == "*":
            #     rNum, lNum = stack.pop(), stack.pop()
            #     stack.append(lNum * rNum)
            # elif token == "/":
            #     rNum, lNum = stack.pop(), stack.pop()
            #     assert lNum != 0
            #     if lNum < 0:
            #         div = -lNum // rNum
            #         stack.append(-div)
            #     else:
            #         stack.append(lNum // rNum)
                
        
        assert len(stack) == 1
        return stack[0]
