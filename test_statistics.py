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
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "123")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_mean, file4_corrupt, "Volume")


class TestCalcStddev(unittest.TestCase):
    """
    Test for calc_stddev-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.calc_stddev(file1_normal, "Open"), 13.430457292229482)
        self.assertAlmostEqual(statistics.calc_stddev(file1_normal, "High"), 13.605159780083438)
        self.assertAlmostEqual(statistics.calc_stddev(file1_normal, "Low"), 13.194562787815293)
        self.assertAlmostEqual(statistics.calc_stddev(file1_normal, "Close"), 13.380800275020922)
        self.assertAlmostEqual(statistics.calc_stddev(file1_normal, "Volume"), 29234378.937317792)
        
        # file 2
        self.assertAlmostEqual(statistics.calc_stddev(file2_normal, "Open"), 2.167220451582126)
        self.assertAlmostEqual(statistics.calc_stddev(file2_normal, "High"), 2.204407501592106)
        self.assertAlmostEqual(statistics.calc_stddev(file2_normal, "Low"), 2.185713236173324)
        self.assertAlmostEqual(statistics.calc_stddev(file2_normal, "Close"), 2.2202661042019654)
        self.assertAlmostEqual(statistics.calc_stddev(file2_normal, "Volume"), 102257.20096860296)
        
        # file 3
        self.assertAlmostEqual(statistics.calc_stddev(file3_normal, "Open"), 3.5664204550418295)
        self.assertAlmostEqual(statistics.calc_stddev(file3_normal, "High"), 3.56881417078409)
        self.assertAlmostEqual(statistics.calc_stddev(file3_normal, "Low"), 3.498120984041589)
        self.assertAlmostEqual(statistics.calc_stddev(file3_normal, "Close"), 3.5981380959603273)
        self.assertAlmostEqual(statistics.calc_stddev(file3_normal, "Volume"), 2090.5043394843146)
        
        # file 4
        self.assertAlmostEqual(statistics.calc_stddev(file4_normal, "Open"), 0.799099141946747)
        self.assertAlmostEqual(statistics.calc_stddev(file4_normal, "High"), 0.815730196654949)
        self.assertAlmostEqual(statistics.calc_stddev(file4_normal, "Low"), 0.7930034705476317)
        self.assertAlmostEqual(statistics.calc_stddev(file4_normal, "Close"), 0.8105596097398405)
        self.assertAlmostEqual(statistics.calc_stddev(file4_normal, "Volume"), 3700.881365423863)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.calc_stddev, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.calc_stddev, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_stddev, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_stddev, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_stddev, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.calc_stddev, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_stddev, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_stddev, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_stddev, file2_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_stddev, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(KeyError, statistics.calc_stddev, file3_corrupt, "Open")
        self.assertRaises(KeyError, statistics.calc_stddev, file3_corrupt, "123")
        self.assertRaises(KeyError, statistics.calc_stddev, file3_corrupt, "Low")
        self.assertRaises(KeyError, statistics.calc_stddev, file3_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_stddev, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.calc_stddev, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_stddev, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_stddev, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.calc_stddev, file4_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_stddev, file4_corrupt, "Volume")


class TestCalcSum(unittest.TestCase):
    """
    Test for calc_sum-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.calc_sum(file1_normal, "Open"), 23372.260000000017)
        self.assertAlmostEqual(statistics.calc_sum(file1_normal, "High"), 23572.92999999999)
        self.assertAlmostEqual(statistics.calc_sum(file1_normal, "Low"), 23174.680000000004)
        self.assertAlmostEqual(statistics.calc_sum(file1_normal, "Close"), 23378.499999999993)
        self.assertAlmostEqual(statistics.calc_sum(file1_normal, "Volume"), 15551309782.0)
        
        # file 2
        self.assertAlmostEqual(statistics.calc_sum(file2_normal, "Open"), 10668.649999999992)
        self.assertAlmostEqual(statistics.calc_sum(file2_normal, "High"), 10753.739999999996)
        self.assertAlmostEqual(statistics.calc_sum(file2_normal, "Low"), 10552.350000000002)
        self.assertAlmostEqual(statistics.calc_sum(file2_normal, "Close"), 10651.889999999996)
        self.assertAlmostEqual(statistics.calc_sum(file2_normal, "Volume"), 36750239.0)
        
        # file 3
        self.assertAlmostEqual(statistics.calc_sum(file3_normal, "Open"), 16524.879999999997)
        self.assertAlmostEqual(statistics.calc_sum(file3_normal, "High"), 16675.15)
        self.assertAlmostEqual(statistics.calc_sum(file3_normal, "Low"), 16344.740000000002)
        self.assertAlmostEqual(statistics.calc_sum(file3_normal, "Close"), 16530.04)
        self.assertAlmostEqual(statistics.calc_sum(file3_normal, "Volume"), 510921.0)
        
        # file 4
        self.assertAlmostEqual(statistics.calc_sum(file4_normal, "Open"), 296.45000000000005)
        self.assertAlmostEqual(statistics.calc_sum(file4_normal, "High"), 297.6400000000001)
        self.assertAlmostEqual(statistics.calc_sum(file4_normal, "Low"), 295.8400000000001)
        self.assertAlmostEqual(statistics.calc_sum(file4_normal, "Close"), 297.1000000000001)
        self.assertAlmostEqual(statistics.calc_sum(file4_normal, "Volume"), 85621.0)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.calc_sum, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.calc_sum, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_sum, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_sum, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_sum, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.calc_sum, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_sum, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_sum, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_sum, file2_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_sum, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(TypeError, statistics.calc_sum, file3_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_sum, file3_corrupt, "123")
        self.assertRaises(TypeError, statistics.calc_sum, file3_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_sum, file3_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_sum, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.calc_sum, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_sum, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_sum, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.calc_sum, file4_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_sum, file4_corrupt, "Volume")
        

class TestCalcVariance(unittest.TestCase):
    """
    Test for calc_variance-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.calc_variance(file1_normal, "Open"), 180.37718307840007)
        self.assertAlmostEqual(statistics.calc_variance(file1_normal, "High"), 185.10037264160002)
        self.assertAlmostEqual(statistics.calc_variance(file1_normal, "Low"), 174.09648716160007)
        self.assertAlmostEqual(statistics.calc_variance(file1_normal, "Close"), 179.04581599999997)
        self.assertAlmostEqual(statistics.calc_variance(file1_normal, "Volume"), 854648911850690.1)
        
        # file 2
        self.assertAlmostEqual(statistics.calc_variance(file2_normal, "Open"), 4.696844485755833)
        self.assertAlmostEqual(statistics.calc_variance(file2_normal, "High"), 4.85941243307555)
        self.assertAlmostEqual(statistics.calc_variance(file2_normal, "Low"), 4.777342350783264)
        self.assertAlmostEqual(statistics.calc_variance(file2_normal, "Close"), 4.929581573468172)
        self.assertAlmostEqual(statistics.calc_variance(file2_normal, "Volume"), 10456535149.933256)
        
        # file 3
        self.assertAlmostEqual(statistics.calc_variance(file3_normal, "Open"), 12.71935486214077)
        self.assertAlmostEqual(statistics.calc_variance(file3_normal, "High"), 12.736434585589333)
        self.assertAlmostEqual(statistics.calc_variance(file3_normal, "Low"), 12.236850418992097)
        self.assertAlmostEqual(statistics.calc_variance(file3_normal, "Close"), 12.946597757601008)
        self.assertAlmostEqual(statistics.calc_variance(file3_normal, "Volume"), 4370208.393402751)
        
        # file 4
        self.assertAlmostEqual(statistics.calc_variance(file4_normal, "Open"), 0.6385594386600273)
        self.assertAlmostEqual(statistics.calc_variance(file4_normal, "High"), 0.6654157537347216)
        self.assertAlmostEqual(statistics.calc_variance(file4_normal, "Low"), 0.6288545043005885)
        self.assertAlmostEqual(statistics.calc_variance(file4_normal, "Close"), 0.6570068809416025)
        self.assertAlmostEqual(statistics.calc_variance(file4_normal, "Volume"), 13696522.880941596)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.calc_variance, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.calc_variance, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_variance, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_variance, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.calc_variance, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.calc_variance, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_variance, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_variance, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.calc_variance, file2_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_variance, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(KeyError, statistics.calc_variance, file3_corrupt, "Open")
        self.assertRaises(KeyError, statistics.calc_variance, file3_corrupt, "123")
        self.assertRaises(KeyError, statistics.calc_variance, file3_corrupt, "Low")
        self.assertRaises(KeyError, statistics.calc_variance, file3_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_variance, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.calc_variance, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.calc_variance, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.calc_variance, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.calc_variance, file4_corrupt, "Close")
        self.assertRaises(KeyError, statistics.calc_variance, file4_corrupt, "Volume")


class TestFindMax(unittest.TestCase):
    """
    Test for find_max-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.find_max(file1_normal, "Open"), 119.27)
        self.assertAlmostEqual(statistics.find_max(file1_normal, "High"), 119.75)
        self.assertAlmostEqual(statistics.find_max(file1_normal, "Low"), 118.05)
        self.assertAlmostEqual(statistics.find_max(file1_normal, "Close"), 119.0)
        self.assertAlmostEqual(statistics.find_max(file1_normal, "Volume"), 266833581.0)
        
        # file 2
        self.assertAlmostEqual(statistics.find_max(file2_normal, "Open"), 48.72)
        self.assertAlmostEqual(statistics.find_max(file2_normal, "High"), 48.74)
        self.assertAlmostEqual(statistics.find_max(file2_normal, "Low"), 48.2)
        self.assertAlmostEqual(statistics.find_max(file2_normal, "Close"), 48.63)
        self.assertAlmostEqual(statistics.find_max(file2_normal, "Volume"), 910079.0)
        
        # file 3
        self.assertAlmostEqual(statistics.find_max(file3_normal, "Open"), 76.7)
        self.assertAlmostEqual(statistics.find_max(file3_normal, "High"), 76.99)
        self.assertAlmostEqual(statistics.find_max(file3_normal, "Low"), 76.49)
        self.assertAlmostEqual(statistics.find_max(file3_normal, "Close"), 76.7)
        self.assertAlmostEqual(statistics.find_max(file3_normal, "Volume"), 15641.0)
        
        # file 4
        self.assertAlmostEqual(statistics.find_max(file4_normal, "Open"), 7.6)
        self.assertAlmostEqual(statistics.find_max(file4_normal, "High"), 7.6)
        self.assertAlmostEqual(statistics.find_max(file4_normal, "Low"), 7.6)
        self.assertAlmostEqual(statistics.find_max(file4_normal, "Close"), 7.6)
        self.assertAlmostEqual(statistics.find_max(file4_normal, "Volume"), 20506.0)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.find_max, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.find_max, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_max, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.find_max, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.find_max, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.find_max, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.find_max, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_max, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.find_max, file2_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_max, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(KeyError, statistics.find_max, file3_corrupt, "Open")
        self.assertRaises(KeyError, statistics.find_max, file3_corrupt, "123")
        self.assertRaises(KeyError, statistics.find_max, file3_corrupt, "Low")
        self.assertRaises(KeyError, statistics.find_max, file3_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_max, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.find_max, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.find_max, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_max, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.find_max, file4_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_max, file4_corrupt, "Volume")


class TestFindMin(unittest.TestCase):
    """
    Test for find_min-Function
    """
    def test_normal(self):
        # file 1
        self.assertAlmostEqual(statistics.find_min(file1_normal, "Open"), 70.74)
        self.assertAlmostEqual(statistics.find_min(file1_normal, "High"), 71.65)
        self.assertAlmostEqual(statistics.find_min(file1_normal, "Low"), 70.51)
        self.assertAlmostEqual(statistics.find_min(file1_normal, "Close"), 71.4)
        self.assertAlmostEqual(statistics.find_min(file1_normal, "Volume"), 14479611.0)
        
        # file 2
        self.assertAlmostEqual(statistics.find_min(file2_normal, "Open"), 36.91)
        self.assertAlmostEqual(statistics.find_min(file2_normal, "High"), 37.24)
        self.assertAlmostEqual(statistics.find_min(file2_normal, "Low"), 35.92)
        self.assertAlmostEqual(statistics.find_min(file2_normal, "Close"), 37.0)
        self.assertAlmostEqual(statistics.find_min(file2_normal, "Volume"), 41653.0)
        
        # file 3
        self.assertAlmostEqual(statistics.find_min(file3_normal, "Open"), 59.69)
        self.assertAlmostEqual(statistics.find_min(file3_normal, "High"), 60.0)
        self.assertAlmostEqual(statistics.find_min(file3_normal, "Low"), 59.0)
        self.assertAlmostEqual(statistics.find_min(file3_normal, "Close"), 59.68)
        self.assertAlmostEqual(statistics.find_min(file3_normal, "Volume"), 11.0)
        
        # file 4
        self.assertAlmostEqual(statistics.find_min(file4_normal, "Open"), 4.63)
        self.assertAlmostEqual(statistics.find_min(file4_normal, "High"), 4.63)
        self.assertAlmostEqual(statistics.find_min(file4_normal, "Low"), 4.63)
        self.assertAlmostEqual(statistics.find_min(file4_normal, "Close"), 4.63)
        self.assertAlmostEqual(statistics.find_min(file4_normal, "Volume"), 0.0)

    def test_corrupt(self):
        # file 1
        self.assertRaises(TypeError, statistics.find_min, file1_corrupt, "Opden")
        self.assertRaises(TypeError, statistics.find_min, file1_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_min, file1_corrupt, "Low")
        self.assertRaises(TypeError, statistics.find_min, file1_corrupt, "Close")
        self.assertRaises(TypeError, statistics.find_min, file1_corrupt, "Volume")
        
        # file 2
        self.assertRaises(TypeError, statistics.find_min, file2_corrupt, "Open")
        self.assertRaises(TypeError, statistics.find_min, file2_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_min, file2_corrupt, "Low")
        self.assertRaises(TypeError, statistics.find_min, file2_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_min, file2_corrupt, "Vol")
        
        # file 3
        self.assertRaises(KeyError, statistics.find_min, file3_corrupt, "Open")
        self.assertRaises(KeyError, statistics.find_min, file3_corrupt, "123")
        self.assertRaises(KeyError, statistics.find_min, file3_corrupt, "Low")
        self.assertRaises(KeyError, statistics.find_min, file3_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_min, file3_corrupt, "Volume")
        
        # file 4
        self.assertRaises(TypeError, statistics.find_min, file4_corrupt, "Open")
        self.assertRaises(TypeError, statistics.find_min, file4_corrupt, "High")
        self.assertRaises(TypeError, statistics.find_min, file4_corrupt, "Lower")
        self.assertRaises(TypeError, statistics.find_min, file4_corrupt, "Close")
        self.assertRaises(KeyError, statistics.find_min, file4_corrupt, "Volume")

if __name__ == "__main__":
    unittest.main()
