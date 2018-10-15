import sys,os

def readfile(fname):
    f = open(fname,'rb')
    for line in f:
        t = line
        if t.isdigtal:
            print('is a number')
        else:
            print(line)

