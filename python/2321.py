left_x0, down_y0, right_x0, up_y0 = map(int, input().split())
left_x1, down_y1, right_x1, up_y1 = map(int, input().split())
if left_x0 <= left_x1 <= right_x0 or left_x0 <= right_x1 <= right_x0 or (left_x1 < left_x0 and right_x1 > right_x0):
    x_intersection = True
else:
    x_intersection = False
if down_y0 <= down_y1 <= up_y0 or down_y0 <= up_y1 <= up_y0 or (down_y1 < down_y0 and up_y1 > up_y0):
    y_intersection = True
else:
    y_intersection = False
if x_intersection and y_intersection:
    print(1)
else:
    print(0)
