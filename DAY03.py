#   DAY03.py
#   Written by Selene R. Schmittling
#   December 3, 2021

#   Import Statements
from typing import Counter
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
    p1vals = {}
    if LOGGING:
        logf.writelines(f"PART 1 \n ********************\n\n")
    counts = [0] * len(data[0])
    threshold = len(data)/2
    p1vals['counts'] = counts
    p1vals['threshold'] = threshold
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
    p1vals['gammastr'] = gammastr
    p1vals['epsilonstr'] = epsilonstr

    gammarate = int(gammastr,2)
    epsilonrate = int(epsilonstr,2)
    powerconsumption = gammarate * epsilonrate
    p1vals['pwrc'] = powerconsumption
    if LOGGING:
        logf.writelines(f"Final Counts: {counts}\n")
        logf.writelines(f"Gamma String: {gammastr}\n")
        logf.writelines(f"Epsilon String: {epsilonstr}\n")
        logf.writelines(f"Gamma Value: {gammarate}\n")
        logf.writelines(f"Epsilon Value: {epsilonrate}\n")
        logf.writelines(f"Power Consumption: {powerconsumption}")
    return p1vals

def part2(data, logf):
    databkup = data
    if LOGGING:
        logf.writelines("\n\nPART 2\n ********************\n\n")
    for i in range(len(data[0])):
        sumbit = 0
        newdata = []
        for d in data:
            sumbit = sumbit + int(d[i])
        if LOGGING:
            logf.writelines(f'Sum Bit: {sumbit} / {len(data)-sumbit}\n')
        if sumbit >= len(data)-sumbit:
            filtval = "1"
        else:
            filtval = "0"
        for d in data:
            if d[i] == filtval:
                newdata.append(d)
        if LOGGING:
            logf.writelines(f'Filter value: {filtval}\n')
            logf.writelines(f'New data: {newdata}\n')
        data = newdata
    oxygenrate = int(data[0], 2)
    data = databkup
    if LOGGING:
        logf.writelines(f'Oxygen Generator Rating: {oxygenrate}\n')
    for i in range(len(data[0])):
        sumbit = 0
        newdata = []
        for d in data:
            sumbit = sumbit + int(d[i])
        if LOGGING:
            logf.writelines(f'Sum Bit: {sumbit} / {len(data)-sumbit}\n')
        if sumbit < len(data)-sumbit:
            filtval = "1"
        else:
            filtval = "0"
        for d in data:
            if d[i] == filtval:
                newdata.append(d)
        if LOGGING:
            logf.writelines(f'Filter value: {filtval}\n')
            logf.writelines(f'New data: {newdata}\n')
        data = newdata
        if len(data)==1:
            break 
    co2scrub = int(newdata[0], 2)
    lifesupport = oxygenrate * co2scrub   
    if LOGGING:
        logf.writelines(f"CO2 Scrubber Rating: {co2scrub}\n")
        logf.writelines(f"Life Support Rating: {lifesupport}\n")
    return lifesupport


#   Main Function
def main():
    if LOGGING:
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY03.txt')
    part1ans = part1(data, logf)
    print(f"Part 1 Answer: {part1ans['pwrc']}")

    part2ans = part2(data, logf)
    print(f"Part 2 Answer: {part2ans}")
    


if __name__ == "__main__":
    main()