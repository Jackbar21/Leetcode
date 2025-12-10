class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = pow(10, 9) + 7
        N = len(complexity)

        # These complexity mappings essentially form a DAG. Only a computer
        # with lower complexity (and a lower index) can unlock another computer.
        # The only problem, is we cannot spend O(N^2) time building an adj_list with all edges...

        # I checked the hints, this is really lame...
        first_complexity = complexity[0]
        for i in range(1, N):
            if complexity[i] <= first_complexity:
                return 0
        def factorial(n):
            assert n >= 0
            if n <= 1:
                return 1
            return n * factorial(n - 1) % MOD
        return factorial(N - 1)
