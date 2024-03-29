# Regularization 

- 为了防止过拟合

- 通过给需要训练的目标函数加上一些规则（限制）

- 如果模型过于复杂出现过拟合时，有必要减少特征数量

- 正则化对较大系数的参数进行‘惩罚’，将系数正则化或者缩小到零，从而限制模型中的方差量

- 缺点，不适用于复杂和灵活的模型，可能会出现过拟合的情况

- 正则化显著降低了方差，而不会增加偏差

- Lasso Regression：在这种技术中，我们添加 α*Σ|β|作为收缩量。它只惩罚高系数。当调整参数 α 足够大时，它具有强制某些系数估计值精确等于 0 的效果。这种技术也称为 L1 正则化。

- Ridge Regression：在这种技术中，我们通过添加收缩量 α*Σβ² 来修改残差平方和，并使用 α 作为调整超参数，它决定了我们想要在多大程度上惩罚我们的灵活性模型。这种技术也称为 L2 正则化
