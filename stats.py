def num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    chars = {}

    for char in text:
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1

    return chars

def sorted_char_count(chars):
    char_list = [{'char': char, 'count':count} for char, count in chars.items()]
    char_list.sort(key=lambda x: x['count'], reverse=True)

    return char_list

