# Tuttnauer_Parser

[![Build Status](https://travis-ci.org/SLPeoples/Tuttnauer_Parser.svg?branch=master)](https://travis-ci.org/SLPeoples/Tuttnauer_Parser)

## t-parse

```
usage: t-parse [-h] -i INPUT [-o OUTPUT] [-v] [--version]

        Parse all TXT files in directory from Tuttnauer Elara11 Output to single CSV for analysis.


optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        PATH to TXT file directory
  -o OUTPUT, --output OUTPUT
                        PATH to output DIRECTORY. Default:
                        ./TXT/
  -v, --verbose         display verbose output while program runs.
                        Default:True
  --version             display version number and exit

        This script will read all TXT files in a directory and output their contents to a single, well-formatted 
	CSV for analysis in various software. The output TXT files are in a proprietary format which provide the 
	user with useful information when printed, but is not formatted well for analysis. The output CSV file 
	will be able to be used to better identify trends and potential issues during normal operation of the 
	Tuttnauer Elara11 Sterilizer.

        Example:         Tuttnauer_Parser.py

            -i --input {PATH to TXT file directory}

            [-o --output {PATH to OUTPUT DIRECTORY}]

```

1. Download/ clone the repository and navigate to the Tuttnauer_Parser directory.

2. Execute:

    ```python setup.py install```
	
3. Navigate to the directory containing your data files. In this instance, the TXT directory is in 
the current working directory.

4. Execute:

    ```t-parse```
	
5. Output file will be saved to the current directory.

![Image](https://i.imgur.com/enzkBV5.png)
