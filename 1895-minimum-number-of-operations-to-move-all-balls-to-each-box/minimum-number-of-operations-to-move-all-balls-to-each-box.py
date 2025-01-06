class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # answer = [0] * len(boxes)
        # for i in range(len(boxes)):
        #     for j in range(len(boxes)):
        #         answer[i] += int(boxes[j]) * abs(i - j)
        
        # return answer

        # Count number of balls up to each index i
        total_num_balls = 0
        prefix_count = [] # prefix_count[i] == # of "1" in boxes[0..i]
        for digit in boxes:
            if digit == "1":
                total_num_balls += 1
            prefix_count.append(total_num_balls)
        
        prefix_sums = [0]
        count = 0
        for digit in boxes:
            count += digit == "1"
            prev = prefix_sums[-1]
            prefix_sums.append(prev + count)
        prefix_sums.pop()
        
        suffix_sums = [0]
        count = 0
        for digit in reversed(boxes):
            count += digit == "1"
            suffix_sums.append(suffix_sums[-1] + count)
        suffix_sums.pop()
        suffix_sums = (suffix_sums)[::-1]
        # print(f"{suffix_sums=}")
        
        # print(f"{prefix_sums=}")
        
        # print(f"{prefix_count=}")
        # print(f"{total_num_balls=}")

        return [prefix_sums[i] + suffix_sums[i] for i in range(len(boxes))]
        # return answer
        
