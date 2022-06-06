def timetomin(time):
    hour, minute = map(int, time.split(':'))
    return hour*60 + minute


pa, cb, pb, ca = map(timetomin, input().split())
travel_time = cb - pa + ca - pb
travel_time = travel_time % 1440 // 2

time_dif = int((cb - pa - travel_time)/60)
if time_dif <= -12:
    time_dif += 24
elif time_dif > 12:
    time_dif -= 24

print(travel_time, time_dif)
