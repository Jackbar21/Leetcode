class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x:x!="", s.split(" ")))[-1])