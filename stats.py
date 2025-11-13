def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def get_sorted_chars(chars_dict):
    # 1. create an empty list to hold mini dictionaries
	num_list = []
	
    # 2. for each character in chars_dict:
        # a) check if character is alphabetical
        # b) if yes, create a mini dictionary with 'char' and 'num'
        # c) add mini dictionary to the list
	for char in chars_dict:
		if char.isalpha():
			mini_dict = {"char": char, "num": chars_dict[char]}
			num_list.append(mini_dict)

	
    # 3. sort the list by 'num' descending
	num_list.sort(key=sort_on, reverse=True)
	
    # 4. return the sorted list
	return num_list
