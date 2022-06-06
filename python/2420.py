section_count = int(input())
section_list = list(map(int, input().split()))
section_sum = sum(section_list)//2
partial_sum = 0
for i in range(section_count):
    partial_sum += section_list[i]
    if partial_sum == section_sum:
        print(i+1)
        break
