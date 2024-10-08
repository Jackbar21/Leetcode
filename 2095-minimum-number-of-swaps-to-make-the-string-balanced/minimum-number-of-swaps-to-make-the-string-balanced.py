class Solution:
    def minSwaps(self, s: str) -> int:

        stack = collections.deque(['dummy'])
        for bracket in s:
            if stack[-1] == "[" and bracket == "]":
                stack.pop()
            else:
                stack.append(bracket)
        stack.popleft()
        print(stack)
        num_swaps = 0
        return math.ceil(len(stack) / 4)

        if len(stack) == 0:
            return 0
        if len(stack) == 2:
            return 1
        return len(stack) // 2 - 1

        queue = collections.deque(s)
        num_swaps = 0
        while len(queue) > 0:
            if queue[0] == "[" and queue[-1] == "]":
                queue.popleft()
                queue.popright()
                continue
            
        # Case 3: string is empty
        return num_swaps


        # '[', add ']' EASY
        # '[', add '[' SWAP RIGHT

        # ']', add '['
        # ']', add ']'

        # [[][][]]
        # ][

            # ']] [[' --> swap 0 with 4
            # '[] []'