class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return list(word.startswith(pref) for word in words).count(True)