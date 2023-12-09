---
title: 最近学习矩阵论, 先把一些重要的性质摘出来
date: 2023_10_09
tags: 矩阵
---

Property 1: The determinant of the identity matrix is one;
Property 2: The determinant changes sign under row/column interchange;
Property 3: The determinant is a linear function of the first row, holding all other rows
fixed.

### SVD from EVD
要从矩阵$AA^H$的特征值分解（EVD）中获取矩阵A的奇异值分解（SVD），您可以按照以下步骤进行：

1. 计算矩阵$AA^H$的特征值分解（EVD）：
   首先，计算矩阵$AA^H$的特征值分解。对于Hermitian（复数域中对称的）矩阵$M$，其特征值分解为：
   $$M = U \Lambda U^H$$
   其中：
   - $U$是一个酉矩阵，其列是$M$的特征向量。
   - $\Lambda$是一个对角矩阵，包含$M$的特征值。

2. 计算矩阵A的奇异值分解（SVD）：
   一旦您获得了矩阵$AA^H$的特征值分解，您可以如下计算矩阵A的SVD：
   $$A = U \sqrt{\Lambda} V^H$$
   其中：
   - $U$是从$AA^H$的特征值分解中获得的酉矩阵。
   - $\sqrt{\Lambda}$是一个对角矩阵，包含$AA^H$的特征值的平方根（逐元素取平方根）。
   - $V^H$是矩阵$V$的共轭转置，$V$可以是任何酉矩阵。

因此，基本上，您使用$AA^H$的特征值分解来找到特征值和特征向量，然后用它们构建矩阵A的奇异值分解。A的左奇异向量是$AA^H$的特征向量，奇异值是$AA^H$的特征值的平方根。右奇异向量可以通过关系$V = A^H U \Lambda^{-1/2}$从左奇异向量和原始矩阵A获得，但请注意，由于SVD的酉性质，右奇异向量并不唯一。

### SVD properties
"MP inverse based on the SVD" 表示基于奇异值分解（SVD）计算的Moore-Penrose伪逆（MP逆）。

奇异值分解（SVD）是一种将一个矩阵分解为三个矩阵乘积的数学工具，具体而言，将矩阵A分解为以下形式：

$$A = U \Sigma V^H$$

其中：
- U是一个酉矩阵（正交矩阵），它的列包含A的左奇异向量。
- Σ是一个对角矩阵，其对角线上的元素是A的奇异值。
- $V^H$是矩阵V的共轭转置，它的列包含A的右奇异向量。

Moore-Penrose伪逆（MP逆）是矩阵的一种广义逆，可以用来求解线性最小二乘问题以及在矩阵求逆不可行时的一些问题。对于一个矩阵A，它的MP逆通常表示为$A^+$。

"MP inverse based on the SVD" 意味着通过使用A的奇异值分解（SVD），可以计算其Moore-Penrose伪逆$A^+$。这通常涉及到利用SVD的性质来构建MP逆，具体方法是使用U，Σ，$V^H$来计算$A^+$，通常的公式是：

$$A^+ = V \Sigma^+ U^H$$

其中，Σ^+是Σ的伪逆，即将Σ的非零奇异值取倒数，然后取共轭转置。

这种方法在数值计算和线性代数中非常有用，特别是在处理奇异矩阵（不可逆矩阵）或求解超定系统（过多未知数的线性方程组）时。



矩阵A的伪逆（Moore-Penrose伪逆）记作$A^{+}$，它对于非方阵A是一种广义的逆矩阵。矩阵A的伪逆具有以下几个性质：

1. $AA^{+}A = A$
2. $A^{+}AA^{+} = A^{+}$
3. $(AA^{+})^T = AA^{+}$
4. $(A^{+}A)^T = A^{+}A$

现在，考虑$x_0 = A^{+}y$，您想知道是否总是可以找到y，使得$y = A^{+}x_0$。让我们进行分析：

从$x_0 = A^{+}y$开始，如果要找到y，可以两边同时左乘A：

$Ax_0 = AA^{+}y$

根据伪逆的性质，我们可以将其简化为：

$Ax_0 = (AA^{+})y = y$

因此，如果$Ax_0 = y$，那么$y = A^{+}x_0$。

然而，有些情况下这个等式可能不成立：

1. 如果矩阵A是奇异矩阵（不满秩），则可能不存在唯一的y解。在这种情况下，A将没有完整的Moore-Penrose伪逆。

2. 如果$Ax_0$不在A的列空间（列空间）内，那么就不存在满足等式$Ax_0 = y$的y。

因此，$y = A^{+}x_0$的存在与矩阵A的性质、$x_0$的具体值以及是否存在满足等式的y解有关。



The statement you've provided suggests that if you have a vector x such that the 2-norm (Euclidean norm) of the difference between A times x_0 and y is equal to the 2-norm of the difference between A times x and y (i.e., ‖Ax_0 - y‖_2 = ‖Ax - y‖_2), then the norm of x_0 is less than or equal to the norm of x (‖x_0 ‖_2 ≤ ‖x‖_2), and equality only holds when x_0 is equal to x.

This statement is related to the concept of the orthogonal projection. When ‖Ax_0 - y‖_2 = ‖Ax - y‖_2, it means that both x_0 and x minimize the 2-norm of the error between the projected vector A times x (or A times x_0) and the target vector y.

In such a case, x_0 and x are both candidates for the solution, but the statement ‖x_0 ‖_2 ≤ ‖x‖_2 implies that x_0 is the solution that minimizes the norm among all possible solutions. If ‖x_0 ‖_2 is less than ‖x‖_2, it means that x_0 is closer to the origin, and therefore has a smaller Euclidean norm.

Equality ‖x_0 ‖_2 = ‖x‖_2 only holds when x_0 is equal to x, indicating that x_0 is the optimal solution. If x_0 is not equal to x, it implies that x is further away from the origin than x_0, resulting in a larger Euclidean norm.

So, when ‖Ax_0 - y‖_2 = ‖Ax - y‖_2, x_0 is the solution that minimizes the 2-norm of the error, and its norm is either less than or equal to the norm of any other candidate solution x.


要证明 $x = A^{+} y$ 是 ||x|| 的最小解，您可以使用 KKT 条件（Karush-Kuhn-Tucker 条件）来建立证明。在这个情况下，您想要最小化 ||x||，同时满足 $x = A^{+} y$。下面是如何使用 KKT 条件来证明 $x = A^{+} y$ 是 ||x|| 的最小解：

考虑最小化目标函数：f(x) = ||x||（即，f(x) 是 x 的 2-范数）。

我们有一个等式约束：$x = A^{+} y$。

使用 KKT 条件，我们得到以下条件：

1. 梯度条件：∇f(x) - λ(∇(x - A^{+}y)) = 0，其中 λ 是 Lagrange 乘子。

2. 稳定性条件：f(x) 在 x = A^{+}y 处是凸函数。

现在，我们来分析这些条件：

1. 梯度条件：∇f(x) = 2x，∇(x - A^{+}y) = I，其中 I 是单位矩阵。因此，梯度条件变为：2x - λI = 0。

2. 稳定性条件：我们知道 2-范数是一个凸函数，因此 f(x) = ||x|| 在整个定义域上都是凸的。

现在，考虑 Lagrange 乘子 λ 和梯度条件。由梯度条件，我们有：

2x - λI = 0

这意味着 x = (1/2λ)I。

现在，我们回到我们的目标函数 f(x) = ||x||。根据 x 的表达式，我们有：

f(x) = ||(1/2λ)I|| = (1/2λ)||I|| = 1/(2λ)

因此，我们看到当 λ 取得最小值时，f(x) = 1/(2λ) 取得最大值。这意味着我们要最小化 ||x||，必须使 λ 取得最小值。而根据 KKT 条件，λ 必须是非负的。因此，λ 最小值为 0。

当 λ = 0 时，我们得到 x = (1/2λ)I = (1/2*0)I = 0I = 0。这表明 x = A^{+}y 是 ||x|| 的最小解，因为它使目标函数取得最小值 0。

因此，我们已经证明 x = A^{+}y 是 ||x|| 的最小解。


设 X_1, ..., X_n 是从正态分布 $N(\mu, \sigma^2)$ 的总体中抽出的样本. 如果始终假设 n 为奇数, 则可以使用样本的中位数 ˜\mun 作为 \mu 的估计量, 这一估计量是渐近正态的, 满足当 n → ∞ 时，
√
n(˜\mun − \mu) (1)
依分布收敛到 N (0,
π
2
σ
2
). 而极大似然估计可以给出方差渐近地最优的结果.
(1) 推导出 \mu 的极大似然估计 ˆ\mun 的表达式.
(2) 写出当 n → ∞ 时,
√
n(ˆ\mun − \mu) 收敛到的分布.


要进行假设检验问题 **H0: σ = σ0** vs. **H1: σ ≠ σ0**，你可以仿照 Wald 检验，但使用卡方分布来替代标准正态分布，具体的步骤如下：

1. 提出原假设 (**H0**) 和备择假设 (**H1**)：
   - 原假设 (**H0**): σ = σ0
   - 备择假设 (**H1**): σ ≠ σ0

2. 收集样本数据，计算样本标准差 (**s**)。

3. 计算检验统计量 (Wald 统计量)：
   - Wald 统计量的计算方式为：
     **W = [(n - 1) * s^2] / σ0^2**
     其中，**n** 是样本容量，**s** 是样本标准差，**σ0** 是原假设中的标准差。

4. 基于卡方分布 (**χ^2**) 进行检验：
   - 在这个情况下，**Wald 统计量 W** 满足自由度为 **n - 1** 的卡方分布，即 **W ~ χ^2(n - 1)**。

5. 选择显著性水平 (**α**).

6. 根据所选择的显著性水平 (**α**) 和自由度 (**n - 1**) 查找卡方分布表格或使用统计软件，确定卡方临界值 (**χ^2_critical**)，使得 **P(χ^2 > χ^2_critical) = α/2**。

7. 判断是否拒绝原假设:
   - 如果 **W > χ^2_critical** 或 **W < 1 / χ^2_critical**，则拒绝原假设 (**H0**).
   - 如果 **W ≤ χ^2_critical** 并 **W ≥ 1 / χ^2_critical**，则无法拒绝原假设 (**H0**).

8. 根据判断的结果，得出对标准差 **σ** 的结论:
   - 如果拒绝原假设，说明在所选显著性水平下，有足够的证据表明标准差 **σ** 不等于 **σ0**.
   - 如果未能拒绝原假设，说明在所选显著性水平下，没有足够的证据表明标准差 **σ** 与 **σ0** 不同。

这样，你就可以使用卡方分布来进行关于标准差 **σ** 的假设检验，检验是否存在显著差异。

To prove that for any non-singular matrix A, there exists an upper-triangular matrix T such that TA is a unitary matrix, we can use the concept of the QR decomposition.

QR decomposition decomposes any matrix A into a product of two matrices: Q (orthogonal or unitary) and R (upper triangular). Specifically:

A = QR

Here, Q is unitary, and R is upper triangular.

Now, let's prove the statement for a non-singular matrix A:

1. Given a non-singular matrix A, perform the QR decomposition:

   A = QR

   Here, Q is unitary, and R is upper triangular.

2. We want to show that TA is unitary:

   TA = TQR

3. Since Q is unitary, we have:

   Q^H Q = I

   (Where Q^H is the conjugate transpose of Q, and I is the identity matrix).

4. Now, let's define T = Q^H. Since Q is unitary, we have:

   T = Q^H

   Then, TA becomes:

   TA = (Q^H) QR

5. Since T = Q^H and Q^H Q = I, we have:

   TA = IR

6. Any upper triangular matrix multiplied by its own conjugate transpose (in this case, R and R^H) will result in the identity matrix times a unitary matrix (IR), which is unitary itself.

So, TA is a unitary matrix, and we have successfully shown that for any non-singular matrix A, there exists an upper-triangular matrix T (in this case, T = Q^H) such that TA is a unitary matrix.

Prove : If A is a real matrix, and $A + A^T = 0$, then $(I - A)(I + A)^{-1}$ is an orthogonal matrix
\\


Let $A$ be a square matrix of order $n$ and $P_A(x)$ be the characteristic polynomial of $A$ defined as:

$P_A(x) = \det(A - xI)$,



We want to show that $P_A(A) = 0$.

Substituting $x$ with the matrix $A$ in the characteristic polynomial, we get:

$P_A(A) = \det(A - AI)$.

Now, we use the properties of determinants:

$\det(A - AI) = \det(A(I - A))$.

We can factor out $A$:

$\det(A(I - A)) = \det(A) \det(I - A)$.

Since $A$ and $I - A$ have the same size, $\det(I - A)$ is a scalar, and we can write it as $c$:

$\det(A) \cdot c$.

We need to show that $\det(A) \cdot c = 0$.

Since $c$ is a scalar, it can be written as $c = c^n$ (for a $n \times n$ matrix).

Now, we have:

$\det(A) \cdot c = \det(A) \cdot c^n$.

We know that the determinant of a matrix raised to its order is always zero (if it's not invertible):

$\det(A^n) = 0$.

Therefore, we have:

$\det(A) \cdot c = 0$.

This concludes the proof that Hamilton-Cayley theorem holds:

$P_A(A) = \det(A - AI) = \det(A) \det(I - A) = \det(A) \cdot c = 0$.
