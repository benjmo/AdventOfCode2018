#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      sum = 0
      for line in file:
         sum += int(line)
      print(sum)

if __name__ == "__main__":
    main()