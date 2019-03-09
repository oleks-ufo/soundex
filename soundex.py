def soundex(word):
    word = word.lower()
    result = ''
    code_str = ''
    code_dict = {
        'bfpv': '1',
        'cgjkqsxz': '2',
        'dt': '3',
        'l': '4',
        'mn': '5',
        'r': '6',
        'aeiouy': 'i',
    }

    for char in word:
        for key, val in code_dict.items():
            if char in key:
                code_str += val

    code_str += 'i'

    if code_str[0] == code_str[1]:
        code_str = code_str[2:]
    else:
        code_str = code_str[1:]

    for index in range(len(code_str) - 1):
        if code_str[index] != code_str[index + 1]:
            result += code_str[index]

    result = result.replace('i', '')

    while len(result) < 3:
        result += '0'

    return "{}{}".format(word[0], result[:3])


def get_info_from_files():
    right_words_list = []
    wrong_words_dict = {}
    input_list = []
    line_number_list = []
    PUNCTUATION = ',.)('

    with open('words.txt') as words:
        for line in words:
            right_words_list.append(line.strip())

    with open('input.txt') as inp_file:
        for line in inp_file:
            input_list.append(line.split())

    for index, line in enumerate(input_list):
        for word in line:
            for symbol in PUNCTUATION:
                word = word.replace(symbol, '').lower()
            if word not in right_words_list:
                wrong_words_dict[word] = index + 1

    context = (right_words_list, wrong_words_dict, line_number_list, )
    return context


right_words_list, wrong_words_dict, line_number_list = get_info_from_files()

right_words_codes_dict = {}

for x in right_words_list:
    code = soundex(x)
    if code in right_words_codes_dict:
        right_words_codes_dict[code].append(x)
    else:
        right_words_codes_dict[code] = [x]


for word, num in wrong_words_dict.items():
    code = soundex(word)
    if code in right_words_codes_dict:
        sugest = ''
        for x in right_words_codes_dict[code]:
            sugest += x + ' '

        print('Found unknown word "{}" in line {}. Suggestions: {}'.format(
            word, num, sugest,
            )
        )






