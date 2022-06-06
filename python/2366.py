station_count, max_distance = map(int, input().split())
station_list = list(map(int, input().split()))
possible = 'S'
for i in range(station_count-1):
    if station_list[i+1] - station_list[i] > max_distance:
        possible = 'N'
if 42195 - station_list[station_count-1] > max_distance:
    possible = 'N'
print(possible)
