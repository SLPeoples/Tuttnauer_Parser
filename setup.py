"""A setuptools based setup module.
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='t-parse',
    version='0.0.1',
    description="This script will read all TXT files in a directory and output their contents to a single, well-formatted CSV for "
                "analysis in various software. The output TXT files are in a proprietary format which provide the user with "
                "useful information when printed, but is not formatted well for analysis. The output CSV file will be able to be"
                "used to better identify trends and potential issues during normal operation of the Tuttnauer Elara11 Sterilizer. ",
    url='https://github.com/slpeoples/Tuttnauer_Parser',
    author='Samuel Peoples',
    author_email='contact@lukepeoples.com',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Elara11 Operators',
        'License :: GPL',
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tuttnauer elara',
    packages=find_packages('parser', exclude=['tests']),
    py_modules=["tuttnauer_parser"],
    install_requires=[],

    entry_points={
        'console_scripts': [
            't-parse=parser.tuttnauer_parser:main',
        ],
    },
)