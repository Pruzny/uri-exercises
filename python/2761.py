from struct import unpack, pack

int_var, float_var, char_var, string_var = input().split(maxsplit=3)
float_var = f'{unpack("f", pack("f", float(float_var)))[0]:.6f}'
print(int_var + float_var + char_var + string_var)
print("{}\t{}\t{}\t{}".format(int_var, float_var, char_var, string_var))
print("{:>10}{:>10}{:>10}{:>10}".format(int_var, float_var, char_var, string_var))


# def singlep(f):
#     if f != 0:
#         if f == int(f):
#             return f
#         else:
#             num_int = int(f)
#             num_dec = f - num_int
#             int_string = str(bin(num_int))[2:]
#             dec_string = ''
#             while num_dec * 2 < 1:
#                 num_dec *= 2
#                 dec_string += str(int(num_dec))
#                 if num_dec >= 1:
#                     num_dec -= 1
#             for _ in range(24):
#                 num_dec *= 2
#                 dec_string += str(int(num_dec))
#                 if num_dec >= 1:
#                     num_dec -= 1
#             num_string = f'{int_string},{dec_string}'
#             print(num_string)
#             exp = num_string.index(',') - num_string.index('1') - 1
#             print(exp)
#             num_string = num_string.replace(',', '')
#             num_string = num_string[num_string.index('1')+1:]
#             num_string = num_string[:23]
#             base = 1
#             print(num_string)
#             for pot, num in enumerate(num_string):
#                 base += 2**(-pot-1)*int(num)
#             return base*2**exp
#     else:
#         return 0
