word_list = []

while True:
    try:
        text = input().lower()
        for char in text:
            if char not in 'abcdefghijklmnopqrstuvwxyz ':
                text = text.replace(char, ' ')
        text = text.split()
        for word in text:
            word_list.append(word)
    except EOFError:
        break

word_list = sorted(list(set(word_list)))
for word in word_list:
    print(word)
