class Solution:
    def robotWithString(self, s: str) -> str:
        # if s is empty, i'm finished
        # if t is empty, I MUST remove letter from s
        # if s[0] <= t[-1], then perform first operation. else, second operation

        suffix_min = []
        min_letter = s[-1]
        for letter in reversed(s):
            if letter < min_letter:
                min_letter = letter
            suffix_min.append(min_letter)
        suffix_min = suffix_min[::-1]

        s = collections.deque((i, letter) for i, letter in enumerate(s))
        t = []
        res = []

        while s:
            i, letter = s.popleft()
            if len(t) == 0:
                t.append(letter)
                continue
            
            # While still something smaller in s
            if suffix_min[i] < t[-1]:
                t.append(letter)
            else:
                res.append(t.pop())
                s.appendleft((i, letter))
        
        return "".join(res) + "".join(t[::-1])