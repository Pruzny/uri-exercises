key_string = input()
len_key = len(key_string)
for _ in range(int(input())):
    message_str = input()
    message_tup = message_str.split()
    full_key = key_string*(len(message_str)//len_key + 1)
    key_list = []
    key_count = 0
    for word in message_tup:
        if word[0] in 'aeiou':
            key_list.append(word)
        else:
            word_key = ''
            for char in range(len(word)):
                word_key += full_key[key_count]
                key_count += 1
            key_list.append(word_key)
    code_message = ''
    for word_m, word_k in zip(message_tup, key_list):
        if word_m[0] not in 'aeiou':
            for char_m, char_k in zip(word_m, word_k):
                char_ord = ord(char_m) - 97 + ord(char_k) - 97
                if char_ord > 25:
                    char_ord -= 26
                code_message += chr(char_ord+97)
        else:
            code_message += word_m
        code_message += ' '
    print(code_message[:-1])
