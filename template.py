#   Import Statements
import pandas as pd

#   Global vars
LOGGING = True

#   Utility Functions
def getdata(ifile):
    indata = pd.read_csv(ifile, sep=" ", header=False)
    # Add code to process data

def part1(data):
    print("In part 1")

def part2(data):
    print("In part 2")

#   Main Function
def main():
    if LOGGING:
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY99.txt',sep=" ")
    print("In main")
    


if __name__ == "__main__":
    main()