class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # for each index, store:
        #   (1) largest value preceding it
        #   (2) smallest value succeeding it
        #   (3) value at index itself (arr[i])

        i = len(arr) - 1
        while i > 0 and arr[i - 1] <= arr[i]:
            i -= 1
        
        # All indices i and greater, form the beginning of a sorted array.
        # I.e. arr[i:], is a sorted array, requiring us to delete len(arr) - i elements.
        # For each index up to i, can calculate smallest index we can continue sorted
        # "chain" from, and find this such index via binary search. I.e., find smallest
        # index k such that i <= k < len(arr), for every index j < i, such that arr[j] <= arr[k],
        # in which case you know you can create a sorted array by removing k - j + 1 elements!
        
        # We know we only want to continue from a sorted left-half, so apply same principle
        j = 0
        while j < len(arr) - 1 and arr[j] <= arr[j + 1]:
            j += 1
        
        # If j and i cross each other, then array must already be sorted! 
        if j >= i:
            assert j == len(arr) - 1 and i == 0 # Might be false at i == j ?
            return 0
        
        # Remove all but one element
        # if min(arr[:j+1]) > max(arr[i:]):
        #     return len(arr) - 1

        res = len(arr) - 1 # Worst case, delete all but one element
        assert j < i
        # print(arr[i:])
        for index in range(j + 1):
        # # print(i)
        # for index in [1]:
            l, r = i, len(arr) - 1
            k = float("inf")
            while l <= r:
                mid = (l + r) // 2
                if arr[index] <= arr[mid]:
                    # Found a valid index! Search for one even smaller :)
                    k = min(k, mid)
                    r = mid - 1
                else:
                    l = mid + 1
            
            # print(index, k, arr[:index + 1], (arr[k:] if k != float("inf") else []))
            res = min(res, k - index + 1 - 2)

        # Length of left subhalf
        length_left = len(arr[:j+1])
        
        length_right = len(arr[i:])
        # print(f"{i=}")
        return min(
            res,
            # len(arr) - (j+1) + 1, # sorted right-half
            # len(arr) - (i + 1), # sorted left-half
            len(arr) - length_left,
            len(arr) - length_right
        )


        # [2,4,2,3,5]