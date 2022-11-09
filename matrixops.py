from numpy import linalg
import numpy as np
from flask import Flask

app = Flask(__name__)

"""
function matrixmultiply
matrixSet - List
Takes in a list of matrices and recursively multiplies them together, 
then returns the matrix product.
"""
@app.route("/matmultiply/<matrixSet>", methods=["GET"])
def matrixmultiply(matrixSet):
    if len(matrixSet) == 1:
        return np.matrix(matrixSet[0])
    elif len(matrixSet) < 1:
        return {"res": ['DNE']}
    matrix1 = np.matrix(matrixSet[0])
    matrix2 = np.matrix(matrixSet[1])
    if np.size(matrix1, 1) != np.size(matrix2, 0):
        return {"res": ['DNE']}
    else:
        newmatrix = []
        for m in range(len(matrixSet)):
            if m == 1:
                continue
            else:
                newmatrix.append(matrixSet[m])
        newmatrix[0] = np.matmul(matrix1, matrix2)
        return matrixmultiply(newmatrix)
        
"""
function dotprod
matrixSet - List
Takes in a set of two matrices and returns their dot product, or
zero if the operation can not be completed. 
"""
@app.route("/dotprod/<matrixSet>", methods=["GET"])
def dotprod(matrixSet):
    if len(matrixSet) == 1:
        return matrixSet[0]
    elif len(matrixSet) != 2:
        return 0
    matrix1 = np.matrix(matrixSet[0])
    matrix2 = np.matrix(matrixSet[1])
    matrix1rows = np.size(matrix1, 0)
    matrix2rows = np.size(matrix2, 0)
    matrix1cols = np.size(matrix1, 1)
    matrix2cols = np.size(matrix2, 1)
    overmatrix1dims = (matrix1rows > 1 and matrix1cols > 1)
    overmatrix2dims = (matrix2rows > 1 and matrix2cols > 1)
    if np.size(matrix1) != np.size(matrix2) or overmatrix1dims or overmatrix2dims:
        return 0
    else:
        newmatrix = []
        for m in range(len(matrixSet)):
            if m == 1:
                continue
            else:
                newmatrix.append(matrixSet[m])
        if matrix1rows == 1 and matrix2rows == 1:
            matrix1 = transpose(matrix1)
            matrix2 = transpose(matrix2)
        sum1 = 0
        for i in range(len(matrix1)):
            sum1 += matrix1[i] * matrix2[i]
        return np.matrix(sum1)

"""
function det
matrix1 - List (matrix)
completes the determinant of the given matrix 
and returns the product.
"""
@app.route("/det/<matrix1>", methods=["GET"])
def det(matrix1):
    matrix1 = np.matrix(matrix1)
    if np.size(matrix1, 0) != np.size(matrix1, 1):
        return {"res": ['DNE']}
    a = linalg.det(matrix1)
    return np.matrix(a)

"""
function transpose
matrix1 - List (matrix)
completes the transpose of the given matrix 
and returns the product.
"""
@app.route("/transpose/<matrix1>", methods=["GET"])
def transpose(matrix1):
    matrix1 = np.matrix(matrix1)
    a = np.transpose(matrix1)
    return a



app.run(port=5000)

