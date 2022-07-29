#!/usr/bin/env python3
import re
import sys


class Formatter:
    # control sequences
    line_comment = re.compile(r'(^|\s*)\/\/.*$')

    # indentation
    ilvl = 0
    iwidth = 0

    def __init__(self, indentwidth):
        self.iwidth = indentwidth

    def multiple_semicolon(self, line, semicolon):
        result = self.indent() + line[0:semicolon[0].span()[1]]
        for i in range(0,len(semicolon)-1):
            result += '\n' + self.indent() +  line[semicolon[i].span()[1]:semicolon[i+1].span()[1]].strip()
        return(0,  result)

    # compute indentation
    def indent(self, add=0):
        if self.iwidth == 0 :
            self.iwidth = 1
        return (self.ilvl)*self.iwidth*' '

    def formatLine(self, line):
        line = line.strip()
        # determine if line is a line comment 
        if re.match(self.line_comment, line):
            return (0, self.indent() + line.strip())

        # find if there " or ' in line
        string_in_line = [m for m in re.findall(r'\"|\'',line)]

        # if " or ' just indent line 
        if len(string_in_line) > 0 :
            return (0, self.indent() + line.strip())
        
        semicolon = [m for m in re.finditer(";",line)]
        open_parenthesis = [m for m in re.finditer("{",line)]
        close_parenthesis = [m for m in re.finditer("}",line)]

        # format if one or multiple { in line 
        if len(open_parenthesis) > 0 :
            result = self.indent() + line[0:open_parenthesis[0].span()[1]]
            self.ilvl +=4
            for i in range(0,len(open_parenthesis)-1):
                result += self.indent() + line[open_parenthesis[i].span()[1]:open_parenthesis[i+1].span()[1]].strip()
                self.ilvl +=4
            return(0, result)
            
        # format if one or multiple } in line
        if len(close_parenthesis)>0 : 
            self.ilvl -= 4
            result = self.indent() + line[0:close_parenthesis[0].span()[1]]
            for i in range(0,len(close_parenthesis)-1):
                self.ilvl -= 4
                result += '\n' + self.indent() + line[close_parenthesis[i].span()[1]:close_parenthesis[i+1].span()[1]].strip()
            return(0, result) 

        # format if multiple ; in line 
        if len(semicolon) > 1 : 
            f = [m for m in re.findall(r'\s*for\s*\(',line)]
            if len(f) < 1 : 
                return self.multiple_semicolon(line, semicolon)
        
        # if no special caraters just indent
        return (0, self.indent() + line.strip())
        


    # format file from line 'start' to line 'end'
    def formatFile(self, filename, start, end):
        # read lines from file
        wlines = rlines = []

        if filename == '-':
            with sys.stdin as f:
                rlines = f.readlines()[start-1:end]
        else:
            with open(filename, 'r', encoding='UTF-8') as f:
                rlines = f.readlines()[start-1:end]

        # take care of empty input
        if not rlines:
            rlines = ['']

        # get initial indent lvl
        self.ilvl = 0

        blank = True
        for line in rlines:
            # format line
            (offset, line) = self.formatLine(line)
            # add line to result
            wlines.append(line)

        # remove last line if blank
        while wlines and not wlines[-1]:
            wlines.pop()

        # take care of empty output
        if not wlines:
            wlines = ['']

        # write output
        for line in wlines:
            print(line)


def main():
    options = dict(startLine=1, endLine=None, indentWidth=4)
    if len(sys.argv) < 2:
        print('Missing arguments', file=sys.stderr)

    else:
        for arg in sys.argv[2:]:
            key, value = arg.split('=')
            if any(char.isdigit() for char in value):
                value = int(value)
            options[key.strip()] = value

        indent = options['--indentWidth']
        start = options['--startLine']
        end = options['--endLine']

        formatter = Formatter(indent)
        formatter.formatFile(sys.argv[1], start, end)


if __name__ == '__main__':
    main()