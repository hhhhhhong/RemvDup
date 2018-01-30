#!/usr/bin/python
import sys
import math

def main():
   a = raw_input().split(",")
   b = []
   for i in a:
      if i not in b:
	 b.append(i)
   print('%s'%(str(b))) 

if __name__=='__main__':
   main()
