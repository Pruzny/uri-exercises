total_area, ab_points, bc_points = map(int, input().split())
while total_area != 0:
    y, x1, x2 = map(int, input().split())
    print(round(total_area*(y/(ab_points+1))*(abs(x2-x1)/(bc_points+1))))
    total_area, ab_points, bc_points = map(int, input().split())
