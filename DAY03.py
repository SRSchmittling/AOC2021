#   DAY03.py
#   Written by Selene R. Schmittling
#   December 3, 2021

#   Import Statements
import pandas as pd

#   Global vars
LOGGING = True

#   Utility Functions
def getdata(ifile):
    f = open(ifile,'r')
    indata = f.readlines()
    f.close()
    # Add code to process data
    data = []
    for d in indata:
        data.append(d.strip())

    return data

def part1(data, logf):
    if LOGGING:
        logf.writelines(f"PART 1 \n ********************\n\n")
    counts = [0] * len(data[0])
    threshold = len(data)/2
    if LOGGING:
        logf.writelines(f"Threshold: {threshold}\n")
    for d in data:
        for i in range(len(d)):
            counts[i] = counts[i] + int(d[i])
    gammastr = ""
    for c in counts:
        if c > threshold:
            gammastr = gammastr+"1"
        else:
            gammastr = gammastr+"0"
    epsilonstr = ""
    for s in gammastr:
        if s=='1':
            epsilonstr = epsilonstr+"0"
        else:
            epsilonstr = epsilonstr+"1"


    gammarate = int(gammastr,2)
    epsilonrate = int(epsilonstr,2)
    powerconsumption = gammarate * epsilonrate
    if LOGGING:
        logf.writelines(f"Final Counts: {counts}\n")
        logf.writelines(f"Gamma String: {gammastr}\n")
        logf.writelines(f"Epsilon String: {epsilonstr}\n")
        logf.writelines(f"Gamma Value: {gammarate}\n")
        logf.writelines(f"Epsilon Value: {epsilonrate}\n")
        logf.writelines(f"Power Consumption: {powerconsumption}")
    return powerconsumption

def part2(data):
    print("In part 2")


#   Main Function
def main():
    if LOGGING:
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY03.txt')
    part1ans = part1(data, logf)
    print(f"Part 1 Answer: {part1ans}")
    


if __name__ == "__main__":
    main()