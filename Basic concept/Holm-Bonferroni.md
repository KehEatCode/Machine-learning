# Holm-Bonferroni 推荐！！

- Step1: 先将各个假说的pvalue从小到大排序

H4=0.005 --> rank 1

H1=0.01  --> rank 2

H3=0.03  --> rank 3

H2=0.04  --> rank 4

- Step2: 拒绝原假设如果 p(i) <= α / (n – rank + 1)

    --> 0.05 / 4-1+1 = 0.0125
    
- Step3: 比较原假设和pvalue的大小

    --> 0.005 < 0.0125 因此拒绝原假设H4
    
    
- 当找到第一个不拒绝的假设时，步骤终止，后续假设都为不显著的

- 这种方法确保了全族错误率 <= α

https://en.wikipedia.org/wiki/Holm%E2%80%93Bonferroni_method


- 在考虑多个假设时，就会出现多重性问题：检查的假设越多，获得I 类错误（误报）的概率就越高。Holm-Bonferroni 方法是通过调整每个单独假设的拒绝标准来控制全族错误率（发生一个或多个 I 类错误的概率）的众多方法之一