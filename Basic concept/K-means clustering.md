# K-means clustering

- 先随机选取K个作为初始的聚类中心 centroids。

- 然后计算每个数据与各个聚类中心之间的距离，

- 把每个对象分配给距离它最近的聚类中心。

- 聚类中心以及分配给它们的对象就代表一个聚类。一旦全部对象都被分配了，每个聚类的聚类中心会根据聚类中现有的对象被重新计算。

- 这个过程将不断重复直到满足某个终止条件。终止条件可以是以下任何一个：

1)没有对象被重新分配给不同的聚类。
2)没有聚类中心再发生变化。
3)误差平方和局部最小。

https://www.analyticsvidhya.com/blog/2016/11/an-introduction-to-clustering-and-different-methods-of-clustering/


## K值的选取

- K值的选取对K-means影响很大，这也是K-means最大的缺点； 通常K值的选取方法有手肘法



![截屏2022-08-14 下午11 34 48](https://user-images.githubusercontent.com/93849914/184572812-b205ccea-8b3a-46bb-9216-8fcb99c4c772.png)
