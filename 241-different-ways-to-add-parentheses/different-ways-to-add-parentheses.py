class Solution:
    def __init__(self):
        # self.op_counts = {op: 0 for op in "+-*"}
        self.seen = set()
        self.strings = set()
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Setup expression as array with entries either being number
        # or operator, to make problem easier. Since expression.length <= 20,
        # this is only constant time :)
        # exp = expression.replace("-", "+-")
        exp = expression
        stack = []
        i = 0
        op_counts = {
            op: 0 for op in "+-*"
        }
        while i < len(exp):
            l = i
            while i < len(exp) and exp[i] not in "+-*":
                i += 1
            # stack.append(int(exp[l:i])) # add number as string
            stack.append((exp[l:i]))
            if i < len(exp):
                op = exp[i]
                stack.append(op)   # add operator
                op_counts[op] += 1
            i += 1

        # Idea: for each operator, consider the case where it goes first. Apply the
        # operator, recursively get all the remaining sub-cases, and consider that
        # as one subset of possible values. Combine all subsets, to get your result.
        print(stack)
        # Stack must be odd in length, since X operators & (X + 1)  
        # numbers ---> 2X + 1 ---> odd number of elements in stack
        assert len(stack) % 2 == 1
        num_operators = len(stack) // 2

        
        # self.d = op_counts
        res = self.allPossibleValues(stack)
        res = set(res)
        print(f"{res=}")
        # print(f"{self.strings=}")
        return [eval(exp) for exp in res]
    
    def getNextUnusedLetter(self, d):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter not in d:
                return letter
        
        raise Exception("Not reachable")

    # Expression is at most 20 in length, and there are 26 letters in alphabet.
    # so can use letters to denote "unknown" value, with mapped values in dictionary,
    # and keep parsing to derive a sort of parenthese-order that we can then add to
    # a set. Once set is fully populated, we evaluate each string and return result.
    def allPossibleValuesNew(self, stack, d = {}):
        assert len(stack) % 2 == 1

        # Operators are at odd indices. For each operator index,
        # consider the case where it is considered for evaluation first,
        # and call method recursively to get remaining combinations.
        res = []
        for i in range(1, len(stack), 2):
            # i-1,i,i+1 --> directly evaluated
            # 0:i-1     --> kept as same
            # i+2:      --> kept as same
            op = stack[i]
            op_counts[op] -= 1
            # old_case = stack[:i-1] + self.allPossibleValues(stack[i-1:i+2]) + stack[i+2:]
            letter = self.getNextUnusedLetter(d)
            d[letter] = f"({stack[i-1:i+2]})"
            # stack[:i-1] + letter + 
            # res.append(old_case)

    def allPossibleValues(self, stack):
        op_counts = {
            op: 0 for op in "+-*"
        }
        for i in range(1, len(stack), 2):
            op_counts[stack[i]] += 1

        assert len(stack) % 2 == 1
        # Base Case #1: Only one operator choice left
        if len(stack) <= 3:
            if len(stack) == 1:
                return [stack[0]]
            else:
                assert len(stack) == 3
                return [f"({''.join(stack)})"]
            # res = stack[0]
            # if len(stack) == 1:
            #     assert False
            #     return res
            
            # if stack[1] == "*":
            #     res *= stack[2]
            # elif stack[1] == "+":
            #     res += stack[2]
            # else:
            #     res -= stack[2]
            
            # return [res]

        # Base Case #2: If have ONLY additions or ONLY multiplications,
        # order DOES NOT MATTER, and should just directly evaluate result
        # if op_counts["-"] <= 0:
        #     assert op_counts["-"] == 0

        #     # Only multiplication symbols
        #     if op_counts["+"] == 0:
        #         base = 1
        #         for i in range(0, len(stack), 2):
        #             base *= stack[i]
        #         return [base]
            
        #     # Only addition symbols
        #     if op_counts["*"] == 0:
        #         return [sum(stack[i] for i in range(0, len(stack), 2))]

        # Operators are at odd indices. For each operator index,
        # consider the case where it is considered for evaluation first,
        # and call method recursively to get remaining combinations.
        res = []
        for i in range(1, len(stack), 2):
            # i-1,i,i+1 --> directly evaluated
            # 0:i-1     --> kept as same
            # i+2:      --> kept as same
            op = stack[i]
            op_counts[op] -= 1
            old_case = stack[:i-1] + self.allPossibleValues(stack[i-1:i+2]) + stack[i+2:]
            # res.append(old_case)
            str1 = ''.join(str(i) for i in stack[:i-1])
            str2 = f"({''.join(str(i) for i in stack[i-1:i+2])})"
            str3 = ''.join(str(i) for i in stack[i+2:])
            corresponding_string = ''.join([str1, str2, str3])
            self.strings.add(corresponding_string)
        # return res
            # tuple_case = tuple(old_case)
            # if tuple_case in self.seen:
            #     continue
            # else:
            #     self.seen.add(tuple_case)
            

            case = self.allPossibleValues(old_case)
            # print(f"{old_case=}, {case=}, {op_counts=}")
            # seen = set("+*-")
            # for num in case:
            #     if num not in seen:
            #         res.append(num)
            #     seen.add(num)
            # if len(case) == 1:
            #     assert case[0] not in ['*', '-', '+']
            #     res.extend(case[0])
            res.extend(case)
        
        # print(f"Mapped res: {list(map(self.allPossibleValues, res))}")
        return res
        
    def computeExpression(self, expression, ordering):
        1-1-1-1-1-1-1-1-1-1-1-1-1-1-1

# 2*3-4*5

# [14, '*', 5]

# [2, '*', 3, '-', 4, '*', 5]
# --> ["(2*3)", '-', 4, '*', 5]
# --> ["((2*3)-4)", '*', 5]
