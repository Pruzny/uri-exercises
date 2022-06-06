def test(nums):
    a, b, c, d = map(int, nums.split())
    if c % a == 0:
        for num in range(a, (int(c**(1/2))+1)*a, a):
            if c % num == 0:
                if num % b != 0:
                    if d % num != 0:
                        return num
        if c % b != 0 and d % c != 0:
            return c
    return -1


print(test(input()))
