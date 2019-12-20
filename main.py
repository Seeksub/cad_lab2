import numpy
import json
import itertools



if __name__ == "__main__":
    bestSolution = []
    with open('config.json') as jsonFile:
        dataConfog = json.load(jsonFile)
        for data in dataConfog['matrix']:
            matrMaxVal = data['max_val']
            matrixSize = data['size']
        for data in dataConfog['Parent']:
            minGroupSize = data['min_group_size']
            maxGroupSize = data['max_group_size'] 
        S = numpy.random.randint(matrMaxVal, size=(matrixSize, matrixSize))
        print(S)
        while minGroupSize < 11:
            if matrixSize%minGroupSize == 0:
                parentNum = numpy.arange(matrixSize)
                partGroup = numpy.arange(minGroupSize)
                parentGroups = []
                parentGroups.extend(itertools.repeat(partGroup, int(matrixSize/minGroupSize)))
                parentGroups = numpy.array(parentGroups)
                parentGroups = [numpy.random.permutation(i) for i in parentGroups]
                parentGroups = numpy.array(parentGroups)
                print("parent groups:")
                print(parentGroups)
                print("-----------------")
                parentGroups = parentGroups.ravel()
                parent = numpy.array([parentNum,parentGroups])
                print("parent")
                print(parent)
                print("-----------------")
                X = numpy.zeros((minGroupSize, matrixSize))
                print("X:")
                print(X)
                print("-----------------")
                for i in range(len(parent[0])):
                    X[parent[1][i]][parent[0][i]] = 1
                W = X.dot(S)
                print("W:")
                print(W)
                print("-----------------")
                W = W.dot(X.transpose())
                print("W:")
                print(W)
                print("-----------------")
                bestSolution.append([W.trace(), minGroupSize])
                minGroupSize += 1
            else:
                minGroupSize += 1
        print(max(i for i in bestSolution))