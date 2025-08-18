class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Enumerate all possible orderings of cards A, B, C, D
        # 1. (A,B),(C,D)
        # 2. A,(B,(C,D))
        # 3. A,((B,C),D)
        # 4. (A,(B,C)),D
        # 5. ((A,B),C),D

        # Then for each such case, each ',' represents an operation. Enumerate through every operation.
        operations = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
        error_bounds = pow(10, -5)

        for a, b, c, d in set(permutations(cards)):
            # 1. (A,B),(C,D)
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        try:
                            val = op2(op1(a,b), op3(c,d))
                            if abs(val - 24) < error_bounds:
                                return True
                        except:
                            pass

            # 2. A,(B,(C,D))
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        try:
                            val = op1(a, op2(b, op3(c,d)))
                            if abs(val - 24) < error_bounds:
                                return True
                        except:
                            pass

            # 3. A,((B,C),D)
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        try:
                            val = op1(a, op3(op2(b,c), d))
                            if abs(val - 24) < error_bounds:
                                return True
                        except:
                            pass

            # 4. (A,(B,C)),D
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        try:
                            val = op3(op1(a, op2(b, c)), d)
                            if abs(val - 24) < error_bounds:
                                return True
                        except:
                            pass
            
            # 5. ((A,B),C),D
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        try:
                            val = op3(op2(op1(a, b), c), d)
                            if abs(val - 24) < error_bounds:
                                return True
                        except:
                            pass

        return False
