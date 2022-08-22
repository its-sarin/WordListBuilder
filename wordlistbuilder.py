#!/usr/bin/python3

from PyPDF2 import PdfReader
import argparse

parser = argparse.ArgumentParser(description='Build a custom wordlist from a source PDF')
parser.add_argument('source_file', type=str, help='The source file to build a wordlist from')
parser.add_argument('output_file', type=str, help='The output file to write the wordlist to')
parser.add_argument('--common', '-c', dest='path_to_common_words', type=str,
                    help='Custom common word list to be excluded from output')
parser.add_argument('--start', '-s', dest='start_page_num', type=int, help='Page number to start on')
parser.add_argument('--end', '-e', dest='end_page_num', type=int, help='Page number to end on')
parser.add_argument('--no-url', '-n', dest='show_no_url', nargs='?', const='not_given', type=bool,
                    help='Disable retention of URLs')
parser.add_argument('--ignored', '-i', dest='show_ignored', nargs='?', const='not_given', type=bool,
                    help='Print list of ignored words after wordlist is built')
args = parser.parse_args()

word_dictionary = {}
ignored_words = []

path_to_input = args.source_file
path_to_output = args.output_file
starting_page = args.start_page_num or 0
ending_page = args.end_page_num
common_words = args.path_to_common_words or 'common_words.txt'
show_no_url = args.show_no_url if args.show_no_url != 'not_given' else False
show_ignored = args.show_ignored if args.show_ignored != 'not_given' else False


def read_pages():
    reader = PdfReader(path_to_input)
    number_of_pages = len(reader.pages)

    # init a few variables for later
    common_list = []
    ignore = False

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
            word = word.strip(',;')

            # if this word is already in the ignored list, ignore it and move on
            for w in ignored_words:
                if w == word:
                    ignore = True

            # we ignore words 3 characters or fewer as those are likely not worth retaining
            if len(word) <= 3:
                ignore = True
                ignored_words.append(word)

            # if the no_url flag is enabled, we attempt to ignore URLs
            if show_no_url:
                if 'http://' in word or 'www.' in word:
                    ignore = True
                    ignored_words.append(word)

            # if the ignore flag isn't set for this word, we check to see if it's a common word
            if not ignore:
                for cmn_wrd in common_list:
                    if word != cmn_wrd.strip():
                        continue
                    else:
                        ignore = True
                        break

            # if this word is flagged to ignore, we move on
            if ignore:
                ignore = False
                continue
            # otherwise we check to see if it already exists in our dictionary
            else:
                # if it does, increment the word's count
                if word_dictionary.get(word) is not None:
                    word_dictionary[word] += 1
                # if it does not, initialize the word at 1
                else:
                    word_dictionary[word] = 1

    # sort our dictionary by value to list words in order of frequency
    sorted_dictionary = sorted(word_dictionary, key=word_dictionary.get, reverse=True)

    # if flag is set, print ignored words list to console
    if show_ignored:
        print('Ignored words: \n')
        print(ignored_words)

    # write our newly built wordlist to the specified location
    with open(path_to_output, 'w') as file:
        for line in sorted_dictionary:
            file.write(line + '\n')
        print("File created at: " + path_to_output)


if __name__ == '__main__':
    read_pages()
