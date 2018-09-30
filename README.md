# Tuttnauer_Parser

[![Build Status](https://travis-ci.org/SLPeoples/Tuttnauer_Parser.svg?branch=master)](https://travis-ci.org/SLPeoples/Tuttnauer_Parser)

[Tableau Dashboard of Parsed Data](https://public.tableau.com/profile/samuel.l.peoples#!/vizhome/TuttnauerParser/TuttnauerParser)

<div class='tableauPlaceholder' id='viz1538270442536' style='position: relative'><noscript><a href='#'><img alt='Tuttnauer Parser ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tu&#47;TuttnauerParser&#47;TuttnauerParser&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TuttnauerParser&#47;TuttnauerParser' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tu&#47;TuttnauerParser&#47;TuttnauerParser&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1538270442536');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1100px';vizElement.style.height='827px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

## t-parse

```
usage: t-parse [-h] -i INPUT [-o OUTPUT] [-v] [--version]

        Parse all TXT files in directory from Tuttnauer Elara11 Output to single CSV for analysis.


optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        PATH to TXT file directory
			Default: ./
  -o OUTPUT, --output OUTPUT
                        PATH to output DIRECTORY. 
			Default: ./TXT/
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
