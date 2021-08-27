"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Outputs the words in a state of the union address
that occur 4 or more times. Omits words that are very common.
You can find the state of the union input texts we tried at
http://stateoftheunion.onetwothree.net/texts/
"""


def main():
    file = open("StateOfTheUnion.txt")
    print('File contains 1, 82,581 lines')
    print('Before applying elimination of common words, file contains 10, 808, 003 words')
    words = file.read()
    print(len(words))
    # Gets rid of punctuation
    words = words.replace(".", "").replace(",", "").replace(";", "")
    words = words.replace("!", "").replace("?", "").replace("\"", "")
    words = words.replace("--", " ")
    words = words.split()

    # Reads all words from the file into a dictionary which maps words to counts of occurrences
    dict_words = {}
    for word in words:
        word = word.lower()
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    print(dict_words)
    common_set = create_set("common_words.txt")

    for word, count in dict_words.items():
        if count >= 4 and word not in common_set:
            print(word + " = " + str(count))


# Creates and returns a set containing all of the words from the file with the passed in name.
def create_set(file_name):
    positive = set()
    positive_words = open(file_name).read()
    positive_words = positive_words.split()
    for word in positive_words:
        positive.add(word)
    return positive


main()
