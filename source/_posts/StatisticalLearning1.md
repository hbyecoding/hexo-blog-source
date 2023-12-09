---
title: 李航之ch1统计学习方法概论 
date: 2023-11-01 22:01:52
tags: learning
---
# 李航之ch1统计学习方法概论 

## 统计学习 监督学习

统计机器学习(statistical machine learning) 建立在计算机及网络之上的, 数据驱动的, 目的是对数据预测和分析的, 构建了模型并且应用模型预测和分析的, 应用到了概率论, 统计学, 计算理论,最优化理论和计算机信息论的.

#### 方法
- supervised learning(*)
- nusupervised learning
- semi-supervised learning
- reinforcement learning

#### 基本概念
输入空间
特征空间= 特征向量存在的空间.每一维度对应一个特征. (有时候这两个空间等同,有时候不一样)
输出空间  
联合概率分布
假设空间

## 统计学习三要素 模型 策略和算法
方法 = 模型 + 策略 + 算法
1 策略, 需要首先损失函数与风险函数的概念, loss 度量模型一次预测的好坏, 风险函数度量平均意义下的模型预测的好坏
2 经验风险最小化与结构风险最小化
经验风险最小化 能保证有很好的学习效果.
结构风险最小化 类似于 最优化.



## 正则化和交叉验证
 指示函数 I
r + e = 1
## 泛化能力
generalization ability  
generalization error (less , better)
generalization error bound (less , better)
function(capacity) 假设空间容量越大,模型就越难学, 泛化误差上界就大
page 15 Hoeffding unequation


## 生成模型generative model  与判别模型 discriminative

page18 生成方法的特点, 判别方法的特点

## 分类问题
page19


## 回归问题

