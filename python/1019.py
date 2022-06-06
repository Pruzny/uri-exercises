durationSec = int(input())
timeHour = durationSec // 60 // 60
timeMin = durationSec // 60 % 60
timeSec = durationSec % 60
print(f'{timeHour}:{timeMin}:{timeSec}')
