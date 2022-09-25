# https://contest.yandex.ru/contest/8458/problems/G/

# import sys
 
# j = sys.stdin.readline().strip()
# s = sys.stdin.readline().strip()


class Solution:
    def findTravel(self, arr: list) -> bool:

        n = arr[0] # cities count
        cities = arr[1:-2]
        max_distance = arr[-2] # max distance
        city_from = arr[-1][0]
        city_to = arr[-1][1]

        coords_from = cities[city_from-1]
        coords_to = cities[city_to-1]

        # print(f"coords_from: {coords_from}, coords_to: {coords_to}")

        width = abs(coords_to[0] - coords_from[0])
        height = abs(coords_to[1] - coords_from[1])

        # print(f"width: {width}, height: {height}")

        if width <= max_distance and height <= max_distance:
            return int(width / max_distance + height / max_distance)
        else:
            return -1

        
        
def test_solution():
    assert Solution().findTravel([7, [0,0], [0,2], [2,2], [0-2], [2,-2], [2,-1], [2,1], 2, [1,3]]) == 2
    assert Solution().findTravel([4, [0,0], [1,0], [0,1], [1,1], 2, [1,4]]) == 1
    assert Solution().findTravel([4, [0,0], [2,0], [0,2], [2,2], 1, [1,4]]) == -1



