#!/usr/bin/env python3

"""
Module for reading CSV-Files in a Matrix
"""

def read_csv(filename):
    """
    Reads data of a csv file, stores header in a list and content in a matrix
    """
    
    content = []

    with open(filename, encoding="utf-8-sig") as f:
        header = f.readline().split(",")
        
        # sometimes there is a trailing \n in the list
        # which needs to be removed       
        if header[-1][-1] == "\n":
            header_tmp = header[-1]
            header_tmp = header_tmp.rstrip("\n")
            header.pop()
            header.append(header_tmp)

    return header
