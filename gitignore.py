#!/usr/bin/env python3
import sys;


ignorefilePath="ignorefiles/"


def main():
	ignorefile = sys.argv[1]
	with open(ignorefilePath+ignorefile,"r") as file_out:
		print(file_out.read())



if __name__ == "__main__":
    main()
