```
from sortedcontainers import SortedList
​
class FoodRatings:
​
def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
# Solution - ordered set
# Time - O(NlogN)
# Space - O(N)
self.hashSet = {}
self.cuisineSet = defaultdict(lambda: SortedList())
self.foodCuisineMap = {}
for i in range(len(foods)):
self.foodCuisineMap[foods[i]] = cuisines[i]
self.hashSet[foods[i]] = (-1 * ratings[i], foods[i])
self.cuisineSet[cuisines[i]].add(self.hashSet[foods[i]])
def changeRating(self, food: str, newRating: int) -> None:
# Time - O(log(N))
# Space - O(1)
prev = self.hashSet[food]
self.hashSet[food] = (-1 * newRating, food)
self.cuisineSet[self.foodCuisineMap[food]].remove(prev)
self.cuisineSet[self.foodCuisineMap[food]].add(self.hashSet[food])
return ""
​
def highestRated(self, cuisine: str) -> str:
# Time - O(1)
# Space - O(1)
return self.cuisineSet[cuisine][0][1]
```