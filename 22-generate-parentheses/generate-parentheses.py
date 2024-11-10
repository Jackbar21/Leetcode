class Solution:
    def __init__(self):
        self.solution = []
    def generateParenthesis(self, n: int) -> List[str]:
        val = self.generateParenthesisHelper(n, n, [])
        return self.solution
    
    def generateParenthesisHelper(self, open_parentheses, closed_parentheses, stack):
        if open_parentheses == 0:
            self.solution.append(
                ''.join(stack) + ')' * closed_parentheses
            )
            return 1

        if open_parentheses >= closed_parentheses:
            assert open_parentheses == closed_parentheses
            stack.append('(')
            return self.generateParenthesisHelper(open_parentheses-1, closed_parentheses, stack)
        
        assert open_parentheses >= 0 and open_parentheses < closed_parentheses
        # Here we have two options:

        # Case 1: add another open parenthese!
        new_stack = stack.copy() + ["("]
        case1 = self.generateParenthesisHelper(open_parentheses-1, closed_parentheses, new_stack)

        # Case 2: add a closed parenthese
        stack.append(')')
        case2 = self.generateParenthesisHelper(open_parentheses, closed_parentheses - 1, stack)

        return case1 + case2