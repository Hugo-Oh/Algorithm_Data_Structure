import sys
sys.stdin = open("input.txt", "rt")
from _collections import deque

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

res = 5 * cacheSize
cache = deque(cities[:cacheSize])

cities = deque(cities[cacheSize:])

while cities and cache:
    tmp = cities.popleft().lower()
    print(tmp, cache, cities, res)
    if tmp.lower() in cache: # hit
        res += 1

    else: #miss
        cache.popleft()
        cache.append(tmp)
        res += 5

if cacheSize == 0 :
    res = 5 * len(cities)

print(res)