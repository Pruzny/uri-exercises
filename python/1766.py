def namesort(n):
    return n[0]


def heightsort(h):
    return h[3]


def agesort(a):
    return a[2]


def weightsort(w):
    return w[1]


delivery_list = []
delivery_num = int(input())
for _ in range(delivery_num):
    total_reindeer, delivery_reindeer = map(int, input().split())
    reindeer_list = []
    for _ in range(total_reindeer):
        name, weight, age, height = input().split()
        reindeer_list.append([name, int(weight), int(age), float(height)])

    reindeer_list.sort(key=namesort)
    reindeer_list.sort(key=heightsort)
    reindeer_list.sort(key=agesort)
    reindeer_list.sort(key=weightsort, reverse=True)
    name_list = []
    for reindeer in reindeer_list[:delivery_reindeer:]:
        name_list.append(reindeer[0])
    delivery_list.append(name_list)

for num, delivery in enumerate(delivery_list):
    print('CENARIO {', end='')
    print(num+1, end='')
    print('}')
    for pos, reindeer in enumerate(delivery):
        print(f'{pos+1} - {reindeer}')
