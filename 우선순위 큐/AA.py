import sys
import heapq as hq
a = []
hq.heappush(a, 1)
hq.heappush(a, 3)
hq.heappush(a, 5)
hq.heappush(a, 4)
print(a)
print(hq.heappop(a))
print(hq.heappop(a))
print(hq.heappop(a))
print(hq.heappop(a))


b = []
hq.heappush(b, -1)
hq.heappush(b, -3)
hq.heappush(b, -5)
hq.heappush(b, -4)

print(list(map(lambda x : -x, b)))
print(-hq.heappop(b))
print(-hq.heappop(b))
print(-hq.heappop(b))
print(-hq.heappop(b))


