class Solution:      
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Idea: from each index, store the length of the LONGEST consecutive & sorted
        # sequence of elements STARTING at that index. Then from that point on, for each
        # index, we check if there is a sorted array of length AT LEAST k (and add its
        # power to answer result if so), or add -1 to answer array since not a power array.

        # Change of plans: Flip idea to store longest consecutive & sorted sequence of elements
        # ENDING at a specific index (instead of starting from!)
        cur_length = 1
        for i in range(k - 2, 0, -1):
            if nums[i - 1] != nums[i] - 1:
                break
            cur_length += 1

        answer = []
        for i in range(k - 1, len(nums)):
            cur_length += 1
            if nums[i - 1] != nums[i] - 1:
                cur_length = 1

            answer.append(nums[i] if cur_length >= k else -1)
        
        return answer
