class Solution:
    def robotWithString(self, s: str) -> str:
        # p="", s="ac", t="b"

        # if s is empty, i'm finished
        # if t is empty, I MUST remove letter from s
        # if s[0] <= t[-1], then perform first operation. else, second operation

        suffix_min = collections.deque()
        min_letter = s[-1]
        for letter in s[::-1]:
            min_letter = min(min_letter, letter)
            suffix_min.appendleft(min_letter)

        s = collections.deque((i, letter) for i, letter in enumerate(s))
        t = []
        res = []

        while len(s) > 0:
            # print(f"{s=}, {t=}, {res=}")
            # print(f"p={''.join(res)}, s={''.join(letter for i, letter in s)}, t={''.join(t)}")
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
            # if s[0] <= t[-1]:
            #     t.append(s.popleft())
            # else:
            #     res.append(t.pop())
            
        
        # res += t[::-1]
        while t:
            res.append(t.pop())
        return "".join(res)