#! /usr/bin/env python3
# Current issue:
#  1. Abbreviations getting cut off such as could've, don't

import re

class BookIndex:

    def __init__(self, bookName):
        self.word_index = dict()
        self.book_name = bookName

    def index_book(self, path_to_book):
        with open(path_to_book, 'r', encoding='utf-8') as f:
            for line in f:
                split_line = re.split('[\W]', line)
                for word in split_line:
                    norm_word = word.lower()
                    if self.word_index.get(norm_word) is not None:
                        self.word_index[norm_word] += 1
                    else:
                        self.word_index[norm_word] = 1

    def word_freq(self, word):
        norm_word = word.lower()
        if (self.word_index.get(norm_word) is not None):
            return self.word_index.get(norm_word)
        else:
            print('The word: {} is not found in the book.'.format(norm_word))
                
    def print(self):
        print(self.word_index)
                        
def main():
    pride_index = BookIndex('Pride and Prejudice')
    book_path = '/Users/moses/interviewprep/problems/cracking/pride.txt'
    pride_index.index_book(book_path)
    #print('Freq of \'Mr\': {}'.format(pride_index.word_freq('Mr')))
    #print('Freq of \'his\': {}'.format(pride_index.word_freq('his')))
    pride_index.print()

if __name__ == '__main__':
    main()
