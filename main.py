from PyPDF2 import PdfReader
import argparse
import sys

parser = argparse.ArgumentParser(description='Build a custom wordlist')
parser.add_argument('source_file', type=str, help='The source file to build a wordlist from')
parser.add_argument('output_file', type=str, help='The output file to write the wordlist to')
parser.add_argument('--common', '-c', dest='common_words', type=str, help='Custom common word list to use')
args = parser.parse_args()

word_dictionary = {}
path_to_input = args.source_file
path_to_output = args.output_file
common_words = ''

if args.common_words is not None:
    common_words = args.common_words
else:
    common_words = 'common_words.txt'


def read_pages():
    reader = PdfReader(path_to_input)
    number_of_pages = len(reader.pages)

    common_list = []
    is_common = False

    with open(common_words, 'r') as f:
        for cmn_wrd in f:
            for word in cmn_wrd.split():
                common_list.append(word)

    for x in range(number_of_pages):
        page = reader.pages[x]
        text = page.extract_text().lower()
        textsplit = text.split()
        for word in textsplit:
            # check to see if our word is a common word
            for cmn_wrd in common_list:
                if word != cmn_wrd.strip():
                    continue
                else:
                    is_common = True
                    break

            if is_common:
                is_common = False
                continue
            else:
                if word_dictionary.get(word) is not None:
                    word_dictionary[word] += 1
                else:
                    word_dictionary[word] = 1

    print(word_dictionary.keys())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_pages()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
