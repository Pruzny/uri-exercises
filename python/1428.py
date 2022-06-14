from math import ceil

results = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    results.append(f"{ceil((n-2)/3) * ceil((m-2)/3)}")

for result in results:
    print(result)
