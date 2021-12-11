#   DAY04.py
#   Written by Selene R. Schmittling
#   December 3, 2021

#   Import Statements
import pandas as pd

#   Global vars
LOGGING = True

#   Utility Functions
def getdata(ifile, logf):
    if LOGGING:
        logf.writelines(f"DATA LOAD \n ********************\n")
        boards = list()
        board = list()
    with open(ifile) as f:
        boardcount = 0
        count = 0
        for line in f:
            count +=1
            if count == 1:
                calls = [i for i in line.strip().split(sep=",")]
                if LOGGING:
                    logf.writelines(f"# of calls: {len(calls)}\n")
                    logf.writelines(f"Calls: {calls}\n")
            else:
                if line != "\n":
                    for num in line.strip().split(" "):
                        if num != '':
                            board.append(num)
                else:
                    if boardcount > 0:
                        boards.append(board)
                        board = list()
                    boardcount += 1
        boards.append(board)
    if LOGGING:
        logf.writelines(f"# of Boards: {boardcount}\n")
        logf.writelines(f"Boards: {boards}\n")
    data = {}
    data = {"calls": calls, "boards": boards, "numboards": boardcount}
    return data

def checkboard(board_marked):
    if sum(board_marked[0:5]) == 5 or sum(board_marked[5:10]) == 5 or sum(board_marked[10:15]) == 5 or sum(board_marked[15:20]) == 5 or sum(board_marked[20:25]) == 5:
        win = True
    elif sum([board_marked[index] for index in [0, 5, 10, 15, 20]]) == 5 or \
         sum([board_marked[index] for index in [1, 6, 11, 16, 21]]) == 5 or \
         sum([board_marked[index] for index in [2, 7, 12, 17, 22]]) == 5 or \
         sum([board_marked[index] for index in [3, 8, 13, 18, 23]]) == 5 or \
         sum([board_marked[index] for index in [4, 9, 14, 19, 24]]) == 5:
        win = True
    else:
        win = False
    return win

def printboard(board, logf):
    if not LOGGING:
        print(f"{board[0:5]}")
        print(f"{board[5:10]}")
        print(f"{board[10:15]}")
        print(f"{board[15:20]}")
        print(f"{board[20:25]}")
    else:
        logf.writelines(f"{board[0:5]}\n")
        logf.writelines(f"{board[5:10]}\n")
        logf.writelines(f"{board[10:15]}\n")
        logf.writelines(f"{board[15:20]}\n")
        logf.writelines(f"{board[20:25]}\n\n")
    
def part1(data, logf): 
    firstwin = True
    if LOGGING:
        logf.writelines("PART 1\n ********************\n\n")
    num_boards = data["numboards"]
    data_marked = [[0 for _ in range(25)] for _ in range(num_boards)]
    for call in data['calls']:
        if LOGGING:
            logf.writelines(f"Call: {call}\n")
        for i in range(len(data['boards'])):
            board = data['boards'][i]
            printboard(board, logf)
            if LOGGING:
                logf.writelines(f"Call on Board?: {call in board}\n")
            if call in board:
                callidx = board.index(call)
                data_marked[i][callidx] = 1
                win = checkboard(data_marked[i])
                if LOGGING:
                    logf.writelines(f"Location on board: {callidx}\n")
                if win and firstwin:
                    firstwin = False
                    unmarked_idx = [j for j, x in enumerate(data_marked[i]) if x == 0]
                    unmarked_vals = [board[index] for index in unmarked_idx]
                    unmarked_sum = 0
                    for val in unmarked_vals:
                        unmarked_sum += int(val)
                    score = unmarked_sum * int(call)
                    if LOGGING:
                        logf.writelines(f"Winning Board: {i}\n")
                        printboard(data_marked[i], logf)
                        logf.writelines(f"Index of unmarked vals: {unmarked_idx}\n")
                        logf.writelines(f"Unmarked Values: {unmarked_vals}\n")
                        logf.writelines(f"Unmarked Sum: {unmarked_sum}\n")
                        logf.writelines(f"Score: {score}\n")
    return score
    
                

def part2(data, logf):
    if LOGGING:
        logf.writelines("PART 2\n ********************\n\n")
    num_boards = data["numboards"]
    data_marked = [[0 for _ in range(25)] for _ in range(num_boards)]
    lastcall = None
    lastboard = None
    wins = [0 for _ in range(num_boards)]
    wincount = 0
    for call in data['calls']:
        if min(wins) > 0:
            if LOGGING:
                logf.writelines(f"Final Win Achieved")
                break
        if LOGGING:
            logf.writelines(f"Call: {call}\n")
        for i in range(len(data['boards'])):
            if min(wins) > 0:
                break
            board = data['boards'][i]
            printboard(board, logf)
            if LOGGING:
                logf.writelines(f"Call on Board?: {call in board}\n")
            if call in board:
                callidx = board.index(call)
                if not sum(wins)==num_boards:
                    data_marked[i][callidx] = 1
                win = checkboard(data_marked[i])
                if win:
                    wincount += 1
                    wins[i] = wincount
                    if LOGGING:
                        if min(wins) > 0:
                            logf.writelines(f"Final Win Achieved")
                    if LOGGING:
                        logf.writelines(f"Wins: {wins}\n")
                    lastcall = call
                    lastboard = i
                    if LOGGING:
                        logf.writelines("WIN!!! \n ********** \n")
                        logf.writelines("Marked Board\n")
                        printboard(data_marked[lastboard], logf)
                        logf.writelines(f"Location on board: {callidx}\n")
                        logf.writelines(f"Current Last Call: {lastcall}\n")
                        logf.writelines(f"Current idx: {lastboard}\n\n")
    if LOGGING:
        logf.writelines("FINAL WIN\n *****\n")
        logf.writelines(f"Index of Final Winning Board: {lastboard}\n")
        logf.writelines(f"Final Call of Winning Board: {lastcall}\n")
        logf.writelines("Marked Board: \n ")
        printboard(data_marked[lastboard], logf)
    board = data['boards'][lastboard]
    unmarked_idx = [i for i, x in enumerate(data_marked[lastboard]) if x == 0]
    unmarked_vals = [board[index] for index in unmarked_idx]
    unmarked_sum = 0
    for val in unmarked_vals:
        unmarked_sum += int(val)
    score = unmarked_sum * int(lastcall)
    if LOGGING:
        logf.writelines(f"Unmarked Values: {unmarked_vals}\n")
        logf.writelines(f"Unmarked Sum: {unmarked_sum}\n")
        logf.writelines(f"Score: {score}\n")
    return score


#   Main Function
def main():
    if LOGGING:
        logf = open('logfile.txt','w')
    else:
        logf = ""
    data = getdata('data/DAY04.txt', logf)
    part1ans = part1(data, logf)
    print(f"Part 1 Answer: {part1ans}")
    part2ans = part2(data, logf)
    print(f"Part 2 Answer: {part2ans}")

    


if __name__ == "__main__":
    main()