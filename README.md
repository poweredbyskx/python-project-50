### Hexlet tests and linter status:
[![Actions Status](https://github.com/poweredbyskx/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/poweredbyskx/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/cf668b92207cab79d8a1/maintainability)](https://codeclimate.com/github/poweredbyskx/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/cf668b92207cab79d8a1/test_coverage)](https://codeclimate.com/github/poweredbyskx/python-project-50/test_coverage)
# Gendiff
*Educational project*

An application for finding the difference in 2 files of json, yaml, yaml formats and displaying the result in several variants

## Installation
1. Requires Python version 3.12 or higher and Poetry
2. Clone the project: `>> git clone git@github.com:poweredbyskx/python-project-50.git`
3. Install the project: `>> make install`
4. Build the project: `>> make build`
5. Install the package: `>> make package-install`

### Usage and Options:
To use it just type `gendiff [-h] [-f FORMAT] <path_to_file_1> <path_to_file_2>`

* -h, --help - show help message.
* -f, --format - ability to specify format selection. Formats are available:
  * `stylish` - displaying differences in the form of a tree
  * `plain` - displaying differences line by line
  * `json` - output in json format

The command for the example: `gendiff example/file1.json example/file2.json`
