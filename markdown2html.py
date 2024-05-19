#!/usr/bin/python3
''' markdown2html.py - converts markdown to html '''

import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    with open(sys.argv[2], 'w') as f:
        unordered_list = []
        for line in lines:
            if line[0] == '#':
                h = line.count('#', 0, 6)
                f.write('<h{}>{}</h{}>\n'.format(h, line[h+1:].strip(), h))
            elif line[0] == '-':
                unordered_list.append(line[2:].strip())

        if unordered_list:
            f.write('<ul>\n')
            for item in unordered_list:
                f.write('<li>{}</li>\n'.format(item))
            f.write('</ul>\n')
            unordered_list = []
