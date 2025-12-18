def word_count(file_contents):
    split_file = file_contents.split()
    return len(split_file)

def character_count(file_contents):
    char_dict = {}
    file_len = len(file_contents)
    for i in range (0, file_len):
        c = file_contents[i].lower()
        if c not in char_dict:
            char_dict[c] = 0
        char_dict[c] += 1
    return char_dict

def dictionify(old_dict):
    char_list = []
    for i in old_dict:
        if i.isalpha():
            char = {
                "char": i,
                "num": old_dict[i]
                }
            char_list.append(char)
    return char_list

def sort_on(items):
    return items['num']

def sort_dict(dictionary):
    return dictionary.sort(reverse=True, key=sort_on)


