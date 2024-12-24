class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        partitions = []
        def backtrack(i):
            # Base Case: If i >= len(s), then we want to check if every partition
            # is a palindrome!
            if i >= len(s):
                strings = ["".join(partition) for partition in partitions]
                if all(isPalindrome(string) for string in strings):
                    yield strings
                return

            letter = s[i]

            # Case 1: add letter at index i into last partition
            # (Can only do this if I have at least one partition in the first place!)
            if len(partitions) > 0:
                partitions[-1].append(letter)
                yield from backtrack(i + 1)
                partitions[-1].pop()

            # Case 2: add letter at index i into new partition
            partitions.append([letter])
            yield from backtrack(i + 1)
            partitions.pop()
        
        return list(backtrack(0))