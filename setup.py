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
    name='tuttnauer-parser',
    version='0.0.1',
    description="Parse all TXT files in directory from Tuttnauer Elara11 Output to single CSV for analysis.",
    url='https://github.com/SLPeoples/Tuttnauer_Parser',
    author='Samuel L. Peoples',
    author_email='contact@lukepeoples.com',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Sterilizer Operators',
        'Topic :: Data Management',
        'License :: GPL',
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tuttnauer',
    packages=find_packages('Tuttnauer_Parser',exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'tuttnauer-parser=Tuttnauer_Parser.Tuttnauer_Parser:main',
        ],
    },
)