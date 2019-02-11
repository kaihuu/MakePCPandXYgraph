import numpy as np

class GenerateFunctionData:
    def generateLinearfunction(self, a, b):
        X = np.linspace(-50, 50, 51)
        Y = a * X + b
        return X, Y

    def generateQuadraticfunction(self, a, b):
        X = np.linspace(-50, 50, 51)
        Y = pow(X, 2)
        return X, Y


