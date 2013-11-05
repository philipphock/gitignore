#!/usr/bin/env python3
import sys,os;


ignorefilePath=os.path.dirname(__file__)+os.sep+"ignorefiles"+os.sep

def main():
	ignorefile = sys.argv[1]
	with open(ignorefilePath+ignorefile,"r") as file_out:
		print(file_out.read())



if __name__ == "__main__":
    main()
