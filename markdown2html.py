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
        unordered_list_open = False
        ordered_list_open = False
        p_open = False
        for line_num in range(len(lines)):
            if lines[line_num].startswith('#'):
                h = lines[line_num].count('#', 0, 6)
                f.write('<h{}>{}</h{}>\n'.format(h, lines[line_num][h+1:].strip(), h))
            
            elif lines[line_num].startswith('-'):
                if not unordered_list_open:
                    f.write('<ul>\n')
                    unordered_list_open = True
                f.write('<li>{}</li>\n'.format(lines[line_num][2:].strip()))
                if ((line_num == len(lines) - 1) and unordered_list_open):
                    f.write('</ul>\n')
                    unordered_list_open = False
                elif (line_num != len(lines) - 1) and not lines[line_num + 1].startswith('-'):
                    f.write('</ul>\n')
                    unordered_list_open = False

            elif lines[line_num].startswith('*'):
                if not unordered_list_open:
                    f.write('<ol>\n')
                    unordered_list_open = True
                f.write('<li>{}</li>\n'.format(lines[line_num][2:].strip()))
                if ((line_num == len(lines) - 1) and unordered_list_open):
                    f.write('</ol>\n')
                    unordered_list_open = False
                elif (line_num != len(lines) - 1) and not lines[line_num + 1].startswith('*'):
                    f.write('</ol>\n')
                    unordered_list_open = False
                
            else:
                if not p_open and len(lines[line_num].strip()):
                    f.write('<p>\n')
                    p_open = True
                if len(lines[line_num].strip()):
                    f.write('{}\n'.format(lines[line_num].strip()))
                if ((line_num == len(lines) - 1) and p_open):
                    f.write('</p>\n')
                    p_open = False
                elif (line_num != len(lines) - 1) and p_open:
                    if len(lines[line_num + 1].strip()):
                        if lines[line_num + 1][0] in ['-', '*', '#']:
                            f.write('</p>\n')
                            p_open = False
                        else:
                            f.write('<br/>\n')
                    else:
                        f.write('</p>\n')
                        p_open = False
                