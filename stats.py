def get_num_words(s):
    return len(s.split())

def get_char_count(s):
    char_table = {}
    for c in s:
        c = c.lower()
        if c not in char_table:
            char_table[c] = 0
        char_table[c] += 1

    return char_table


def get_sorted_char_counts_pairs(char_counts):
    char_count_pairs_list = []
    for char in char_counts:
        char_count_pairs_list.append({"char": char, "num": char_counts[char]})
        
    char_count_pairs_list.sort(key=char_counts_sort, reverse=True)
    return char_count_pairs_list

def char_counts_sort(items):
    return items["num"]