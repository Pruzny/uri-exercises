vowel_string = ''
reversed_string = ''
laugh_string = input()
for char in laugh_string:
    if char in 'aeiou':
        vowel_string += char
        reversed_string = char + reversed_string
if vowel_string == reversed_string:
    print('S')
else:
    print('N')
