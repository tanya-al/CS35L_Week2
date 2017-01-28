#!/usr/bin/python

import random, sys
from optparse import OptionParser

class comm:
    def __init__(self, file1, file2):
        if(file1 == "-"):
            self.lines1 = sys.stdin.readlines()
        else:
            f1 = open(file1, 'r')
            self.lines1 = f1.readlines()
            f1.close()
        if(file2 == "-"):
            self.lines2 = sys.stdin.readlines()
        else:
            f2 = open(file2, 'r')
            self.lines2 = f2.readlines()
            f2.close()
    
def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2

Output differences between FILE1 and FILE2."""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-1",
                      action="store_true", dest="sup1", default=False,
                      help="output the 2nd and 3rd columns")
    parser.add_option("-2",
                      action="store_true", dest="sup2", default=False,
                      help="output the 1st and 3rd columns")
    parser.add_option("-3",
                      action="store_true", dest="sup3", default=False,
                      help="output the 1st and  2nd columns")
    parser.add_option("-u",
                      action="store_true", dest="sort", default=False,
                      help="sort files 1 and 2 before comparing them")
    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:
        parser.error("wrong number of operands")
    input_file1 = args[0]
    input_file2 = args[1]
    col = []

    try:
        compare = comm(input_file1, input_file2)
    except:
        sys.stdout.write("Cannot read files")
    try:
        if(options.sort):
            for line1 in compare.lines1:
                for line2 in compare.lines2:
                    if(line1 == line2):
                        col.append((line1, 3))
                        break
                if((line1, 3) not in col):
                    col.append((line1, 1))
            for line in compare.lines2:
                if((line, 3) not in col):
                    col.append((line, 2))
    except:
        sys.stdout.write("Failed to sort")
    try:
        if(options.sort == False):
            for line1 in compare.lines1:
                for line2 in compare.lines2:
                    if(line1 == line2):
                        col.append((line1, 3))
                        break
                    elif(line1 < line2):
                        col.append((line1, 1))
                        break
                    elif((line2, 3) not in col and (line2, 2) not in col):
                        col.append((line2, 2))
            for line in compare.lines1:
                if((line, 3) not in col and (line, 1) not in col):
                    col.append((line,1))
            for line in compare.lines2:
                if((line, 3) not in col and (line, 2) not in col):
                    col.append((line, 2))
    except:
        sys.stdout.write("Lines not read correctly")
                    
    if(options.sup1):#if -1 is used
        if(options.sup2):
            if(options.sup3 == False):#-12
                for element in col:
                    if(element[1]==3):
                        sys.stdout.write(element[0])
        elif(options.sup3):#-13
            for element in col:
                if(element[1]==2):
                    sys.stdout.write(element[0])
        else:#-1
            for element in col:
                if(element[1]==2):
                    sys.stdout.write(element[0])
                elif(element[1]==3):
                    sys.stdout.write("\t"+element[0])
    elif(options.sup2):#if -2 and not -1 is used
        for element in col:
            if(element[1]==1):#-23
                sys.stdout.write(element[0])
            elif(element[1]==3 and options.sup3 == False):#-2
                sys.stdout.write("\t"+element[0])
    elif(options.sup3):#if -3 and neither -1 nor -2 are used
        for element in col:
            if(element[1]==1):
                sys.stdout.write(element[0])
            elif(element[1]==2):
                sys.stdout.write("\t"+element[0])
    else:#no supression
        for element in col:
            if(element[1]==1):
                sys.stdout.write(element[0])
            elif(element[1]==2):
                sys.stdout.write("\t"+element[0])
            else:
                sys.stdout.write("\t\t"+element[0])

if __name__ == "__main__":
    main()
