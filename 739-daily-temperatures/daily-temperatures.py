class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        INDEX, TEMPERATURE = 0, 1
        stack = [(None, float("inf"))] # monotonically decreasing
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            top_index, top_temp = stack[-1]
            while temp > stack[-1][TEMPERATURE]:
                top_index, top_temp = stack.pop()
                # The next index after 'top_index' that had warmer temperature
                # ocurred here at index 'i'. Hence, it took a total of 'i - top_index' days.
                answer[top_index] = i - top_index
            stack.append((i, temp))

        return answer
