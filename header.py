#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Script description: TODO
"""

__author__ = 'Micha Wirth'
__version__ = '0.0.1'
__status__ 'Prototype'

def read_in(file_name):
  """Read in data from file."""
  with open(file_name, 'rt') as f:
    file_content = f.read()
  

def cli():
  """Command-line interface"""
  import argparse
  
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file',
                      default='file_name',
                      nargs='?',
                      type=str,
                      help="name of input file",
                     )
  args = parser.parse_args()
  return args.input_file

def main():
  file_name = cli()
  read_in(file_name)    
  return None
  
  
if __name__ == "__main__":
  # execute only if run as a script
  try:
    print("Start ...")
    while True:
        main()
  except KeyboardInterrupt:
    print("Bye ...")
