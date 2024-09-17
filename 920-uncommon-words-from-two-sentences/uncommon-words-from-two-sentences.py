class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(" "), s2.split(" ")
        d1, d2 = {}, {}
        res = []

        for word in s1:
            d1[word] = d1.get(word, 0) + 1
        
        for word in s2:
            d2[word] = d2.get(word, 0) + 1

        for word in s1:
            if d1[word] == 1 and word not in d2:
                res.append(word)
        
        for word in s2:
            if d2[word] == 1 and word not in d1:
                res.append(word)
        
        return res
