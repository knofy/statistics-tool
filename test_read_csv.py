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
    
    def test_normal(self):
        self.assertEqual(read_csv.read_csv(file1_normal), self.header1)

if __name__ == "__main__":
    unittest.main()
