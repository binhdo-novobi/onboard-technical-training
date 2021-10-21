def count_words(text):
    count_dict = {}
    words = text.split()
    for w in words:
        if w in count_dict.keys():
            count_dict[w] += 1
        else:
            count_dict[w] = 1
    return count_dict


def write_file(count_dict, fileout):
    result = filter(lambda w: count_dict[w] > 1, count_dict)
    with open(fileout, 'w') as fout:
        fout.write(','.join(result))


def check_word_exist(count_dict, word):
    if word in count_dict.keys():
        print(count_dict[word])
    else:
        print("{} does not exist".format(word))


if __name__ == "__main__":
    filein = "text.txt"
    fileout = "out.txt"
    with open(filein, 'r') as fin:
        text = fin.read()
        print(text[:100])
        count_dict = count_words(text)
        print(count_dict)
        write_file(count_dict, fileout)
        word = input("Enter a word: ")
        check_word_exist(count_dict, word)
