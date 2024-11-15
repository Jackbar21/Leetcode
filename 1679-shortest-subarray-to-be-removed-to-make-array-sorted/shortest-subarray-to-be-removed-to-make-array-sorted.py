class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = len(arr) - 1
        while i > 0 and arr[i - 1] <= arr[i]:
            i -= 1
        
        # All indices i and greater, form the beginning of a sorted array.
        # I.e. arr[i:], is a sorted array, requiring us to delete len(arr) - i elements.
        # For each index up to i, can calculate smallest index we can continue sorted
        # "chain" from, and find this such index via binary search. I.e., find smallest
        # index k such that i <= k < len(arr), for every index j < i, such that arr[j] <= arr[k],
        # in which case you know you can create a sorted array by removing k - j + 1 elements!
        
        # We know we only want to continue from a sorted left-half, so apply same principle!
        j = 0
        while j < len(arr) - 1 and arr[j] <= arr[j + 1]:
            j += 1
        
        # If j and i cross each other, then array must already be sorted! 
        if j >= i:
            # assert j == len(arr) - 1 and i == 0
            return 0
        
        # Case 1: Check if removing all elements except left sorted part yields better results
        length_left = j + 1
        # Case 2: Check if removing all elements except right sorted part yields better results
        length_right = len(arr) - i
        # Initialze res to better of these two cases!
        res = len(arr) - max(length_left, length_right)

        for index in range(j + 1):
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
            
            res = min(res, k - index - 1) # (k-index+1) - 2 since don't wanna include ends!

        return res
        