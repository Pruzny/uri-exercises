def josephus(n: int, k: int) -> int:
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


def josephus2(n: int, k: int) -> int:
    soldier = 1
    for i in range(1, n + 1):
        soldier = (soldier + k - 1) % i + 1
    return soldier


results = []
size = int(input())
for _ in range(1, size + 1):
    n, k = map(int, input().split())
    results.append(josephus2(n, k))

for i, result in enumerate(results):
    print(f"Case {i+1}: {result}")
