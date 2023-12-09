---
title: Matrix-w03
date: 2023-09-23 09:56:27
tags: 
    - 矩阵
    - 笔记
---


<!-- ## ![Alt text](image-1.png)
 -->

 ## Properties on the Matrix Inverse


## Inner Product 

$ <u,v>$
$$<A,B> = <\text{vec}(A), \text{vec}(B)> = tr(A^HB)
$$

矩阵的共轭转置

Frobenius 范数

![Alt text](https://picx.zhimg.com/80/v2-73d221cb9175ae0c6895b8e13b39f598_1440w.png)

![Alt text](https://pic1.zhimg.com/80/v2-1b121b4cb8c2b6aefab8fbb0c512a4c7_1440w.png)

![Alt text](https://pic1.zhimg.com/80/v2-fc409ca69910b1fa30679d57849c8b18_1440w.png)


## Rank of a  Matrix
1. max number of linearly independent rows/cols
1. rank(A)  = dim row(A) = dim col(A)

$$row(A) = \{ y^TA\}$$
$$col(A) = \{ Ax\}$$
$$ rank{ AX} ??  rank(A)$$
什么满秩的时候/
左乘一个列满秩 或者 右乘一个 行满秩的矩阵 不改变 A的rank
![Alt text](https://picx.zhimg.com/80/v2-a8b15a56dcacbb5dff6fa723e664fee4_1440w.png)

![Alt text](https://picx.zhimg.com/80/v2-93fa826cb8731b5cb0cf59b23a2e9630_1440w.png)
这里面其实有A = XY (总可以)

未来我们使用这个性质 就是总可以 AB = XY  (if AB!=  0)

![Alt text](https://pic1.zhimg.com/80/v2-bf527d551f6a12be44f878ab30da1f50_1440w.png)

![ker 和 rank 之间的关系需要证明](https://picx.zhimg.com/80/v2-59f41ee793651362f0c3df57879725aa_1440w.png)

## determination of MATRIX
### properties of det(A)
8 properties AND 2 other properties
![Alt text](https://pic1.zhimg.com/80/v2-615846d6bcc61dfcd75916fe4b98b1b4_1440w.png)

![Alt text](https://picx.zhimg.com/80/v2-b2ac3acef2562ba596ecbde6d78d4b69_1440w.png)