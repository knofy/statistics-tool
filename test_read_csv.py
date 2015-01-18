#!/usr/bin/env python3

"""
Testfile for module read_csv.py
"""

import unittest
import read_csv

# normal files with no conflicts
file1_normal = "testfiles/aapl.csv"
file2_normal = "testfiles/andr.csv"
file3_normal = "testfiles/ros.csv"
file4_normal = "testfiles/testdata.csv"

# corrupted files
file1_corrupt = "testfiles/aapl_header.csv"
file2_corrupt = "testfiles/andr_header.csv"
file3_corrupt = "testfiles/ros_header.csv"
file4_corrupt = "testfiles/testdata_header.csv"

class TestReadCsv(unittest.TestCase):
    """
    Testcase for various header-combinations
    """
    def setUp(self):
        self.header1 = ["Date","Open","High","Low","Close","Volume"]
        self.header1_check = ["Date","Opden","High","Low","Close","Volume"]
        self.header2_check = ["Date","Open","High","Low","Close","Vol"]
        self.header3_check = ["Date","Open","123","Low","Close","Volume"]
        self.header4_check = ["Date","Open","High","Lower","Close","Volume"]
    
    def test_normal(self):
        self.assertEqual(read_csv.read_csv(file1_normal), self.header1)
        self.assertEqual(read_csv.read_csv(file2_normal), self.header1)
        self.assertEqual(read_csv.read_csv(file3_normal), self.header1)
        self.assertEqual(read_csv.read_csv(file4_normal), self.header1)
        

    def test_corrupt(self):
        self.assertEqual(read_csv.read_csv(file1_corrupt), self.header1_check)
        self.assertEqual(read_csv.read_csv(file2_corrupt), self.header2_check)
        self.assertEqual(read_csv.read_csv(file3_corrupt), self.header3_check)
        self.assertEqual(read_csv.read_csv(file4_corrupt), self.header4_check)

if __name__ == "__main__":
    unittest.main()
