class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(
            filter(lambda x:x.isalnum(), s)
        ).lower()
        return filtered_s == filtered_s[::-1]