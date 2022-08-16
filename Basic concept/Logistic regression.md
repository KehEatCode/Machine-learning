# Logistic regression 逻辑回归

- 是一种用于解决二分类（0 or 1）问题的机器学习方法，用于估计某种事物的可能性。

    - 比如某用户购买某商品的可能性，某病人患有某种疾病的可能性，以及某广告被用户点击的可能性等。 
    
    - 注意，这里用的是“可能性”，而非数学上的“概率”，logisitc回归的结果并非数学定义中的概率值，不可以直接当做概率值来用。该结果往往用于和其他特征值加权求和，而非直接相乘。

- Logistic Regression is a supervised learning algorithm that is used for classification problems, i.e., where the dependent variable is categorical.

- In logistic regression, we use the Sigmoid function to calculate the probability of the dependent variable.

- The real-life applications of logistic regression are churn prediction, spam detection, etc.

- The below image shows how logistic regression is different from linear regression in fitting the model.

- ![截屏2022-08-16 上午12 01 15](https://user-images.githubusercontent.com/93849914/184795233-b00e258f-2c01-41d2-ae12-2d1b8f862d0b.png)


## 那么逻辑回归与线性回归是什么关系呢？

- 逻辑回归（Logistic Regression）与线性回归（Linear Regression）都是一种广义线性模型（generalized linear model）。逻辑回归假设因变量 y 服从伯努利分布，而线性回归假设因变量 y 服从高斯分布。 

- 因此与线性回归有很多相同之处，去除Sigmoid映射函数的话，逻辑回归算法就是一个线性回归。可以说，逻辑回归是以线性回归为理论支持的，但是逻辑回归通过Sigmoid函数引入了非线性因素，因此可以轻松处理0/1分类问题。

