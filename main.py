from collections import deque

n = int(input())
queue = deque()
queue = list(map(str, input().split()))
print(" ".join(reversed(queue)))

