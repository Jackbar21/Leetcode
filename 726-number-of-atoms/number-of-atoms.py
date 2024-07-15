from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            N = len(formula)
            i = 0
            
            def parse_element():
                nonlocal i
                start = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1
                return formula[start:i]
            
            def parse_number():
                nonlocal i
                if i == N or not formula[i].isdigit():
                    return 1
                start = i
                while i < N and formula[i].isdigit():
                    i += 1
                return int(formula[start:i])
            
            stack = [defaultdict(int)]
            while i < N:
                if formula[i] == '(':
                    i += 1
                    stack.append(defaultdict(int))
                elif formula[i] == ')':
                    i += 1
                    num = parse_number()
                    top = stack.pop()
                    for elem, v in top.items():
                        stack[-1][elem] += v * num
                else:
                    elem = parse_element()
                    num = parse_number()
                    stack[-1][elem] += num
            
            return stack[0]
        
        count = parse()
        return ''.join(f'{elem}{(count[elem] if count[elem] > 1 else "")}' for elem in sorted(count))
