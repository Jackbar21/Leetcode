class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Idea: Let N = len(nums). Then, there are N * (N - 1) / 2 total possible pairs. Since there are
        # likely much fewer good pairs than there are bad, given we know there are k good pairs, the number
        # of bad pairs is simply (N * (N - 1) / 2) - K.
        # A pair of indices (i, j) is a GOOD PAIR if i >= j or j - i == nums[j] - nums[i]
        # <==> j + nums[i] != i + nums[j]
        # <==> nums[i] - i != nums[j] - j
        # Hence for every single index i, we can map it to the value nums[i] - i, to use it for
        # comparison with other indices in nums! Then if two indices map to the same value, we know
        # those indices form ONE GOOD PAIR! Hence, we can add the frequency of each of these "values"
        # to a hash map, then counting number of total good pairs, subtracting that from the total
        # number of pairs in general, to finally obtain the number of BAD pairs.
        N = len(nums)
        d = {}
        for i, num in enumerate(nums):
            d[num - i] = d.get(num - i, 0) + 1

        good_pairs = functools.reduce(lambda acc, k: acc + k * (k - 1) // 2, d.values(), 0)
        total_pairs = N * (N - 1) // 2
        bad_pairs = total_pairs - good_pairs
        return bad_pairs

        # Given a non-negative integer N >= 0, I claim that:
        # sum([0..N]) == N * (N + 1) // 2, where sum([A..B]) == A + (A+1) + (A+2) + ... + B

        # PROOF:
        # P(N): sum([0..N]) == N * (N + 1) // 2
        # Want to show: P(N) is True for ALL N >= 0

        # Base Case: Let's show that P(0) holds, i.e. P(N) when N = 0
        #   sum([0..N]) == sum([0..0]) == sum([0]) == 0
        #   N * (N + 1) // 2 == 0 * (0 + 1) // 2 == 0 * 1 // 2 == 0 // 2 == 0
        #   Therefore, P(0) is True!

        # Inductive Step: Suppose P(i) is true, where i >= 0. Let's show that P(i + 1) holds.
        #   Since P(i) is true, we have that sum([0..i]) == i * (i + 1) // 2 [I.H.]
        #   We want to show that P(i + 1) holds, i.e. that sum([0..(i+1)]) == (i + 1) * ((i + 1) + 1) // 2
        #   sum([0..(i+1)])
        #   == sum([0..i]) + (i + 1)
        #   == (i * (i + 1) // 2) + (i + 1), by [I.H.]
        #   == (i + 1) * (i//2 + 1)
        #   == (i + 1) * (i//2 + 2//2)
        #   == (i + 1) * (i + 2) // 2
        #   == (i + 1) * ((i + 1) + 1) // 2
        #   Therefore, given P(i) is True, P(i + 1) must also be True.

        # Therefore, by proof by Induction, it must be that P(N) is True for all N >= 0!

        # P(0) ==> P(1) ==> P(2) ==> P(3) ==> P(4) ==> P(5) ==> ... P(N), for any N >= 0

        # HW: Prove that the sum of the first N odd positive integers (i.e. 1,3,5,7,9,11,...),
        # is EQUAL to N^2.
        # For example, with N = 3, sum of first 3 odd positive integers is:
        #   1 + 3 + 5 == 9
        # And N^2 is equal to:
        #   3 * 3 == 9