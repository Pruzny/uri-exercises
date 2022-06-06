testGrade = int(input())
if testGrade == 0:
    print('E')
elif 0 < testGrade <= 35:
    print('D')
elif 35 < testGrade <= 60:
    print('C')
elif 60 < testGrade <= 85:
    print('B')
else:
    print('A')
