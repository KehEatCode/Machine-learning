# Hierarchical clustering

- 通过计算不同类别数据点间的相似度来创建一棵有层次的嵌套聚类树。

- 在聚类树中，不同类别的原始数据点是树的最低层，树的顶层是一个聚类的根节点。创建聚类树有自下而上合并和自上而下分裂两种方法.


<img width="653" alt="Screen Shot 2022-08-15 at 1 06 07 PM" src="https://user-images.githubusercontent.com/93849914/184681610-be596724-8855-4a24-8546-0466efb3f561.png">


## Agglomerative clustering 合并算法

- 通过计算两类数据点间的相似性，对所有数据点中最为相似的两个数据点进行组合，并反复迭代这一过程。

- 简单的说层次聚类的合并算法是通过计算每一个类别的数据点与所有数据点之间的距离来确定它们之间的相似性，距离越小，相似度越高。

- 并将距离最近的两个数据点或类别进行组合，生成聚类树。

## Distance measures between clusters

- **Single Linkage** 的计算方法是将两个组合数据点中距离最近的两个数据点间的距离作为这两个组合数据点的距离。

    - 这种方法容易受到极端值的影响。两个很相似的组合数据点可能由于其中的某个极端的数据点距离较近而组合在一起。

- **Complete linkage** 计算方法与Single Linkage相反，将两个组合数据点中距离最远的两个数据点间的距离作为这两个组合数据点的距离。

    - Complete Linkage的问题也与Single Linkage相反，两个不相似的组合数据点可能由于其中的极端值距离较远而无法组合在一起。 

- **Average Linkage** 的计算方法是计算两个组合数据点中的每个数据点与其他所有数据点的距离。

    - 将所有距离的均值作为两个组合数据点间的距离。这种方法计算量比较大，但结果比前两种方法更合理。

## Choosing the number of clusters

https://www.analyticsvidhya.com/blog/2019/05/beginners-guide-hierarchical-clustering/
