#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Script description: TODO
"""

__author__ = 'Micha Wirth'
__copyright__ = 'Copyright 2019, xyz'
__version__ = '0.0.1'
__maintainer __ = 'Micha Wirth'
__status__ 'Prototype'

import argparse


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('input_file', type=str,help="name of input file")
  args = parser.parse_args()
  file_name = args.input_file
  with open(file_name, 'rt') as f:
    file_content = f.read()
  
  
if __name__ == "__main__":
  try:
    print("Start ...")
    while True:
        main()
  except KeyboardInterrupt:
    print("Bye ...")
