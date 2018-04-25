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

    # Optional parameters
    parser.add_argument('-i', '--input', type=str, default="./TXT/", \
                        help='PATH to TXT file directory')
    
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
    """ Parses the input directory, saves to output directory
    :param input: txt file directory
    :param output: output directory for combined dataset
    :return: dataframe for testing
    
    Example file:


    ------------------------
    ------------------------
    Date: 01/JAN/2017
    Time: 16:23:33
    Ser. Num: 00000000
    Model: ELARA11
    Version: 1
    Software vers.: 2.0.3.98
    Cycle Num: 000100
    WRAPPED INSTU
    (Customized)
    Ster. Temp. 273.2 *F
    Ster. Time 5.0 min*
    Dry Time 20 min
    End Temperature 248 °F
      Time     °F    Psig
    A 00:00:07 138.2 00.55
    A 00:00:08 138.4 00.55
    A 00:03:08 149.0 24.78In
    A 00:03:52 150.4 25.90In
    A 00:05:04 220.6 05.99
    A 00:05:05 221.2 06.19
    A 00:08:05 149.0 22.94In
    A 00:08:59 143.8 24.04In
    A 00:09:51 224.1 06.28
    A 00:09:52 224.1 06.28
    A 00:12:52 158.5 20.08In
    A 00:15:38 140.5 23.62In
    A 00:16:27 222.3 06.25
    H 00:16:28 222.3 06.25
    H 00:19:28 231.6 07.67
    H 00:22:28 264.7 24.21
    H 00:25:28 269.2 27.06
    H 00:26:14 275.2 31.31
    CLK 1: 16:49:48
    CLK 2: 16:49:48
    S 00:26:16 275.4 31.50
    S 00:27:16 275.9 31.07
    S 00:28:16 275.7 30.88
    S 00:29:16 275.9 30.88
    S 00:30:16 275.9 31.08
    S 00:31:16 275.9 31.05
    S 00:31:16 275.9 31.05
    CLK 1: 16:54:49
    CLK 2: 16:54:48
    E 00:31:18 276.1 31.02
    E 00:32:35 228.4 00.65
    D 00:32:41 220.8 02.16In
    D 00:35:41 202.8 22.86In
    D 00:38:41 190.4 19.70In
    D 00:41:41 184.1 19.61In
    D 00:44:41 183.4 22.77In
    D 00:47:41 183.2 21.65In
    D 00:50:41 183.2 21.73In
    D 00:52:43 183.0 21.38In
      00:52:50 184.1 13.94In
      00:53:11 189.5 00.97In
    Status: Cycle Ended
    Time: 17:16:44
    Operator: ____________
    ------------------------
    ------------------------


    """
    
    # Create an array for each column
    cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, softwareVersion, setSterTemp, setSterTime, \
    setDryTime, setEndTemp, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleEnd = ([] for i in range(17))
    
    # Open each file and add the contents to the column arrays
    for file in os.listdir(input):
        f = open(input + file, 'rb')
        content = f.readlines()
        contents = []
        i = 0
        # Ignore the first four lines
        for line in content:
            if i < 4:
                pass
            else:
                contents.append(str(line))
            i += 1
        
        # The formatting is affected by the Cycle Name, which varies between one and two lines.
        # Check if Ster. Temp is at position 8, or 9, and process the rows accordingly.
        if contents[8].startswith("Ster. Temp."):
            i = 13
            # Collect the cycle time, temperature, pressure data, these lines always begin with A, H, S, E, or D.
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
            # Collect the cycle time, temperature, pressure data, these lines always begin with A, H, S, E, or D.
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

    # Create the dataframe using the column names
    d = {'cycleNum': cycleNum, 'cycleName': cycleName, 'cycleDate': cycleDate, 'startTime': startTime,
         'endTime': endTime,
         'serialNum': serialNum, 'modelNum': modelNum, 'softwareVersion': softwareVersion, 'setSterTemp': setSterTemp,
         'setSterTime': setSterTime, 'setDryTime': setDryTime, 'setEndTemp': setEndTemp, 'cycleStatus': cycleStatus,
         'cycleTime': cycleTime, 'cycleTemp': cycleTemp, 'cyclePSI': cyclePSI, 'cycleEnd': cycleEnd}
    df = pd.DataFrame(data=d)
    
    # Reindex the dataframe explicitly to have appropriate output formatting
    df = df.reindex_axis(['serialNum', 'modelNum', 'softwareVersion',
                          'cycleNum', 'cycleName', 'cycleEnd', 'cycleDate', 'startTime', 'endTime',
                          'setSterTemp', 'setSterTime', 'setDryTime', 'setEndTemp', 'cycleStatus',
                          'cycleTime', 'cycleTemp', 'cyclePSI'], axis=1)
    df.to_csv(output + "combined_history.csv", index=False)
    return df


def append_rows_8(i, contents, cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum,
                  softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus,
                  cycleTime, cycleTemp, cyclePSI, cycleEnd):
    cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum, softwareVersion, cycleNum,\
    cycleName, endTime, cycleEnd \
        = append_rows(i, contents, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum,
                    modelNum, softwareVersion, cycleNum, cycleName, endTime, cycleEnd)
    
    # Ster. Temp. 273.2 °F --> 273.2 
    setSterTemp.append(contents[8].replace("Ster. Temp. ", "").split(" ")[0])
    # Ster. Time 5.0 min* --> 5.0
    setSterTime.append(contents[9].replace("Ster. Time ", "").split(" ")[0])
    # Dry Time 20 min --> 20
    setDryTime.append(contents[10].replace("Dry Time ", "").split(" ")[0])
    # End Temperature 248 °F --> 248
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

    # Ster. Temp. 273.2 °F --> 273.2 
    setSterTemp.append(contents[9].replace("Ster. Temp. ", "").split(" ")[0])
    # Ster. Time 5.0 min* --> 5.0
    setSterTime.append(contents[10].replace("Ster. Time ", "").split(" ")[0])
    # Dry Time 20 min --> 20
    setDryTime.append(contents[11].replace("Dry Time ", "").split(" ")[0])
    # End Temperature 248 °F --> 248
    setEndTemp.append(contents[12].replace("End Temperature ", "").split(" ")[0])

    return cycleNum, cycleName, cycleDate, startTime, endTime, serialNum, modelNum, \
           softwareVersion, setSterTemp, setSterTime, setDryTime, setEndTemp, cycleStatus, \
           cycleTime, cycleTemp, cyclePSI, cycleEnd

def append_rows(i, contents, cycleStatus, cycleTime, cycleTemp, cyclePSI, cycleDate, startTime, serialNum, modelNum,
                softwareVersion, cycleNum, cycleName, endTime, cycleEnd):
    # A 00:00:07 138.2 00.55In --> [A, 00:00:07, 138.2, 00.55In]
    temp = contents[i].split(" ")
    # A
    cycleStatus.append(temp[0])
    # 00:00:07
    cycleTime.append(temp[1])
    # 138.2
    cycleTemp.append(temp[2])
    # 00.55In --> 00.55
    cyclePSI.append(temp[3].replace("In", "").replace("\n", ""))
    # Date: 21/NOV/2017 --> 21/NOV/2017
    cycleDate.append(contents[0].replace("Date: ", "").replace("\n", ""))
    # Time: 16:23:33 --> 16:23:33
    startTime.append(contents[1].replace("Time: ", "").replace("\n", ""))
    # Ser. Num: 00000000 --> 00000000
    serialNum.append(contents[2].replace("Ser. Num: ", "").replace("\n", ""))
    # Model: ELARA11 --> ELARA11
    modelNum.append(contents[3].replace("Model: ", "").replace("\n", ""))
    # Version: 1 --> 1
    softwareVersion.append(contents[5].replace("Software vers.: ", "").replace("\n", ""))
    # Cycle Num: 000100 --> 000100
    cycleNum.append(contents[6].replace("Cycle Num: ", "").replace("\n", ""))
    # WRAPPED INSTU
    cycleName.append(contents[7].replace("\n", ""))
    # Time: 17:16:44 --> 17:16:44
    endTime.append(contents[-6].replace("Time: ", "").replace("\n", ""))
    # Status: Cycle Ended -- > Cycle Ended
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
        print("\t output:" +output +"combined_history.csv")

    parse_input(input, output, verbose)


if __name__ == "__main__":
    main()
