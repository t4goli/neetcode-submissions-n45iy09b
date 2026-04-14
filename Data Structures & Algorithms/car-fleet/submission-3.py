class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        if len(cars) == 0:
            return 0
        fleets = 1
        prevtime = (target - cars[0][0]) / cars[0][1]

        for i, val in enumerate(cars):
            if i == 0:
                continue
            currtime = (target - cars[i][0]) / cars[i][1]
            print(i)
            print(cars[i][0])
            print(prevtime)
            print(currtime)
            if not (currtime <= prevtime):
                fleets += 1
                prevtime = currtime

        return fleets