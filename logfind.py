#! /usr/bin/env python
from glob import glob
from re import search


def match_string(word, line):
    if search(word.lower(), line.lower()):
        return True
    else:
        return False


def search_string(word_list):
    word_list = word_list.split()
    print(word_list)
    search_in_files = glob("*.h")
    result = dict()
    for a_file in search_in_files:
        with open(a_file) as search_in_file:
            for line in search_in_file:
                line = line.strip()
                for a_word in word_list:
                    if match_string(a_word, line):
                        if a_file not in result:
                            result[a_file ] = (a_word, line)
    return result

if __name__ == "__main__":
    print(search_string("int & char void"))
