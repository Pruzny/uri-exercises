original_list = list(chr(char) for char in range(97, 123))
code_list = list(char for char in input())
original_phrase = ''
for char in input():
    original_phrase += original_list[code_list.index(char)]
print(original_phrase)
