from functools import reduce

INPUT_PATH = 'text.txt'
OUTPUT_PATH = 'output.txt'

def read_and_write(input_path, output_path):

    with open(input_path, 'r') as reader:
        data = reader.readlines()
    
    freq = {}

    words = list(reduce(lambda x,y: x + y.split(" "), data, []))
    # Count word frequency
    for word in words:

        # Replace newline characters
        word = word.replace("\n", " ")

        # Count word frequency
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    larger_than_1 = []
    for keys, values in freq.items():
        if values > 1: 
            larger_than_1.append(keys)
    
    with open(output_path, 'w') as writer:
        writer.write(", ".join(larger_than_1))
    
    return freq

def print_appereance(freq_dict):

    for keys, values in freq_dict.items():
        print(f"Word: {keys}, count: {values}")

def check_for_a_word(freq_dict, inp):

    if str(inp) in freq_dict:
        print(f"The word {str(inp)} appears {freq_dict[inp]} time(s).")
    else:
        print("Word not found")

def print_first_n(freq_dict, n):
    all_char =  "".join([keys for keys in freq_dict.keys()])
    print(all_char[:n])

if __name__ == "__main__":

    """
    Read this file using python, 
    find those words that appear more than 1 time, 
    and save these words to a new file, separated by comma.
    """
    freq_dict = read_and_write(INPUT_PATH, OUTPUT_PATH)

    """
    Print out the count of appearence for each word.
    """
    # Please uncomment the following line to run
    # print_appereance(freq_dict)

    """"
    Allow user to input a word, check if the word is in the file. 
    If yes, print the times that the word appear, 
    or print out a message saying it does not exist if no.
    """
    # Please uncomment the following 2 lines to run
    # inp = input("Please input your word: ")
    # check_for_a_word(freq_dict, inp)

    """
    Print the first 100 characters of the string.
    """
    print_first_n(freq_dict, 100)
