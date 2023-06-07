#!/usr/bin/python3
def uppercase(str):
    strtmp = ""
    for c in str:
        if ord(c) > 65 and ord(c) < 91:
            strtmp += chr(ord(c)-32)
        else:
            strtmp += c
    print("{}".format(strtmp))
