class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [(-1, float("inf"))]

        INDEX, TEMPERATURE = 0, 1
        for index, temperature in enumerate(temperatures):
            while stack[-1][TEMPERATURE] < temperature:
                i, temp = stack.pop()
                answer[i] = index - i

            # Loop Invariant
            stack.append((index, temperature))
        
        # assert all([val != -1 for val in answer])
        return answer