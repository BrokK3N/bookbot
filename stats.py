def get_num_words(pth):
    with open(pth) as f:
        contents = f.read()
        num = len(contents.split())

    return num

def get_num_char(pth):
    with open(pth) as f:
        contents = f.read()
        lower_char = contents.lower()
    char_count = {}
    
    for char in lower_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def get_count(items):
    return items["num"]

def sorted_dict(pth):
    unsorted_dict = get_num_char(pth)
    char_num_list = []
    
    for char, num in unsorted_dict.items():
        char_num_list.append({"char": char, "num": num})
    
    char_num_list.sort(reverse = True, key = get_count)

    return char_num_list