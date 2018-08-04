**sample** Example project for a Python package

Provides an example project to develop Python packages from.

## Current status

### Design

This works with the Makefile.

The tests/ directory has files test_Test.py test_Test1.py and others.

The setup process for tests is in test_Test.py; it creates the object, loads and
sets up. test_Test1.py inherits from it.

You should use test_Test1.py to test the sub-components and test it with

 make UUT=test_Test1 check
 
And then use the sub-components in the main test with

 make check
 
The tests/ directory contains file to use in testing.

## Requirements

 * unidecode python module

## Installation

This works for Debian stretch. 

Create a Python3 Anaconda environment.

Install the package in dist/

 pip install dist/weaves-0.0.1.dev510.tar.gz

And thereafter, you can run

 make check

This should run the test files.
    
## Contributors

 * Walter Eaves

## License

[Gnu General Public License (GPL), Version 2 or later](https://www.gnu.org/licenses/gpl-2.0.html#SEC1)
