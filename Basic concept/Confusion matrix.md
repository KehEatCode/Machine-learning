# Confusion matrix

- 测试分类算法的表现

![截屏2022-08-16 上午12 21 51](https://user-images.githubusercontent.com/93849914/184797243-01b5398b-4b8d-4218-98e5-3432d7eca3ce.png)

矩阵可以延伸出一些列的指标，包括精度，准确率召回率等。

精度accuracy = (TP+TN)/(TP+TN+FP+FN)
准确率precision = TP/(TP+FP)
召回率recall = TP/(TP+FN)

精度：就是预测准确的数占所有样本的比例，是最基本的指标；

准确率表示被预测为正例的样本中有多少是positive的样本

召回率表示所有actual value的样本（实际卖出去的产品）中有多少是预测的positive；

通常来说在准确率和召回率之间是无法同时提高的，要相互妥协找到折中点的，调节的办法就是分类的阈值。
