# Author: Rohan Singh
# Date: 12/9/2022
# Source code for a general purpose single-layer n-to-1 neural network, i.e. The network takes in an n-dimensional input vector and returns a scalar output

#imports 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
"""
This cell contains the source code for the SingleLayer Neural Network Class
"""
class NeuralNetwork:

    #The constructor for the Neural Network class
    def __init__(self, dataset, targets) -> None:
        self.trainset = dataset
        self.targetset = targets
        pass

    

    #This function will give you the output of the neural network given a weight vector
    def getNNOutput(self, weights):

        #This vector will contain the output of the neural network
        output = []

        #Getting the output for all of the datapoints within the dataset
        for i in range (0,len(self.trainset),1):

            #This will be added for the bias-term
            a = np.array([1]) 
            a = np.concatenate((a,self.trainset[i]),axis=0)

            #Appending the output for the point (inner-product) into the output list
            output.append(np.dot(a,weights))

        #Converting the output into a numpy array
        return np.array(output)



    #This will be used to train the Neural Network using gradient descent, using the input step-size and stopping point
    def train(self, epsilon, maxerr):
        


        print("Lmao")

    def printHello(self):
        print("Hello World!")


#%%
"""
This cell contains a helper function to pre-process the data for the demonstration in the main method
"""

def getData():
    dataset = []
    target = []

    filepath = ""

    #Reading the csv from the filepath
    df = pd.read_csv(filepath)

    #Getting numpy array columns from the dataframe
    pet_len = df["petal_length"].to_numpy()
    pet_wid = df["petal_width"].to_numpy()
    sep_len = df["sepal_length"].to_numpy()
    sep_wid = df["sepal_width"].to_numpy()
    spec = df["species"]

    for i in range(0,len(pet_len),1):

        #For a row of datapoints
        temp = []
        temp.append(pet_len[i])
        temp.append(pet_wid[i])
        temp.append(sep_len[i])
        temp.append(sep_wid[i])

        #Converting Species string to float
        if(spec[i] == "setosa"):
            target.append(100.0)
        elif(spec[i] == "virginica"):
            target.append(200.0)
        else:
            target.append(300.0)

        #Adding the row to the dataset
        dataset.append(temp)


    return np.array(dataset), np.array(target)


#%%
"""
This cell contains the main method to show the demonstration of the code
"""

def main():

    #Fetching the data using the helper function in the cell above
    dataset, target = getData()

    #Instantiating the Neural Network Object
    DemoNN = NeuralNetwork(dataset=dataset,targets=target)
    DemoNN.printHello()



if __name__ == "__main__":
    main()


#%%
