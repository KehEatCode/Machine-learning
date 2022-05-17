# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Importing the dataset
dataset = pd.read_csv('Data.csv')

#创建x
X = dataset.iloc[:,:-1].values
# dataset 是我们已经导入好的数据集；iloc是我们会取数据集中的某一些行和某一些列；逗号前面是行数，右边是列数；冒号代表取所有的行数or列数；：-1代表我们不会取最后一列（最后是否买产品，这一列是因变量y）；.values代币安我们取dataset中的这些值

# 创建y
y= dataset.iloc[]
