results = []
size = int(input())
for _ in range(1, size + 1):
    n, k = map(int, input().split())
    soldiers = list(i for i in range(1, n + 1))
    position = (k - 1) % n
    for i in range(n-1, 0, -1):
        soldiers.pop(position)
        position = (position + k - 1) % i
    results.append(soldiers[0])

for i, result in enumerate(results):
    print(f"Case {i+1}: {result}")
