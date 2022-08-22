from PyPDF2 import PdfReader
import argparse

parser = argparse.ArgumentParser(description='Build a custom wordlist from a source PDF')
parser.add_argument('source_file', type=str, help='The source file to build a wordlist from')
parser.add_argument('output_file', type=str, help='The output file to write the wordlist to')
parser.add_argument('--common', '-c', dest='path_to_common_words', type=str, help='Custom common word list to be excluded from output')
parser.add_argument('--start', '-s', dest='start_page_num', type=int, help='Page number to start on')
parser.add_argument('--end', '-e', dest='end_page_num', type=int, help='Page number to end on')
args = parser.parse_args()

word_dictionary = {}
path_to_input = args.source_file
path_to_output = args.output_file
starting_page = args.start_page_num or 0
ending_page = args.end_page_num
common_words = args.path_to_common_words or 'common_words.txt'


def read_pages():
    reader = PdfReader(path_to_input)
    number_of_pages = len(reader.pages)

    # init a few variables for later
    common_list = []
    is_common = False

    # store our common words list in an array
    with open(common_words, 'r') as f:
        for line in f:
            for word in line.split():
                common_list.append(word)

    # iterate through our PDF pages
    for x in range(starting_page, ending_page or number_of_pages):
        page = reader.pages[x]
        text = page.extract_text().lower()
        textsplit = text.split()
        for word in textsplit:
            word = word.strip(',.;')

            # check to see if our word is a common word
            for cmn_wrd in common_list:
                if word != cmn_wrd:
                    continue
                else:
                    is_common = True
                    break

            # if this word is common, we move on
            if is_common:
                is_common = False
                continue
            # otherwise we check to see if it already exists in our dictionary
            else:
                # if it does, increment the word's count
                if word_dictionary.get(word) is not None:
                    word_dictionary[word] += 1
                # if it does not, initialize the word at 1
                else:
                    word_dictionary[word] = 1

    # write our newly built wordlist to the specified location
    with open(path_to_output, 'a') as file:
        for key in word_dictionary.keys():
            file.write(key + '\n')
        print("File created at: " + path_to_output)


if __name__ == '__main__':
    read_pages()
