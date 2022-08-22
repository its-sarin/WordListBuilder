# WordListBuilder
A tool for extracting unique words from documents and building a wordlist using those words

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

## Example:
    
    $ ./wordlistbuilder.py --common ~/Documents/mylist.txt --start 1 ~/Documents/report.pdf ~/Documents/wordlist.txt
    $ File created at: /home/user/Documents/wordlist.txt

