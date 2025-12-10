class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = pow(10, 9) + 7
        N = len(complexity)

        # These complexity mappings essentially form a DAG. Only a computer
        # with lower complexity (and a lower index) can unlock another computer.
        # The only problem, is we cannot spend O(N^2) time building an adj_list with all edges...

        # I checked the hints, this is really lame...
        first_complexity = complexity[0]
        count = 0
        for c in complexity:
            count += c <= first_complexity
            if count > 1:
                return 0
        return math.factorial(N - 1) % MOD
