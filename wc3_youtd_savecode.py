#!/usr/bin/env python
#Python3
# coding: utf-8

import os
import re
import pyperclip

def main():
    fhand = open('C:\\...\\savecode.txt') # replace filepath with location of "savecode.txt"
    
    for line in fhand:
        if re.match('-load', line):
            pyperclip.copy(line)

    fhand.close()
    
if __name__ == '__main__':
    main() # calls main function from command line
