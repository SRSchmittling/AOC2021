#   DAY04.py
#   Written by Selene R. Schmittling
#   December 3, 2021

#   Import Statements
import pandas as pd

#   Global vars
LOGGING = True

#   Utility Functions
def getdata(ifile):
    indata = pd.read_csv(ifile, sep=" ", header=False)
    # Add code to process data

def part1(data, logf):
    if LOGGING:
        logf.writelines("PART 1\n ********************\n\n")
    print("In part 1")

def part2(data, logf):
    if LOGGING:
        logf.writelines("\n\nPART 2\n ********************\n\n")
    print("In part 2")

#   Main Function
def main():
    if LOGGING:
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY04.txt',sep=" ")
    print("In main")
    


if __name__ == "__main__":
    main()