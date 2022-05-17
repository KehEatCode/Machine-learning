# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Importing the dataset in python （行数从0-9开始）
dataset = pd.read_csv('Data.csv')
#创建x
X = dataset.iloc[:,:-1].values
# dataset 是我们已经导入好的数据集；iloc是我们会取数据集中的某一些行和某一些列；逗号前面是行数，右边是列数；冒号代表取所有的行数or列数；：-1代表我们不会取最后一列（最后是否买产品，这一列是因变量y）；.values代币安我们取dataset中的这些值
# 创建y
y= dataset.iloc[:,3].values

# Importing the dataset in R （行数从1-10开始）
#设置工作路径，读取数据
dataset = read.csv('Data.csv')

#classes类，object对象

# 处理Missing data，用平均值来代替
#Taking care of missing data in python
from sklearn.preprocessing import SimpleImputer
#sklearn 非常强大的，挖掘数据的标准库；preprocessing数据的预处理；从标准库中导入了imputer这个类（专门进行缺失数据的处理）
# 创建类的对象
imputer = SimpleImputer (missing_values = 'NaN', strategy='mean', axis = 0)
imputer = SimpleImputer.fit(X[:,1:3])
X[:, 1:3] = SimpleImputer.transform(X[:,1:3])

# Taking care of missing data in R
dataset = read.csv('Data.csv')
# Taking care of missing data in R
dataset$Age[is.na(dataset$Age)] = mean(dataset$Age,na.rm = T)
#dataset中Age这一列，如果是NA那返还的是true，如果不是NA那么会是false, na: NA; rm:remove
dataset$Salary[is.na(dataset$Salary)] = mean(dataset$Salary,na.rm = T)
















