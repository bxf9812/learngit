import numpy as np
import pandas as pd

#print(data.shape[0])
#print(data.head())

# Implementing Laplace mechanism on Adult dataset by adding Laplacian random noise


# Load Adult dataset 
dataset = pd.read_csv(r'D:\bxf\python_work\adult.data',
    names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],
        sep=r'\s*,\s*',
        na_values="?",
        header=None,
        encoding='utf-8')
dataset.tail()

# Set parameters for Laplace function implementation
location = 1.0
scale = 1.0

#Find actual data count
datacount = dataset["Age"].value_counts()

# Gets random laplacian noise for all values
Laplacian_noise = np.random.laplace(location,scale, len(datacount))
print(Laplacian_noise)

# Add random noise generated from Laplace function to actual count
noisydata = datacount + Laplacian_noise

# Generate noisy histogram
noisydata.plot(kind="bar",color = 'g')