class Solution:
    def robotWithString(self, s: str) -> str:
        suffix_min = [] # suffix_min[i] == min(s[i:])
        min_letter = s[-1]
        for letter in reversed(s):
            if letter < min_letter:
                min_letter = letter
            suffix_min.append(min_letter)
        suffix_min = suffix_min[::-1]

        queue = collections.deque(enumerate(s))
        t = []
        res = []

        while queue:
            i, letter = queue.popleft()
            if len(t) == 0:
                t.append(letter)
                continue
            
            # While still something smaller in s
            if suffix_min[i] < t[-1]:
                t.append(letter)
            else:
                res.append(t.pop())
                queue.appendleft((i, letter))
        
        return "".join(res) + "".join(t[::-1])

# 1. Pop START of s, and push to END of t
# 2. Pop from END of t, push to END of res