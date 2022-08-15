# DBSCAN

- DBSCAN(Density-Based Spatial Clustering of Applications with Noise)是一基于密度的聚类算法

- DBSCAN将簇定义为密度相连的点的最大集合，能够把具有足够高密度的区域划分为簇，并可在噪声的空间数据库中发现任意形状的聚类。

- ε 当两点距离小于或等于ε，将其视为邻居

- DBSCAN是基于一组邻域来描述样本集的紧密程度的，参数 minPts (minimum number of points) 半径为ε 的最小数据个数 and ε (radius of neighborhood) 邻域半径

<img width="423" alt="Screen Shot 2022-08-15 at 1 58 05 PM" src="https://user-images.githubusercontent.com/93849914/184689631-ad7d46de-f1fd-4089-b703-32941cdbc450.png">
