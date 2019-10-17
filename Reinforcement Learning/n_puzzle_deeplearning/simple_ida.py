from Npuzzle import Npuzzle

def cleanIda(scrambleList, scrambleSize):
    states = [tuple(row[0]) for row in scrambleList]
    values = [row[1] for row in scrambleList]
    clean_states = list(set(states))
    ret = [None] * len(clean_states)
    idx = 0
    print("a")
    for j in range(len(clean_states)):
        min_val = scrambleSize
        for i in range(len(states)):
            if clean_states[j] == states[i] and values[i] <= min_val:
                ret[j] = [list(states[i]), values[i]]
        idx += 1
    print("b")
    return ret

def getIdaExamples(nbPuzzle, scrambleSize, puzzleSize):
    ret = []
    n = Npuzzle(None, puzzleSize)
    for _ in range(nbPuzzle):
        scrambleList = n.scramble(scrambleSize - 1)
        ret += scrambleList
    return(ret)