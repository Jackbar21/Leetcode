class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # For any pair of positive integers X and Y, it is ALWAYS
        # true that the bitwise AND of X and Y, namely (X & Y), is
        # AT MOST the MINIMUM between X and Y. In other words, 
        # (X & Y) <= min(X,Y), which also implies (X & Y) <= X, and (X & Y) <= Y.
        max_num = max(nums)

        # If we pick any number other than num, that will DECREASE the value of the
        # maximum bitwise AND. Henceforth, we must instead find the LARGEST consecutive
        # sequents of elements whose values are all num.
        longest_sequence = 1
        cur_length = 0
        for num in nums:
            cur_length = (cur_length + 1) if num == max_num else 0
            longest_sequence = max(longest_sequence, cur_length)
        
        return longest_sequence
            

