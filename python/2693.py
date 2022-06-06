def namesort(n):
    return n[0]


def regionsort(r):
    return r[1]


def distancesort(d):
    return int(d[2])


route_list = []

while True:
    try:
        passenger_list = []
        passenger_num = int(input())
        for _ in range(passenger_num):
            passenger_list.append(input().split())
        passenger_list.sort(key=namesort)
        passenger_list.sort(key=regionsort)
        passenger_list.sort(key=distancesort)
        for name in passenger_list:
            route_list.append(name[0])
    except EOFError:
        break

for passenger in route_list:
    print(passenger)
