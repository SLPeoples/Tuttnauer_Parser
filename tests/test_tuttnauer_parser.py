#!/usr/bin/env python

__author__ = "Samuel Peoples"
__version__ = "1.0.0-dev"
__maintainer__ = "Samuel Peoples"
__email__ = "contact@lukepeoples.com"
__status__ = "Development"

import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))
import unittest
from warnings import catch_warnings
import tuttnauer_parser
import pandas as pd

"""
Tests for spatial_ornstein_uhlenbeck.py
"""


class Test_tuttnauer_parser(unittest.TestCase):

    def setUp(self):
        input = testdir+"/data/"
        output = "./"
        verbose = True

        self.df = tuttnauer_parser.parse_input(input, output, verbose)
    def tearDown(self):
        del self.df


    def test_serial_number(self):
        for serialNum in self.df.serialNum:
            assert serialNum == "88888888"


    def test_model_number(self):
        for modelNum in self.df.modelNum:
            assert modelNum == "BEST-MODEL"


    def test_software_version(self):
        for s in self.df.softwareVersion:
            assert s == "1.0.0"


    def test_cycle_number(self):
        for cycleNum in self.df.cycleNum:
            assert cycleNum == "000001" or "000002"


    def test_cycle_name(self):
        for cycleName in self.df.cycleName:
            assert cycleName == "WRAPPED INSTU" or "Bowie and Dick"

    def test_cycle_end(self):
        for cycleEnd in self.df.cycleEnd:
            assert cycleEnd == "Cycle Ended"

    def test_cycle_date(self):
        for cycleDate in self.df.cycleDate:
            assert cycleDate == "01/JAN/2018"

    def test_start_time(self):
        for startTime in self.df.startTime:
            assert startTime == "00:00:00"

    def test_end_time(self):
        for endTime in self.df.endTime:
            assert endTime == "00:00:00"


    def test_sterilizer_temp(self):
        for setSterTemp in self.df.setSterTemp:
            assert setSterTemp == "273.2"

    def test_sterilizer_time(self):
        for setSterTime in self.df.setSterTime:
            assert setSterTime == "5.0"

    def test_dry_time(self):
        for setDryTime in self.df.setDryTime:
            assert setDryTime == "20"

    def test_set_end_time(self):
        for setEndTemp in self.df.setEndTemp:
            assert setEndTemp == "248"

    def test_cycle_status(self):
        for cycleStatus in self.df.cycleStatus:
            assert cycleStatus == "A" or "H" or "S" or "E" or "D"

    def test_cycle_time(self):
        for cycleTime in self.df.cycleTime:
            assert cycleTime.startswith("00:00:")

    def test_cycle_temp(self):
        for cycleTemp in self.df.cycleTemp:
            assert cycleTemp == "001.0"

    def test_cycle_psi(self):
        for cyclePSI in self.df.cyclePSI:
            assert cyclePSI == "00.01"


if __name__ == '__main__':
    unittest.main()


