import numpy
import json




if __name__ == "__main__":
    with open('config.json') as jsonFile:
        dataConfog = json.load(jsonFile)
        for data in dataConfog['matrix']:
            print(data['max_val'])
            matrMaxVal = data['max_val']
            print(data['size'])
            matrixSize = data['size']
        print(numpy.random.randint(matrMaxVal, size=(matrixSize, matrixSize)))