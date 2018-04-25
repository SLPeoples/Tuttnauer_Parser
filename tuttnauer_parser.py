#!/usr/bin/env python
from __future__ import division
import pandas as pd
import os

__author__ = "Samuel L. Peoples"
__version__ = "0.0.1"
__email__ = "contact@lukepeoples.com"
__status__ = "Development"

from argparse import ArgumentParser, RawDescriptionHelpFormatter, FileType


# Documentation can be found here:https://docs.python.org/2/library/argparse.html#module-argparse

def make_commandline_interface():
    """Returns a parser for the commandline"""
    short_description = \
        """
        Parse all TXT files in directory from Tuttnauer Elara11 Output to single CSV for analysis.
        """

    long_description = \
        """
        This script will read all TXT files in a directory and output their contents to a single, well-formatted CSV for 
        analysis in various software. The output TXT files are in a proprietary format which provide the user with 
        useful information when printed, but is not formatted well for analysis. The output CSV file will be able to be
        used to better identify trends and potential issues during normal operation of the Tuttnauer Elara11 Sterilizer. 
        
        Example: \t Tuttnauer_Parser.py  \n\t\t
            -i --input {PATH to TXT file directory} \n\t\t
            [-o --output {PATH to OUTPUT DIRECTORY}] \n\t\t
        """

    parser = ArgumentParser(description=short_description, \
                            epilog=long_description, formatter_class=RawDescriptionHelpFormatter)

    # Required parameters
    parser.add_argument('-i', '--input', type=str, default="./TXT/", \
                        help='PATH to TXT file directory')

    # Optional parameters
    parser.add_argument('-o', '--output', type=str, default='./',
                        help='PATH to output DIRECTORY. Default: .~\[feature]_network_analysis.txt')

    # Example of a 'flag option' that sets a variable to true if provided
    parser.add_argument('-v', '--verbose', default=True, action='store_true', \
                        help="display verbose output while program runs. Default:%(default)s")

    # Add version information (from the __version__ string defined at top of script
    parser.add_argument('--version', action='version', version=__version__, \
                        help="display version number and exit")
    return parser


def parse_input(input, output, verbose):
    """
    Parses the input directory, saves to output directory
    :param input:
    :param output:
    :return:
    """
    cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, softwareVersion, setSterTemp, setSterTime, \
    setDryTime, setEndTemp, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleEnd = ([] for i in range(17))

    for file in os.listdir(input):
        f = open(input + file, 'r')
        content = f.readlines()
        contents = []
        i = 0
        for line in content:
            if i < 4:
                pass
            else:
                contents.append(line)
            i += 1

        if contents[8].startswith("Ster. Temp."):
            i = 13
            while not contents[i].startswith("Status: "):
                if contents[i].startswith("A") or \
                        contents[i].startswith("H") or \
                        contents[i].startswith("S") or \
                        contents[i].startswith("E") or \
                        contents[i].startswith("D"):
                    cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, \
                    softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus, \
                    cycleTime, cycleTemp, cyclePSI, cycleEnd \
                        = append_rows_8(i, contents, cycleNum, cycleName, cycleDate, startTime, endTime,
                                        serialNum, modelNum, softwareVersion, setSterTemp, setSterTime,
                                        setDryTime, setEndTemp, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleEnd)
                i += 1

        elif contents[9].startswith("Ster. Temp."):
            i = 14
            while not contents[i].startswith("Status: "):
                if contents[i].startswith("A") or \
                        contents[i].startswith("H") or \
                        contents[i].startswith("S") or \
                        contents[i].startswith("E") or \
                        contents[i].startswith("D"):
                    cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, \
                    softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus, \
                    cycleTime, cycleTemp, cyclePSI, cycleEnd \
                        = append_rows_9(i, contents, cycleNum, cycleName, cycleDate, startTime, endTime,
                                        serialNum, modelNum, softwareVersion, setSterTemp, setSterTime,
                                        setDryTime, setEndTemp, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleEnd)

                i += 1

    d = {'cycleNum': cycleNum, 'cycleName': cycleName, 'cycleDate': cycleDate, 'startTime': startTime,
         'endTime': endTime,
         'serialNum': serialNum, 'modelNum': modelNum, 'softwareVersion': softwareVersion, 'setSterTemp': setSterTemp,
         'setSterTime': setSterTime, 'setDryTime': setDryTime, 'setEndTemp': setEndTemp, 'cycleStatus': cycleStatus,
         'cycleTime': cycleTime, 'cycleTemp': cycleTemp, 'cyclePSI': cyclePSI, 'cycleEnd': cycleEnd}
    df = pd.DataFrame(data=d)
    df = df.reindex_axis(['serialNum', 'modelNum', 'softwareVersion',
                          'cycleNum', 'cycleName', 'cycleEnd', 'cycleDate', 'startTime', 'endTime',
                          'setSterTemp', 'setSterTime', 'setDryTime', 'setEndTemp', 'cycleStatus',
                          'cycleTime', 'cycleTemp', 'cyclePSI'], axis=1)
    df.to_csv(output + os.getcwd().split("\\")[-1]+".csv", index=False)
    return df


def append_rows_8(i, contents, cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum,
                  softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus,
                  cycleTime, cycleTemp, cyclePSI, cycleEnd):

    cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum, softwareVersion, cycleNum,\
    cycleName, endTime, cycleEnd \
        = append_rows(i, contents, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum,
                    modelNum, softwareVersion, cycleNum, cycleName, endTime, cycleEnd)

    setSterTemp.append(contents[8].replace("Ster. Temp. ", "").split(" ")[0])
    setSterTime.append(contents[9].replace("Ster. Time ", "").split(" ")[0])
    setDryTime.append(contents[10].replace("Dry Time ", "").split(" ")[0])
    setEndTemp.append(contents[11].replace("End Temperature ", "").split(" ")[0])

    return cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, \
           softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus, \
           cycleTime, cycleTemp, cyclePSI, cycleEnd


def append_rows_9(i, contents, cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum,
                  softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus,
                  cycleTime, cycleTemp, cyclePSI, cycleEnd):

    cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum, softwareVersion, cycleNum,\
    cycleName, endTime, cycleEnd \
        = append_rows(i, contents, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum,
                    modelNum, softwareVersion, cycleNum, cycleName, endTime, cycleEnd)

    setSterTemp.append(contents[9].replace("Ster. Temp. ", "").split(" ")[0])
    setSterTime.append(contents[10].replace("Ster. Time ", "").split(" ")[0])
    setDryTime.append(contents[11].replace("Dry Time ", "").split(" ")[0])
    setEndTemp.append(contents[12].replace("End Temperature ", "").split(" ")[0])

    return cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, \
           softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus, \
           cycleTime, cycleTemp, cyclePSI, cycleEnd

def append_rows(i, contents, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum,
                softwareVersion, cycleNum, cycleName, endTime, cycleEnd):

    temp = contents[i].split(" ")
    cycleStatus.append(temp[0])
    cycleTime.append(temp[1])
    cycleTemp.append(temp[2])
    cyclePSI.append(temp[3].replace("In", "").replace("\n", ""))
    cycleDate.append(contents[0].replace("Date: ", "").replace("\n", ""))
    startTime.append(contents[1].replace("Time: ", "").replace("\n", ""))
    serialNum.append(contents[2].replace("Ser. Num: ", "").replace("\n", ""))
    modelNum.append(contents[3].replace("Model: ", "").replace("\n", ""))
    softwareVersion.append(contents[5].replace("Software vers.: ", "").replace("\n", ""))
    cycleNum.append(contents[6].replace("Cycle Num: ", "").replace("\n", ""))
    cycleName.append(contents[7].replace("\n", ""))
    endTime.append(contents[-6].replace("Time: ", "").replace("\n", ""))
    cycleEnd.append(contents[-7].replace("Status: ", "").replace("\n", ""))

    return cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum, softwareVersion, \
           cycleNum, cycleName, endTime, cycleEnd


def main():
    """Main function"""
    parser = make_commandline_interface()
    args = parser.parse_args()

    input = args.input
    if not os.path.isdir(input):
        print(input + " not found. Please verify location.")
        exit(0)

    output = args.output
    if not os.path.isdir(output):
        print(output + " not found. Please verify location.")
        exit(0)

    verbose = args.verbose
    if verbose:
        print("tuttnauer_parser.py")
        print("\t input:", input)
        print("\t output:" +output +os.getcwd().split("\\")[-1]+".csv")

    parse_input(input, output, verbose)


if __name__ == "__main__":
    main()
