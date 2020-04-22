# Practice project 1: Table printer
table_data = [['chocolate frogs', 'butter beer', 'jelly beans', 'pumpkin pasties'],
              ['Harry', 'Hermoine', 'Ron', 'Luna'],
              ['owls', 'cats', 'rats', 'nargles']]


def print_table(list):
    col_width = [0] * len(list)
    index = 0

    for inner_list in list:
        col_width[index] = max(len(x) for x in inner_list)
        word_location = 0
        for word in inner_list:
            list[index][word_location] = word.rjust(col_width[index])
            word_location += 1
        index += 1

    for index_word in range(0, len(inner_list)):
        table = []
        for index_list in range(0, len(list)):
            table.append(list[index_list][index_word])
        print(' '.join(table))


print_table(table_data)
