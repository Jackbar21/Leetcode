# Definition for singly-linked list.
class ListNode:
    def __init__(self, val="", nxt=None):
        self.val = val
        self.next = nxt

class Solution:
    # Linked List to list/array
    def ll_to_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Setup expression as array with entries either being number
        # or operator, to make problem easier. Since expression.length <= 20,
        # this is only constant time :)
        head = ListNode(-1)
        cur = head
        i = 0
        while i < len(expression):
            l = i
            while i < len(expression) and expression[i] not in "+-*":
                i += 1

            cur.next = ListNode(expression[l:i]) # add number as string
            cur = cur.next
            if i < len(expression):
                cur.next = ListNode(expression[i])   # add operator
                cur = cur.next
            i += 1
        
        # print(ll_to_list(head.next))
        # return []

        # Idea: for each operator, consider the case where it goes first. Apply the
        # operator, recursively get all the remaining sub-cases, and consider that
        # as one subset of possible values. Combine all subsets, to get your result.
        stack = self.ll_to_list(head.next)
        results_as_strings = self.allPossibleValues(stack)
        # results_as_strings = self.allPossibleValues(head.next)
        results_as_values = map(eval, results_as_strings)
        return results_as_values

    def allPossibleValues(self, stack):
        # Stack must be odd in length, since X operators & (X + 1)  
        # numbers ---> 2X + 1 ---> odd number of elements in stac
        assert len(stack) % 2 == 1

        # Base Case #1: Only one operator choice left
        if len(stack) <= 3:
            if len(stack) == 1:
                return [stack[0]]
            assert len(stack) == 3
            return [f"({''.join(stack)})"]

        # Operators are at odd indices. For each operator index,
        # consider the case where it is considered for evaluation first,
        # and call method recursively to get remaining combinations.
        res = set()
        for i in range(1, len(stack), 2):
            # i-1,i,i+1 --> directly evaluated
            # 0:i-1     --> kept as same
            # i+2:      --> kept as same
            cases = stack[:i-1] + self.allPossibleValues(stack[i-1:i+2]) + stack[i+2:]
            cases = self.allPossibleValues(cases)
            
            for case in cases:
                res.add(case)
        
        return res
        