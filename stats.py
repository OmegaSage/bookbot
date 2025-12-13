letter_count = dict()


def get_num_words(text):
    return len(text.split())


def character_count(text):
    global letter_count
    letter_count = []
    letters = [char.lower() for char in text if char.isalpha()]
    for letter in letters:
        for items in letter_count:
            if items["char"] == letter:
                items["num"] += 1
                break
        else:
            letter_count.append({"char": letter, "num": 1})
    return letter_count


def sort_on(x):
    return x["num"]


def sort_letter_count(char_dict):
    # print(char_dict)
    sorted_list = []
    char_dict.sort(key=sort_on, reverse=True)
    sorted_list = char_dict
    # for item in char_dict:
    # sorted_list.append(char_dict[item].sort(key=sort_on, reverse=True))
    return sorted_list
