import numpy as np  
  
# Creating the matrix  
record = np.array( [['Itika', 89, 91],  
                                   ['Aditi', 96, 82],  
                                   ['Harry', 91, 81],  
                                   ['Andrew', 87, 91],  
                                   ['Peter', 72, 79]])  
  
matrix = np.reshape(record, (5,3))  
print("The matrix is: \n", matrix)  
