class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        assert N == len(position) == len(speed)
        POSITION, SPEED = 0, 1

        cars = [(position[i], speed[i]) for i in range(N)]
        cars.sort(key = lambda car: car[POSITION], reverse=True)

        stack = [float("-inf")]

        for car in cars:
            pos, spd = car
            time_to_arrive = (target - pos) / spd

            if time_to_arrive > stack[-1]:
                # Takes longer to arrive than current fleet, hence begins its own
                # new fleet
                stack.append(time_to_arrive)
            else:
                # Joins part of current fleet
                continue
        
        return len(stack) - 1
