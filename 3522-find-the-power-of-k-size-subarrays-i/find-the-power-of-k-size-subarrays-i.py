class Solution:      
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Base Case: k == 1 (each number represents power of its own length-1 array!)
        if k == 1:
            return nums

        # Idea: from each index, store the length of the LONGEST consecutive & sorted
        # sequence of elements STARTING at that index. Then from that point on, for each
        # index, we check if there is a sorted array of length AT LEAST k (and add its
        # power to answer result if so), or add -1 to answer array since not a power array.

        # Change of plans: Make array that stores index of where current longest chain started
        
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

        return 