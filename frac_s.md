# 分数阶 Sobolev 空间 $W^{s,p}$（非傅里叶定义）

设 $\Omega \subset \mathbb{R}^n$，$s > 0$，令 $k = \lfloor s \rfloor$，$\theta = s - k \in (0, 1)$。

---

## 1. Gagliardo 半范定义（最常用，最直观）

当 $0 < s < 1$，$1 \leq p < \infty$：

$$W^{s,p}(\Omega) = \left\{ u \in L^p(\Omega) : \frac{|u(x) - u(y)|}{|x - y|^{\frac{n}{p} + s}} \in L^p(\Omega \times \Omega) \right\}$$

Gagliardo 半范：

$$[u]_{W^{s,p}(\Omega)} = \left( \iint_{\Omega \times \Omega} \frac{|u(x) - u(y)|^p}{|x - y|^{n + sp}} \, dx \, dy \right)^{1/p}$$

完整范数：

$$\|u\|_{W^{s,p}} = \|u\|_{L^p} + [u]_{W^{s,p}}$$

**直观解释**：这个积分衡量的是 $u$ 在两点之间的差与距离 $|x-y|^s$ 相比的增长速度。如果 $u$ 是 Hölder 连续指数 $s$ 的，这个积分收敛。

---

## 2. 一般非整数 $s = k + \theta$

先取整数阶导数，再对导数用 Gagliardo 半范：

$$W^{s,p}(\Omega) = \left\{ u \in W^{k,p}(\Omega) : D^\alpha u \in W^{\theta,p}(\Omega),\ \forall |\alpha| = k \right\}$$

范数：

$$\|u\|_{W^{s,p}} = \|u\|_{W^{k,p}} + \sum_{|\alpha| = k} [D^\alpha u]_{W^{\theta, p}}$$

---

## 3. 实插值定义（泛函分析视角）

$$W^{s,p}(\Omega) = \left(L^p(\Omega), W^{k,p}(\Omega)\right)_{\theta, p}$$

其中 $\theta = s/k \in (0,1)$，$(\cdot,\cdot)_{\theta,p}$ 是 Lions-Peetre 的 $K$-方法实插值。

$K$-泛函定义：

$$K(t, u) = \inf_{u = u_0 + u_1} \left( \|u_0\|_{L^p} + t\,\|u_1\|_{W^{k,p}} \right)$$

$$\|u\|_{(L^p, W^{k,p})_{\theta, p}} = \left( \int_0^\infty \left( t^{-\theta} K(t, u) \right)^p \frac{dt}{t} \right)^{1/p}$$

这个定义的优势是不依赖傅里叶，适用于有界域、流形等情况。

---

## 4. Slobodeckij（差商）定义

另一种等价的刻画是用**有限差分**（差分法）：

设 $\Delta_h^m u(x)$ 是 $m$ 阶差分，则 $W^{s,p}$ 可以通过条件

$$\sup_{h > 0} \frac{\|\Delta_h^m u\|_{L^p}}{h^s} < \infty$$

来刻画（需要 $m > s$）。这与 Besov 空间的定义密切相关。

---

## 5. 与 Besov 空间的关系

- $W^{s,p}$ 当 $p=2$ 时等于 $H^s$，也是 Besov 空间 $B^s_{2,2}$
- 一般 $p \neq 2$ 时，$W^{s,p} = B^s_{p,p}$
- 如果交换指标顺序得到 $B^s_{p,q}$（$q \neq p$），就是更细的 Besov 空间

---

## 嵌入定理（$W^{s,p}$ 版本）

对 $0 < s < 1$，$1 \leq p < \infty$：

- 若 $sp < n$：$W^{s,p}(\mathbb{R}^n) \hookrightarrow L^{p^*}(\mathbb{R}^n)$，其中 $p^* = \frac{np}{n-sp}$
- 若 $sp = n$：$W^{s,p}(\mathbb{R}^n) \hookrightarrow L^r(\mathbb{R}^n)$，$\forall r \in [p, \infty)$
- 若 $sp > n$：$W^{s,p}(\mathbb{R}^n) \hookrightarrow C^{0, s - n/p}(\mathbb{R}^n)$（Hölder 连续）

---

这些定义中，**Gagliardo 半范**是最直接的"不看傅里叶"的方式。它在有界域上尤其好用，积分只在 $\Omega \times \Omega$ 上做，不涉及延拓到全空间。
