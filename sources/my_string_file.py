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
    return count_dict.get(word, 0)


if __name__ == "__main__":
    filein = "text.txt"
    fileout = "out.txt"
    with open(filein, 'r') as fin:
        print("Reading file '{}' ...".format(filein))
        text = fin.read()
        print("\nWriting words that appear more than 1 time into file '{}' ...".format(fileout))
        count_dict = count_words(text)
        write_file(count_dict, fileout)
        print("\nFirst 100 characters:\n", text[:100])
        print("\nThe count of appearence for each word:\n", count_dict)
        word = input("\nEnter a word: ")
        count = check_word_exist(count_dict, word)
        if count != 0:
            print("The word '{}' appears {} time(s).".format(word, count))
        else:
            print("The word '{}' does not exist.".format(word))
