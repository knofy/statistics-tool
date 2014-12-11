#!/usr/bin/env python3

"""
Module for reading CSV-Files in a Matrix
"""

import sys
import argparse


def read_csv(filename):
    """
    Reads data of a csv file, stores header in a list and content in a matrix
    """
    content = []

    with open(filename, encoding="utf-8-sig") as f:
        header = f.readline().split(",")
        for line in f:
            temp = f.readline().split(",")
            temp_float = []
            for i in temp:
                try:
                    temp_float.append(float(i))
                except:
                    temp_float.append(i)
            content.append(temp_float)

    return header, content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    read_csv(args.filename)

    return 0

if __name__ == "__main__":
    sys.exit(main())
