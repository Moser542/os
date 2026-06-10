# Lemma 2.1 的完整证明

## 引理陈述

**Lemma 2.1 (强极值原理)**: 设 $u$ 是方程
$$-\Delta_m u \geq 0$$
在连通开集 $\Omega \subset \mathbb{R}^n$ 上的弱解，且 $u \geq 0$。则要么 $u \equiv 0$，要么 $u > 0$ 在 $\Omega$ 上处处成立。

这里 $\Delta_m$ 是 $m$-Laplacian 算子，定义为：
$$\Delta_m u := \operatorname{div}(|\nabla u|^{m-2} \nabla u)$$

## 所需工具

证明依赖于以下弱 Harnack 不等式：

**Lemma 3.2 (Trudinger 的弱 Harnack 不等式)**: 设 $-\Delta_m u \geq 0$ 且 $u \geq 0$ 在 $\Omega$ 中。则对所有 $\gamma \in (0, m_* - 1)$ 和任意球 $B_{2R} \subset \Omega$，存在常数 $C = C(n, m, \gamma) > 0$ 使得
$$\min_{x \in B_R} u(x) \geq C R^{-n/\gamma} \|u\|_{L^\gamma(B_{2R})}$$

其中 $B_R$ 表示半径为 $R$ 的球，$m_* = \frac{nm}{n-m}$ 是 Sobolev 共轭指数（当 $m < n$ 时）。

## 证明

**反证法架构**：我们将证明，如果 $u \not\equiv 0$，则必有 $u > 0$ 处处成立。

### 第一步：非平凡解的局部正性

**断言**: 如果 $u \not\equiv 0$，则存在某个球 $B_{2R_0} \subset \Omega$ 使得 $\|u\|_{L^\gamma(B_{2R_0})} > 0$。

**证明**: 由于 $u \not\equiv 0$，存在一个正测度集合 $E \subset \Omega$ 使得 $u > 0$ 在 $E$ 上。由于 $\Omega$ 是开集，我们可以找到一个球 $B_{2R_0} \subset \Omega$ 使得 $E \cap B_{2R_0}$ 有正测度。因此
$$\|u\|_{L^\gamma(B_{2R_0})}^\gamma = \int_{B_{2R_0}} u^\gamma dx \geq \int_{E \cap B_{2R_0}} u^\gamma dx > 0$$

### 第二步：应用弱 Harnack 不等式

对于球 $B_{2R_0}$，选择 $\gamma \in (0, m_* - 1)$。由 Lemma 3.2，我们有
$$\min_{x \in B_{R_0}} u(x) \geq C R_0^{-n/\gamma} \|u\|_{L^\gamma(B_{2R_0})}$$

由第一步，右边严格大于零，因此
$$\min_{x \in B_{R_0}} u(x) > 0$$

这表明 $u(x) > 0$ 对所有 $x \in B_{R_0}$ 成立。

### 第三步：定义正性集合

定义
$$\mathcal{P} := \{x \in \Omega : u(x) > 0\}$$

由第二步，$\mathcal{P}$ 非空（因为 $B_{R_0} \subset \mathcal{P}$）。

**$\mathcal{P}$ 是开集**: 由于 $u$ 是连续的（弱解的正则性理论保证了这一点），集合 $\mathcal{P} = u^{-1}((0, +\infty))$ 是开集。

### 第四步：$\mathcal{P}$ 是闭集（在 $\Omega$ 中）

设 $\{x_k\} \subset \mathcal{P}$ 是一个序列，且 $x_k \to x_0 \in \Omega$。我们需要证明 $x_0 \in \mathcal{P}$。

由于 $x_0 \in \Omega$，存在 $\rho > 0$ 使得 $B_{2\rho}(x_0) \subset \Omega$。

对于充分大的 $k$，$x_k \in B_\rho(x_0)$。由于 $u(x_k) > 0$ 且 $u$ 非负，我们有
$$\|u\|_{L^\gamma(B_{2\rho}(x_0))} \geq \|u\|_{L^\gamma(B_\rho(x_0))} > 0$$

（因为在 $B_\rho(x_0)$ 中有无穷多个点 $x_k$ 满足 $u(x_k) > 0$）

应用 Lemma 3.2 于球 $B_{2\rho}(x_0)$：
$$\min_{x \in B_\rho(x_0)} u(x) \geq C \rho^{-n/\gamma} \|u\|_{L^\gamma(B_{2\rho}(x_0))} > 0$$

特别地，$u(x_0) > 0$，即 $x_0 \in \mathcal{P}$。

因此 $\mathcal{P}$ 在 $\Omega$ 中是闭集。

### 第五步：连通性论证

我们已经证明：
1. $\mathcal{P} \neq \emptyset$（第二步）
2. $\mathcal{P}$ 在 $\Omega$ 中既开又闭（第三、四步）
3. $\Omega$ 是连通的（假设条件）

由连通性的定义，$\Omega$ 不能表示为两个非空不交开集的并。因此，唯一既开又闭的非空子集是 $\Omega$ 本身。

故 $\mathcal{P} = \Omega$，即 $u(x) > 0$ 对所有 $x \in \Omega$ 成立。

## 结论

综上所述，我们证明了：如果 $u$ 是 $-\Delta_m u \geq 0$ 的非负弱解且 $u \not\equiv 0$，则 $u > 0$ 在 $\Omega$ 上处处成立。

这完成了 Lemma 2.1 的证明。$\square$

## 注记

1. **正则性**: 证明隐含地使用了 $u$ 的连续性。对于 $m$-Laplacian 方程的弱解，这由 Hölder 连续性理论（如 Serrin 的 Theorem 8）保证。

2. **弱 Harnack 不等式的作用**: 该不等式是关键工具，它将积分信息（$L^\gamma$ 范数）转化为逐点信息（最小值估计）。

3. **与线性情形的比较**: 当 $m = 2$ 时，这退化为经典 Laplace 算子的强极值原理。非线性情形 ($m \neq 2$) 的证明本质上遵循相同的逻辑，但需要 Trudinger 的非线性弱 Harnack 不等式。

4. **假设的必要性**: 
   - 非负性 $u \geq 0$ 是必需的，否则弱 Harnack 不等式不适用
   - 连通性是必需的，否则 $u$ 可能在不同的连通分量上有不同的行为
