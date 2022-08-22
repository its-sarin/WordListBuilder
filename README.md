# WordListBuilder
A tool that builds custom wordlists using unique words from a source PDF document. The built wordlist is automatically sorted by appearance frequency.

## Install:

    $ git clone https://github.com/its-sarin/WordListBuilder.git
    $ pip3 install -r requirements.txt

## Basic Usage:

    $ ./wordlistbuilder.py ~/path/to/source/pdf ~/path/to/output/file

## Optional Usage:

    # build wordlist starting from specified page number (of source document) 
    $ ./wordlistbuilder.py --start 5 ~/path/to/source/pdf ~/path/to/output/file

    # build wordlist ending with specified page number (of source document)
    $ ./wordlistbuilder.py --end 25 ~/path/to/source/pdf ~/path/to/output/file

    # build wordlist starting from and ending with specified page numbers
    $ ./wordlistbuilder.py --start 5 --end 25 ~/path/to/source/pdf ~/path/to/output/file
    
    # use a custom common words list to be excluded from final output (list should be line-delimited)
    $ ./wordlistbuilder.py --common ~/path/to/common/list ~/path/to/source/pdf ~/path/to/output/file

    # discard URLs from final output
    $ ./wordlistbuilder.py --no-url ~/path/to/source/pdf ~/path/to/output/file

    # print list of ignored words to console with final output 
    $ ./wordlistbuilder.py --ignored ~/path/to/source/pdf ~/path/to/output/file

## Example:
    
    $ ./wordlistbuilder.py --common ~/Documents/mylist.txt --start 1 ~/Documents/report.pdf ~/Documents/wordlist.txt
    $ File created at: /home/user/Documents/wordlist.txt
    
## Help output:

    usage: wordlistbuilder.py [-h] [--common PATH_TO_COMMON_WORDS] [--start START_PAGE_NUM]
                          [--end END_PAGE_NUM] [--no-url [SHOW_NO_URL]] [--ignored [SHOW_IGNORED]]
                          source_file output_file

    Build a custom wordlist from a source PDF

    positional arguments:
      source_file           The source file to build a wordlist from
      output_file           The output file to write the wordlist to

    options:
      -h, --help            show this help message and exit
      --common PATH_TO_COMMON_WORDS, -c PATH_TO_COMMON_WORDS
                            Custom common word list to be excluded from output
      --start START_PAGE_NUM, -s START_PAGE_NUM
                            Page number to start on
      --end END_PAGE_NUM, -e END_PAGE_NUM
                            Page number to end on
      --no-url [SHOW_NO_URL], -n [SHOW_NO_URL]
                            Disable retention of URLs
      --ignored [SHOW_IGNORED], -i [SHOW_IGNORED]
                            Print list of ignored words after wordlist is built

 ## Todo:
 
    * Add functionality to support other file types for source file
    * Add option to discard email addresses
    * Improve word detection through RegEx patterns
