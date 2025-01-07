class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        res = set()
        for i in range(N):
            for j in range(N):
                if i != j and words[i] in words[j]:
                    res.add(words[i])
        return list(res)