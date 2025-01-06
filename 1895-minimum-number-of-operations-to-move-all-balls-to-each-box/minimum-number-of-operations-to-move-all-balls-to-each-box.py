class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)

        for i in range(len(boxes)):
            for j in range(len(boxes)):
                answer[i] += int(boxes[j]) * abs(i - j)
        
        return answer