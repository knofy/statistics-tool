#!/usr/bin/env python3

"""
Testfile for module statistics.py
"""

import unittest
import statistics

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

class TestCount(unittest.TestCase):
    """
    Test for items-Function
    """
    def test_normal(self):
        self.assertEqual(statistics.count(file1_normal), 250)
        self.assertEqual(statistics.count(file2_normal), 246)
        self.assertEqual(statistics.count(file3_normal), 245)
        self.assertEqual(statistics.count(file4_normal), 47)

class TestCalcMean(unittest.TestCase):
    """
    Test for calc_mean-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.calc_mean(file1_normal, "Open"), 93.48904000000006)
        self.assertAlmostEqual(statistics.calc_mean(file1_normal, "High"), 94.29171999999996)
        self.assertAlmostEqual(statistics.calc_mean(file1_normal, "Low"), 92.69872000000001)
        self.assertAlmostEqual(statistics.calc_mean(file1_normal, "Close"), 93.51399999999997)
        self.assertAlmostEqual(statistics.calc_mean(file1_normal, "Volume"), 62205239.128)
        
        # file 2
        self.assertAlmostEqual(statistics.calc_mean(file2_normal, "Open"), 43.36849593495932)
        self.assertAlmostEqual(statistics.calc_mean(file2_normal, "High"), 43.71439024390242)
        self.assertAlmostEqual(statistics.calc_mean(file2_normal, "Low"), 42.89573170731708)
        self.assertAlmostEqual(statistics.calc_mean(file2_normal, "Close"), 43.30036585365852)
        self.assertAlmostEqual(statistics.calc_mean(file2_normal, "Volume"), 149391.21544715448)
        
        # file 3
        self.assertAlmostEqual(statistics.calc_mean(file3_normal, "Open"), 67.44848979591836)
        self.assertAlmostEqual(statistics.calc_mean(file3_normal, "High"), 68.06183673469388)
        self.assertAlmostEqual(statistics.calc_mean(file3_normal, "Low"), 66.71322448979592)
        self.assertAlmostEqual(statistics.calc_mean(file3_normal, "Close"), 67.46955102040816)
        self.assertAlmostEqual(statistics.calc_mean(file3_normal, "Volume"), 2085.3918367346937)
        
        # file 4
        self.assertAlmostEqual(statistics.calc_mean(file4_normal, "Open"), 6.307446808510639)
        self.assertAlmostEqual(statistics.calc_mean(file4_normal, "High"), 6.332765957446811)
        self.assertAlmostEqual(statistics.calc_mean(file4_normal, "Low"), 6.294468085106385)
        self.assertAlmostEqual(statistics.calc_mean(file4_normal, "Close"), 6.321276595744682)
        self.assertAlmostEqual(statistics.calc_mean(file4_normal, "Volume"), 1821.723404255319)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Volume")
        
        # file 3
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Volume")
        

if __name__ == "__main__":
    unittest.main()
