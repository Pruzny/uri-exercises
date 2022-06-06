binStart, dayStart = map(str, input().split())
hourStart, minStart, secStart = map(int, input().split(':'))
binEnd, dayEnd = map(str, input().split())
hourEnd, minEnd, secEnd = map(int, input().split(':'))
dayTime = int(dayEnd) - int(dayStart)
hourTime = hourEnd - hourStart
minTime = minEnd - minStart
secTime = secEnd - secStart
if hourTime < 0:
    dayTime -= 1
    hourTime += 24
if minTime < 0:
    hourTime -= 1
    minTime += 60
if secTime < 0:
    minTime -= 1
    secTime += 60
print(f'{dayTime} dia(s)\n'
      f'{hourTime} hora(s)\n'
      f'{minTime} minuto(s)\n'
      f'{secTime} segundo(s)')
