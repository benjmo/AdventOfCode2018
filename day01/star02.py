#!/usr/bin/python3

import re

def main():
   with open("./input.txt", 'r') as file:
      lines = file.readlines()
   sum = 0;
   pastSums = {0}
   while True:
      for line in lines:
         sum += int(line)
         if (sum in pastSums):
            print(sum)
            return
         pastSums.add(sum)

if __name__ == "__main__":
    main()