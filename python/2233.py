r_size = int(input(), 16)
g_size = int(input(), 16)
b_size = int(input(), 16)
g_total = (r_size//g_size)**2
b_total = (g_size//b_size)**2
tag_total = 1 + g_total + g_total*b_total
print(hex(tag_total)[2:])
