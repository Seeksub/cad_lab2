import numpy
import json
import itertools
import random
from tabulate import tabulate

if __name__ == "__main__":
    bestSolution = []
    parents = []
    with open('config.json') as jsonFile:
        dataConfog = json.load(jsonFile)
    for data in dataConfog['matrix']:
        matrMaxVal = data['max_val']
        matrixSize = data['size']
    for data in dataConfog['Parent']:
        minGroupSize = data['min_group_size']
        maxGroupSize = data['max_group_size'] 
    S = numpy.random.randint(matrMaxVal, size=(matrixSize, matrixSize))
    for i in range(matrixSize):
        S[i][i] = 0
    for i in range(matrixSize):
        for j in range(matrixSize):
            S[j][i] = S[i][j]
    print(tabulate(S))
    mgroup = 0
    while minGroupSize < maxGroupSize:
        if matrixSize%minGroupSize == 0:
            print('Group_size: ')
            print(minGroupSize)
            parentNum = numpy.arange(matrixSize)
            partGroup = numpy.arange(minGroupSize)
            parentGroups = []
            parentGroups.extend(itertools.repeat(partGroup, int(matrixSize/minGroupSize)))
            parentGroups = numpy.array(parentGroups)
            parentGroups = [numpy.random.permutation(i) for i in parentGroups]
            parentGroups = numpy.array(parentGroups)
            parentGroups = parentGroups.ravel()
            parent = numpy.array([parentNum,parentGroups])
            print("parent")
            print(tabulate(parent))
            print("-----------------")
            X = numpy.zeros((minGroupSize, matrixSize))
            for i in range(len(parent[0])):
                X[parent[1][i]][parent[0][i]] = 1
            print("X:")
            print(tabulate(X))
            print("-----------------")
            W = X.dot(S)
            W = W.dot(X.transpose())
            print("W:")
            print(tabulate(W))
            print("-----------------")
            bestSolution.append([W.trace(), minGroupSize])
            parents.append([W.trace(), parent])
            mgroup = minGroupSize
            minGroupSize += 1
        else:
            minGroupSize += 1

    print(bestSolution)
    print('Max W:')
    print(max(i for i in bestSolution))
    maxW = max(i for i in bestSolution)[0]
    print('Median W:')
    print(numpy.median(bestSolution, axis=0))
    print('Parents:')
    print(tabulate(parents))
    print('--------------')
    median = numpy.median(bestSolution, axis=0)[0]
    arr_forDel = []
    for arr in parents:
        if arr[0] >= median:
            arr_forDel.append(arr)
    # for elem in arr_forDel:
        # parents.remove(elem)
    parents = arr_forDel
    print('True parents:')
    print(tabulate(parents))
    print('------------')
    #print(crossoverNum)
    # parentId = 0
    plen = len(parents)
    permutationPairs = itertools.permutations(parents, 2)
    # print("Parents to permutate:")
    # print(tabulate(permutationPairs))
    random.seed(100)
    bestFit = []
    for pair in permutationPairs:
        # print("Pair:")
        # print(pair)
        # print('------------')
        crossoverNum = random.randint(2, matrixSize-2)
        # print("Number of crossovers for pair:")
        # print(crossoverNum)
        for i in range(crossoverNum):
            headCut = random.randint(0, matrixSize-1)
            tailCut = random.randint(0, matrixSize-1)
            while tailCut == headCut:
                tailCut = random.randint(0, matrixSize-1)
            for i in range(headCut, tailCut):
                pair[0][1][0][i],pair[1][1][0][i] = pair[1][1][0][i], pair[0][1][0][i]
                pair[0][1][1][i],pair[1][1][1][i] = pair[1][1][1][i], pair[0][1][1][i]
            # print("crossover:")
            # print([pair[0][1],pair[1][1]])
            #-------
            X = numpy.zeros((mgroup, matrixSize))
            for unit in pair:
                for j in range(len(unit[1][1])):
                    X[unit[1][1][j]][unit[1][0][j]] = 1
                # print(unit)
                # print("X:")
                # print(tabulate(X))
                # print("-----------------")
                W = X.dot(S)
                W = W.dot(X.transpose())
                # print("W:")
                # print(tabulate(W))
                # print("-----------------")
                if W.trace() > maxW:
                    bestFit = numpy.array([W.trace(), unit[1]])
                    #bestUnit.append([W.trace(), unit[1]])
            # -------
    print("Best Unit:")
    print(tabulate(bestFit[1]))
    print("Best fit:")
    print(bestFit[0])
