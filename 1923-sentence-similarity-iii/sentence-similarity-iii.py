class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        
        if len(s1) == len(s2):
            return s1 == s2
        
        small, big = s1, s2
        if len(s1) > len(s2):
            small, big = s2, s1
        
        small, big = collections.deque(small), collections.deque(big)
        while len(small) > 0 and (small[0] == big[0] or small[-1] == big[-1]):
            if small[0] == big[0]:
                small.popleft()
                big.popleft()
            
            if len(small) > 0 and small[-1] == big[-1]:
                small.pop()
                big.pop()
        
        return len(small) == 0
