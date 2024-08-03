class Solution:
    def convertArrToDict(self, arr):
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        return d
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_dict = self.convertArrToDict(target)
        arr_dict = self.convertArrToDict(arr)
        return target_dict == arr_dict

        # Question: If you can reverse any sub-array of ARR, as many times
        #           as you like, can you reach every possible permutation
        #           of the elements in ARR?

        # P(i):     Given an array of elements of length i, you can reach
        #           every possible permutation of these i elements, given
        #           that you may reverse any non-empty sub-array in the original
        #           array, and repeat this process as many times as desired.
        
        # Base Case: P(0) == True
        #            This is because a zero-element array only has one
        #            permutation anyway, so every permutation has already been 
        #            reached from the getgo!

        # It can easily be shown that P(i) is true for 0 <= i <= 3.
        # I will assume that these are already well-defined base cases

        # WTS: P(i) => P(i + 1) 
        #      [in other words, if P(i) is true, then P(i+1) is true]
        
        # Suppose P(i) is True.
        # WTS: P(i+1)

        """
        # In P(i) there are i! total reachable permutations
        # want to show now for i+1, there are (i+1)! = (i+1) * i! permutations
        # Specifically, for each permutation in P(i), want to show that u can
        # place (i+1)th element in between any two other elements

        # Let [1,2,...,i] be an arbitrary permutation of i elements
        #       (where 1,2,...,i are labels for each element)
        # We now have new element with label '0'
        # Suppose 0 at index k, for some arbitrary 0 <= k < i
        #       i.e. [1,2,...,k-1,0,k,...,i]
        # Then since k >= 0 and k < i, then P(j) for 0 <= k < i is true
        # Therefore, we can use that fact to change this permutation to be:
        #       [0,1,2,...,k-1,k,...,i]
        # This can also easily be shown to be true with following 3 steps:
        #           [1,2,...,k-1,0,k,...,i]
        #       --> [0,k-1,...,2,1,k,...,i]
        #       --> [0,1,2,...,k-1,k,...,i]     
        # Since P(2) is true (from base case), then we must be able to reach:
        #       [1,0,2,...,k-1,k,...,i] 
        # Since P(3) is true (from base case), then we must be able to reach:
        #       [1,2,0,3,...,k,...,i]
        # We repeat this for any j such that 1 <= j < i to reach:
        #       [1,2,...,j-1,0,j,...,i]
        # Again, we can easily show this with following 3-step process:
        #           [0,1,2,...,j-1,j,...,i]
        #       --> [j-1,...,2,1,0,j,...,i]
        #       --> [1,2,...,j-1,0,j,...,i]
        # Until finally we reach:
        #       [1,2,...,i,0]

        # Since original permutation [1,2,...,i] we deemed to be arbitrary,
        # this means that we can fit in this new element (that we labeled 0)
        # into any single permutation of i elements, regardless of where this
        # 0-labeled element happens to be inside a (i+1) total-element array.

        # And again since original permutation was arbitrary, this means we can
        # do this for any single permutation of i elements, meaning we can reach
        # (i+1) new unique arrays (with added 0-labeled element) for any array
        # with i elements, giving us the total of (i+1)*i! == (i+1)! unique
        # permutations that we needed to reach to show that P(i+1) is true,
        # i.e. every permutation of i+1 elements is reachable.

        # Therefore, given P(i) is true, 
        # it must immediately follow that P(i + 1) is also true.

        # QED (Quod Erat Demonstratum)
        """
