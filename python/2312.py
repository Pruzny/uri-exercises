def namesort(n):
    return n[0]


def bronzesort(b):
    return int(b[3])


def silversort(s):
    return int(s[2])


def goldsort(g):
    return int(g[1])


country_list = []
country_num = int(input())
for _ in range(country_num):
    country_list.append(input().split())

country_list.sort(key=namesort)
country_list.sort(key=bronzesort, reverse=True)
country_list.sort(key=silversort, reverse=True)
country_list.sort(key=goldsort, reverse=True)

for country in country_list:
    print(country[0], country[1], country[2], country[3])
