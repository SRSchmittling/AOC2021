#   DAY02.py
#   Written by Selene R. Schmittling
#   December 2, 2021

#   Import Statements
import pandas as pd
LOGGING = True

#   Utility Functions
def getdata(ifile):
    indata = pd.read_csv(ifile, sep=" ")
    # Process data
    return indata

def part1(data, logf):
    logf.writelines(f"PART 1 \n ********************\n\n")
    horizontal = 0
    depth = 0
    if LOGGING:
        logf.writelines(f"Current horizontal: {horizontal} / Current depth: {depth}\n")
    for i in range(len(data.index)):
        if LOGGING:
            logf.writelines(f"{i}: {data.dir[i]}/{data.val[i]}\n")
        if data.dir[i] == 'forward':
            horizontal = horizontal + data.val[i]
        elif data.dir[i] == 'down':
            depth = depth + data.val[i]
        elif data.dir[i] == 'up':
            depth = depth - data.val[i]
        else:
            print(f'Error: unknown direction: {data.dir[i]}!!')

        if LOGGING:
            logf.writelines(f"Updated horizontal: {horizontal} / Updated depth: {depth}\n")
    if LOGGING:
        logf.writelines(f"Final horizontal: {horizontal} / Final depth: {depth}\n")
    part1ans = horizontal * depth
    return part1ans

def part2(data, logf):
    logf.writelines(f"PART 2 \n ********************\n\n")
    horizontal = 0
    depth = 0
    aim = 0
    if LOGGING:
        logf.writelines(f"Current horizontal: {horizontal} / Current depth: {depth} / Current Aim: {aim}\n")
    for i in range(len(data.index)):
        if LOGGING:
            logf.writelines(f"{i}: {data.dir[i]}/{data.val[i]}\n")
        if data.dir[i] == 'forward':
            horizontal = horizontal + data.val[i]
            depth = depth + (aim * data.val[i])
        elif data.dir[i] == 'down':
            aim = aim + data.val[i]
        elif data.dir[i] == 'up':
            aim = aim - data.val[i]
        else:
            print(f'Error: unknown direction: {data.dir[i]}!!')

        if LOGGING:
            logf.writelines(f"Updated horizontal: {horizontal} / Updated depth: {depth} / Updated Aim: {aim}\n")
    if LOGGING:
        logf.writelines(f"Final horizontal: {horizontal} / Final depth: {depth} / Final aim: {aim}\n")
    part2ans = horizontal * depth
    return part2ans


#   Main Function
def main():
    if LOGGING:
        # Open log file
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY02.txt')
    part1ans = part1(data, logf)
    print(f"Part 1 Answer: {part1ans}")
    part2ans = part2(data, logf)
    print(f"Part 2 Answer: {part2ans}")
    if LOGGING:
        logf.close()


if __name__ == "__main__":
    main()