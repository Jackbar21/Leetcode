class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        record = 0

        for op in operations:
            if op == '+':
                record = stack[-1] + stack[-2]
            elif op == 'D':
                record = 2 * stack[-1]
            elif op == 'C':
                stack.pop()
            else:
                record = int(op)
            if op != 'C':
                stack.append(record)
        
        return sum(stack)