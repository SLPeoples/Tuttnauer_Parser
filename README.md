This script will read all TXT files in a directory and output their contents to a single, well-formatted CSV for 
analysis in various software. The output TXT files are in a proprietary format which provide the user with 
useful information when printed, but is not formatted well for analysis. The output CSV file will be able to be
used to better identify trends and potential issues during normal operation of the Tuttnauer Elara11 Sterilizer. 

usage:

1. Download the repository and navigate to the Tuttnauer_Parser directory.

2. Execute:

    python setup.py install
	
3. Navigate to the directory containing your data files. In this instance, the format is:
  
    Date1-Date2 ---CYC
                \
				 ---TXT

4. Execute:

    tuttnauer-parser -i ./TXT/ -o ./
	
5. Output file will be saved to the current directory.
  
    Date1-Date2 ---CYC
                \
				 ---TXT
                 \
                  ---tuttnauer_combined.csv 