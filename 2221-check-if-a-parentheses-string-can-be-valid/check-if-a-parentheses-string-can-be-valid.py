class Solution:

    @cache
    def dp(self, i):
        if i >= len(self.s):
            return True


    def canBeValid(self, s: str, locked: str) -> bool:
        # self.s, self.locked = s, locked
        # return self.dp(0)
        INDEX, PARENTHESE = 0, 1

        # Hint 1
        if len(s) % 2 == 1:
            return False
        
        # locked_open = 0
        # flexible = 0
        locked_open = collections.deque()
        flexible = collections.deque()

        # Hint 2 -- Pass through to find all locked ')', and in doing so have number
        # of locked-open or free indices (flexible) to the left of it
        for index, parenthese in enumerate(s):
            if locked[index] == "0":
                # flexible += 1
                flexible.append(index)
                continue
            
            if parenthese == "(":
                # locked_open += 1
                locked_open.append(index)
                continue
            
            assert parenthese == ")"
            # if locked_open > 0:
            if len(locked_open) > 0:
                # For locked opens, we'll need to match them with something
                # on the right. So ideally, we want to match with leftmost locked-open we have!
                # So, get rid of locked-open parentheses from the RIGHT
                # locked_open -= 1
                locked_open.pop()
            # elif flexible > 0:
            elif len(flexible) > 0:
                # flexible -= 1
                # TODO: might need to do flexible.pop() instead?
                flexible.popleft()
            else:
                # Cannot balance this locked closed-parenthese!
                return False 
        
        # Hint 3 -- Now, we've been able to clear ALL locked closed-parentheses,
        # choosing to do so via 
        while len(locked_open) > 0:
            locked_open_index = locked_open.pop()
            if len(flexible) == 0:
                return False
            flexible_index = flexible.pop()

            if not (locked_open_index < flexible_index):
                return False
        
        return True


        # need = collections.deque()
        # for index, parenthese in s:
        #     if locked[index] == "0":
        #         continue
            
            # other_parenthese = ")" if parenthese == "(" else "("
            # need.append((index, other_parenthese))
        
        # flexible_open = 0
        # flexible_closed = 0

        # prefix_open = [] # prefix_open[i] == # of non-locked closed parenthese in s[0..i]
        # count = 0
        # for digit in locked:
        #     count += digit == "0"
        #     prefix_closed.append(count)



        # for index, parenthese in s:
        #     if locked[index] == "1":
        #         assert need[0][INDEX] == index
        #         need_index, need_parenthese = need.popleft()
        #         if need_parenthese == ")":
        #             if flexible_open == 0:
        #                 return False
        #             flexible_open -= 1
        #         else:
        #             if flexible_closed == 0:
        #                 return False
                    
                



        INDEX, PARENTHESE = 0, 1
        stack = collections.deque()
        for index, parenthese in enumerate(s):
            # #print(f"{stack=}")
            # Four possible cases:
            # (1) stack[-1] == '(', parenthese == ')' --> pop from stack
            # (2) stack[-1] == '(', parenthese == '(' --> 
            # (3) stack[-1] == ')', parenthese == ')' --> 
            # (4) stack[-1] == ')', parenthese == '(' --> 
            if len(stack) == 0:
                stack.append((index, parenthese))
                continue
            
            # if index == 41:
                #print("ALERT START")
                #print(f"{stack=}")
                #print(f"{prev_parenthese=}, {prev_index=}, {locked[prev_index]=}")
                #print(f"{parenthese=}, {index=}, {locked[index]=}")
                #print("ALERT END")

            # Check if can eliminate prev_parenthese and cur_parenthese, accounting for
            # locked allowing us to change parentheses in real time!
            prev_index, prev_parenthese = stack[-1]
            if (locked[prev_index] == "0" == locked[index]):
                stack.append((index, parenthese))
                continue
    
            if (
                # (locked[prev_index] == "0" == locked[index]) or
                (locked[prev_index] == "0" and parenthese == ")") or
                (prev_parenthese == "(" and locked[index] == "0") or
                (prev_parenthese == "(" and parenthese == ")")
            ):
                stack.pop()
            else:
                # Otherwise, I cannot match these two parentheses, so append to stack
                stack.append((index, parenthese))


            # if parenthese == ")" and len(stack) > 0 and stack[-1][PARENTHESE] == "(":
            #     stack.pop()
            # elif len(stack) > 0 and locked[stack[-1][INDEX]] == 0 == locked[i]:
            #     stack.pop()
            # else:
            #     stack.append((i, parenthese))
        

        # We need to keep popping pairs of parenthese from the stack. We can do so
        # while len(stack) >= 2:
        #     right, left = stack.pop(), stack.pop()
            # Want left to be open parenthese, and right to be closed parenthese!
        print(f"{locked=}")
        print(f"{stack=}")
        print(f"{[locked[s[INDEX]] for s in stack]}")

        return len(stack) % 2 == 0

        # For each element in the stack that is locked, need to see if it's unlockable
        # for index, parenthese in stack:
        #     if locked[index] == 0:
        #         continue
            
            # if parenthese == "(":
                # We need the right parenthese to

        # Handle closed parentheses (left-side)
        flexible_left = 0
        need_right = 0
        while len(stack) > 0 and stack[0][PARENTHESE] == ")":
            index, parenthese = stack.popleft()
            if locked[index] == "0":
                flexible_left += 1
                continue
            
            assert parenthese == ")"
            if flexible_left == 0:
                # return False
                need_right += 1
                continue
            
            # Match parentheses!
            flexible_left -= 1
        
        print(f"{locked=}")
        print(f"{stack=}")
        print(f"{[locked[s[INDEX]] for s in stack]}")

        # Handle open parentheses (right-side)
        flexible_right = 0
        need_left = 0
        while len(stack) > 0 and stack[-1][PARENTHESE] == "(":
            index, parenthese = stack.pop()
            if locked[index] == "0":
                flexible_right += 1
                continue
            
            assert parenthese == "("
            if flexible_right == 0:
                # return False
                need_left += 1
                continue

            
            # Match parentheses!
            flexible_right -= 1
        
        if need_right > flexible_right or need_left > flexible_left:
            return False
        
        flexible_right -= need_right
        flexible_left -= need_left

        print(f"{locked=}")
        print(f"{stack=}")
        print(f"{[locked[s[INDEX]] for s in stack]}")
        # assert len(stack) == 0
        print(f"{flexible_left, flexible_right=}")
        return (flexible_left + flexible_right) % 2 == 0
        

        # Now left with all remaining un-fixed parentheses... must ALL be unlockable
        print(f"RES: {stack=}, {[locked[index] for index, _ in stack]}")
        return all([locked[index] == "0" for index, _ in stack])


        # assert 0 <= len(stack) <= 1
        return len(stack) == 0
        