class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        assert N == len(position) == len(speed)
        POSITION, SPEED = 0, 1

        cars = [(position[i], speed[i]) for i in range(N)]
        cars.sort(key = lambda car: car[POSITION], reverse=True)

        # stack = [float("-inf")]
        res = 0
        latest_time = float("-inf")

        for car in cars:
            pos, spd = car
            time_to_arrive = (target - pos) / spd

            if time_to_arrive > latest_time:
                # Takes longer to arrive than current fleet, hence begins its own
                # new fleet
                latest_time = time_to_arrive
                res += 1
            else:
                # Joins part of current fleet
                continue
        
        return res
