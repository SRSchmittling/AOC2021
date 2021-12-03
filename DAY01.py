#   Import Statements
import numpy as np

#   Utility Functions
def getdata(ifile):
    f = open(ifile,"r")
    indata = f.readlines()
    f.close()
    data = []
    for d in indata:
        data.append(int(d.strip()))
    return np.asarray(data)

def part1(data):
    data1 = data[1:len(data)]
    data2 = data[0:len(data)-1]
    dif = data1-data2
    return sum(dif>0)

def part2(data,window):
    outdata = []
    for i in range(len(data)-2):
        outdata.append(sum(data[i:i+window]))
    print(f"Length of outdata: {len(outdata)}")
    outdata = np.asarray(outdata)
    data1 = outdata[1:len(outdata)]
    data2 = outdata[0:len(outdata)-1]
    difs = data1-data2
    print(sum(difs>0))


#   Main Function
def main():
    ifile = 'data/DAY01.txt'
    data = getdata(ifile)
    print(f"# of data elements: {len(data)}")
    #print(part1(data))
    print(part2(data,3))
    


if __name__ == "__main__":
    main()