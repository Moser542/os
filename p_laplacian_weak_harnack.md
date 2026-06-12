# $p$-超解的弱 Harnack 不等式

### —— 基于 Serrin（1964）迭代方法对 $-\Delta_p u\ge 0$ 的处理

**摘要.** 设 $1<p<n$，$\Omega\subset\mathbb R^n$ 为区域。本文对 $p$-Laplace 算子的非负弱**超解**（即满足 $-\Delta_p u\ge 0$ 的弱意义解）证明弱 Harnack 不等式：存在仅依赖 $n,p,s$ 的常数 $C$，使得对任意 $0<s<\dfrac{n(p-1)}{n-p}$ 有

$$
\Bigl(\frac{1}{|B_{2R}|}\int_{B_{2R}}u^{s}\,dx\Bigr)^{1/s}\le C\,\inf_{B_R}u .
$$

证明采用 Serrin 论文《Local Behavior of Solutions of Quasi-Linear Equations》(Acta Math. 111, 1964) 中定理 5 的 Moser 迭代方法。由于仅假设超解（单边不等式），测试函数指数受限于 $\beta\le 0$，对应 Serrin 的 Case II–IV。

---

## 1. 问题陈述与 Serrin 定理 5

Serrin 处理的方程是散度型拟线性方程 $\operatorname{div}\mathcal A(x,u,u_x)=\mathcal B(x,u,u_x)$，结构条件 (6)。取

$$
\mathcal A(x,u,p)=|p|^{p-2}p,\qquad \mathcal B\equiv 0,\qquad \alpha=p,
$$

即得纯 $p$-Laplace 方程 $\Delta_p u=\operatorname{div}(|\nabla u|^{p-2}\nabla u)=0$。此时低阶系数 $b,c,d,e,f,g$ 全部为零，故 $k=0$。Serrin 定理 5 对**非负解**给出完整 Harnack 不等式

$$
\max_{S(R)}u\le C\min_{S(R)}u .
$$

他的证明用测试函数 $\phi=\eta^{\alpha}\bar u^{\beta}$，分四种情形讨论指数 $\beta$：

- **Case I** $\beta>0$：控制 $\sup u$（需要 $u$ 是下解）；
- **Case II** $1-\alpha<\beta<0$、**Case III** $\beta<1-\alpha$：负幂迭代，控制 $\inf u$；
- **Case IV** $\beta=1-\alpha$：对数估计，桥接正负指数。

本文只假设 $-\Delta_p u\ge 0$（**超解**），不假设它是下解，故 Case I 不可用。剩余的 Case II–IV 给出 $\inf u$ 下界与 $L^s$ 平均控制，这正是**弱 Harnack 不等式**。

**记号约定.** 始终设 $1<p<n$。记

$$
p^{*}=\frac{np}{n-p},\qquad \chi=\frac{p^{*}}{p}=\frac{n}{n-p}>1 .
$$

$B_\rho(z)$ 表示以 $z$ 为心、半径 $\rho$ 的开球，省略圆心时同心于固定点（取为原点）。球 $B$ 上函数 $f$ 的平均值记为

$$
\frac{1}{|B|}\int_B f\,dx .
$$

$\omega_n=|B_1(0)|$。常数 $C$ 在不同处可不同，但只依赖所标记的参数。

---

## 2. 定义与主定理

**定义 2.1（弱超解）.** 设 $u\in W^{1,p}_{\mathrm{loc}}(\Omega)$，$u\ge 0$。称 $u$ 为 $-\Delta_p u\ge 0$ 的**弱超解**，若对一切非负 $\varphi\in C_c^\infty(\Omega)$（等价地，一切非负、紧支的 $\varphi\in W^{1,p}$）有

$$
\int_\Omega |\nabla u|^{p-2}\nabla u\cdot\nabla\varphi\,dx\ \ge\ 0. \tag{2.1}
$$

直观上 $\int\nabla\varphi\cdot|\nabla u|^{p-2}\nabla u=-\int\varphi\,\Delta_p u\ge0$，即 $-\Delta_p u\ge0$ 的弱形式。

**主定理（弱 Harnack 不等式）.** 设 $1<p<n$，$u$ 是 $-\Delta_p u\ge0$ 在 $B_{4R}\subset\Omega$ 中的非负弱超解。则对任意指数

$$
0<s<\frac{n(p-1)}{n-p}=\chi(p-1)
$$

存在常数 $C=C(n,p,s)>0$，使得

$$
\boxed{\ \Bigl(\frac{1}{|B_{2R}|}\int_{B_{2R}}u^{s}\,dx\Bigr)^{1/s}\ \le\ C\,\inf_{B_{R}}u\ } \tag{WH}
$$

（其中 $\inf$ 理解为本质下确界）。

**关于指数上界 $\chi(p-1)$.** 这是最优的：取 $p$-基本解 $u(x)=|x|^{(p-n)/(p-1)}$，它在 $B_{4R}\setminus\{0\}$ 上是 $p$-调和的正函数，但在原点处 $\inf u$ 邻域行为与 $|x|^{(p-n)/(p-1)}$ 同阶。直接计算 $\int_{B_{2R}}u^s<\infty$ 当且仅当 $s\cdot\frac{n-p}{p-1}<n$，即 $s<\frac{n(p-1)}{n-p}$。超过此指数左端积分发散，(WH) 不可能成立。这与 Serrin 定理 10 中"指数 $\theta=s(\alpha-1)/(s-\alpha)$ 最优"的论断在 $s=n$（孤立点 $n$-容量为零）时完全吻合。

**归约.** 由伸缩 $u_R(y)=u(Ry)$ 把方程化到单位尺度，并由平移可设球同心于原点。故只需在 $R=1$ 下证明：$u$ 是 $B_4$ 中超解时

$$
\Bigl(\frac{1}{|B_{2}|}\int_{B_{2}}u^{s}\,dx\Bigr)^{1/s}\le C\inf_{B_1}u . \tag{2.2}
$$

又因 $-\Delta_p$ 关于常数平移不变（$\nabla(u+c)=\nabla u$），可用 $\bar u=u+\epsilon$（$\epsilon>0$）代替 $u$，使 $\bar u\ge\epsilon>0$ 处处成立，从而负幂 $\bar u^\beta$ 有界、可作测试函数；最后令 $\epsilon\to0^+$。下文一律以 $\bar u$ 记此严格正的超解，并在末尾恢复。

---

## 3. 基本能量估计（Caccioppoli 不等式）

这一节是 Serrin (14)–(18) 在纯 $p$-Laplace、$\beta\le0$ 情形的精确化。

**引理 3.1.** 设 $\bar u\ge\epsilon>0$ 是 $B_4$ 中超解，$\eta\in C_c^\infty(B_4)$，$0\le\eta\le1$。设 $\beta<0$，$\beta\ne 1-p$，记

$$
\gamma=\frac{\beta+p-1}{p},\qquad w=\bar u^{\gamma}.
$$

则存在 $C=C(n,p)$ 使得

$$
\int \eta^{p}|\nabla w|^{p}\,dx\ \le\ C\,\Bigl(\frac{|\gamma|}{|\beta|}\Bigr)^{\!p}\,\Bigl(\frac{|\gamma|}{|\beta|}\Bigr)^{\!p}\!\int |\nabla\eta|^{p}\,w^{p}\,dx. \tag{3.1}
$$

更确切地，设 $M:=1+\bigl(|\gamma|/|\beta|\bigr)^{p'}$（$p'=\frac{p}{p-1}$），则

$$
\int \eta^{p}|\nabla w|^{p}\,dx\ \le\ C\,M^{\,p-1}\!\int |\nabla\eta|^{p}\,w^{p}\,dx. \tag{3.1'}
$$

**证明.** 取测试函数

$$
\varphi=\eta^{p}\,\bar u^{\beta}.
$$

因 $\beta<0$ 而 $\bar u\ge\epsilon$，函数 $s\mapsto s^{\beta}$ 在 $[\epsilon,\infty)$ 上 Lipschitz 且有界，故 $\bar u^\beta\in W^{1,p}_{\mathrm{loc}}\cap L^\infty$，$\varphi$ 紧支于 $B_4$ 且属于 $W^{1,p}$。又 $\beta<0$ 使 $\varphi\ge0$，故 $\varphi$ 在 (2.1) 中可用：

$$
0\le\int|\nabla\bar u|^{p-2}\nabla\bar u\cdot\nabla\varphi\,dx . \tag{3.2}
$$

计算梯度

$$
\nabla\varphi=p\,\eta^{p-1}\bar u^{\beta}\,\nabla\eta+\beta\,\eta^{p}\bar u^{\beta-1}\nabla\bar u .
$$

代入 (3.2)：

$$
0\le \beta\int \eta^{p}\bar u^{\beta-1}|\nabla\bar u|^{p}\,dx
+p\int \eta^{p-1}\bar u^{\beta}|\nabla\bar u|^{p-2}\nabla\bar u\cdot\nabla\eta\,dx .
$$

由于 $\beta<0$，把负项移到左边（取绝对值 $|\beta|=-\beta$）：

$$
|\beta|\int \eta^{p}\bar u^{\beta-1}|\nabla\bar u|^{p}\,dx
\ \le\ p\int \eta^{p-1}\bar u^{\beta}|\nabla\bar u|^{p-1}|\nabla\eta|\,dx . \tag{3.3}
$$

**换元到 $w=\bar u^\gamma$.** 由 $\gamma=(\beta+p-1)/p$ 得

$$
\nabla w=\gamma\,\bar u^{\gamma-1}\nabla\bar u,\qquad
|\nabla w|^{p}=|\gamma|^{p}\,\bar u^{(\gamma-1)p}|\nabla\bar u|^{p}.
$$

注意指数 $(\gamma-1)p=\beta-1$，故

$$
\bar u^{\beta-1}|\nabla\bar u|^{p}=|\gamma|^{-p}\,|\nabla w|^{p}. \tag{3.4}
$$

同理，利用 $\beta-(\gamma-1)(p-1)=\gamma$（直接代入 $\gamma$ 的定义验证：$\beta-(\gamma-1)(p-1)=\beta-(p-1)\gamma+(p-1)$，而 $(p-1)\gamma=\frac{(p-1)(\beta+p-1)}{p}$，化简即得 $\gamma$），有

$$
\bar u^{\beta}|\nabla\bar u|^{p-1}
=\bar u^{\gamma}\cdot \bar u^{\beta-\gamma}|\nabla\bar u|^{p-1}
=w\cdot|\gamma|^{-(p-1)}|\nabla w|^{p-1}. \tag{3.5}
$$

把 (3.4)、(3.5) 代入 (3.3)：

$$
|\beta|\,|\gamma|^{-p}\!\int \eta^{p}|\nabla w|^{p}
\ \le\ p\,|\gamma|^{-(p-1)}\!\int \eta^{p-1}w\,|\nabla w|^{p-1}|\nabla\eta| .
$$

两边乘以 $|\gamma|^{p}/|\beta|$：

$$
\int \eta^{p}|\nabla w|^{p}
\ \le\ \frac{p\,|\gamma|}{|\beta|}\int \eta^{p-1}|\nabla w|^{p-1}\,\bigl(w|\nabla\eta|\bigr). \tag{3.6}
$$

**Young 不等式吸收.** 对右端用 $ab\le\delta a^{p'}+C_\delta b^{p}$（$a=\eta^{p-1}|\nabla w|^{p-1}$，$b=w|\nabla\eta|$，$p'=\frac{p}{p-1}$）：

$$
\eta^{p-1}|\nabla w|^{p-1}\cdot w|\nabla\eta|
\le \delta\,\eta^{p}|\nabla w|^{p}+C_\delta\,w^{p}|\nabla\eta|^{p},
$$

其中 $C_\delta=C(p)\,\delta^{-(p-1)}$。代入 (3.6) 并取 $\delta=\delta(p)$ 使 $\frac{p|\gamma|}{|\beta|}\delta\le\frac12$，即 $\delta\asymp |\beta|/|\gamma|$，得

$$
\tfrac12\int \eta^{p}|\nabla w|^{p}
\le \frac{p|\gamma|}{|\beta|}\,C_\delta\int w^{p}|\nabla\eta|^{p} .
$$

而 $\frac{|\gamma|}{|\beta|}C_\delta\asymp \frac{|\gamma|}{|\beta|}\cdot\bigl(\frac{|\gamma|}{|\beta|}\bigr)^{p-1}=\bigl(\frac{|\gamma|}{|\beta|}\bigr)^{p}$。但更利于迭代的写法是用 $M=1+(|\gamma|/|\beta|)^{p'}$：因 $\delta^{-(p-1)}=(|\gamma|/|\beta|)^{p-1}\cdot\text{const}$ 且 $\frac{|\gamma|}{|\beta|}\cdot(|\gamma|/|\beta|)^{p-1}=(|\gamma|/|\beta|)^p\le M^{p-1}$（因 $(|\gamma|/|\beta|)^p=\bigl((|\gamma|/|\beta|)^{p'}\bigr)^{p-1}\le M^{p-1}$），即得 (3.1′)。$\blacksquare$

---

## 4. Sobolev 步与单步反向 Hölder 不等式

把 Caccioppoli 估计与 Sobolev 不等式结合，得到 Serrin (23) 的对应形式。

**引理 4.1（Sobolev，Serrin 引理 4）.** 对紧支于 $B_4$ 的 $\psi\in W^{1,p}$，

$$
\|\psi\|_{L^{p^{*}}}\le C_S(n,p)\,\|\nabla\psi\|_{L^{p}} .
$$

对 $\psi=\eta w$ 用之（$w=\bar u^\gamma$），并由 $\nabla(\eta w)=\eta\nabla w+w\nabla\eta$ 及引理 3.1：

$$
\|\eta w\|_{p^{*}}\le C_S\bigl(\|\eta\nabla w\|_{p}+\|w\nabla\eta\|_{p}\bigr)
\le C\,M^{(p-1)/p}\,\|w\nabla\eta\|_{p}. \tag{4.1}
$$

**选取截断.** 设 $1\le \rho'<\rho\le 3$，取 $\eta$ 满足 $\eta\equiv1$ 于 $B_{\rho'}$，$\operatorname{supp}\eta\subset B_{\rho}$，$0\le\eta\le1$，$|\nabla\eta|\le \dfrac{2}{\rho-\rho'}$。代入 (4.1) 并仅在 $B_{\rho'}$ 上估计左端（那里 $\eta=1$）：

$$
\Bigl(\int_{B_{\rho'}}w^{p^{*}}\Bigr)^{1/p^{*}}
\le \frac{C\,M^{(p-1)/p}}{\rho-\rho'}\Bigl(\int_{B_{\rho}}w^{p}\Bigr)^{1/p}. \tag{4.2}
$$

**回到 $\bar u$ 的幂.** 记 $t:=\gamma p=\beta+p-1$，则 $w^{p}=\bar u^{t}$，$w^{p^{*}}=\bar u^{\chi t}$（因 $p^*\gamma=\chi p\gamma=\chi t$）。于是 (4.2) 化为

$$
\Bigl(\int_{B_{\rho'}}\bar u^{\chi t}\Bigr)^{1/(\chi t)\cdot\chi}
\le\frac{CM^{(p-1)/p}}{\rho-\rho'}\Bigl(\int_{B_{\rho}}\bar u^{t}\Bigr)^{1/t\cdot 1},
$$

即对函数

$$
\Phi(\tau,\rho):=\Bigl(\int_{B_\rho}\bar u^{\tau}\,dx\Bigr)^{1/\tau}\qquad(\tau\ne0)
$$

有，**当 $t>0$**（指数为正，开 $1/t$ 次方保序）：

$$
\Phi(\chi t,\rho')\le\Bigl[\frac{C\,M^{(p-1)/p}}{\rho-\rho'}\Bigr]^{p/t}\,\Phi(t,\rho); \tag{4.3$^+$}
$$

而**当 $t<0$**（开 $1/t$ 次方反序，且 $\chi t<t<0$）：

$$
\Phi(\chi t,\rho')\ \ge\ \Bigl[\frac{C\,M^{(p-1)/p}}{\rho-\rho'}\Bigr]^{p/t}\,\Phi(t,\rho). \tag{4.3$^-$}
$$

这里关键约束是 $\beta<0\iff t<p-1$，即 (4.3$^\pm$) 只在 $t<p-1$ 时可用。两种情形对应 Serrin：

- $t<0$（$\beta<1-p$ 或 $1-p<\beta<0$ 中 $t<0$ 那部分）→ Case III/II，向 $-\infty$ 迭代控制 $\inf$；
- $0<t<p-1$（即 $1-p<\beta<0$ 且 $\beta>1-p$ 使 $t>0$）→ Case II，正幂有限迭代到接近 $\chi(p-1)$。

**$M$ 的一致控制.** 迭代中 $\gamma=t/p$，$\beta=t-(p-1)$。
- 负向 $t\to-\infty$：$\dfrac{|\gamma|}{|\beta|}=\dfrac{|t|/p}{|t|+(p-1)}\to\dfrac1p$，故 $M$ 有界，且一致远离奇点 $t=p-1$。
- 正向 $0<t\le t_{\max}<p-1$：$|\beta|=(p-1)-t\ge (p-1)-t_{\max}>0$，故 $M\le M(n,p,t_{\max})<\infty$。

奇异指数 $t=p-1$（即 $\beta=0$）被排除，这正是 Serrin 把 $p=\alpha-1$ 设为"奇异值"、迭代时令 $p$ 避开该点的原因（他的脚注与 (39) 下方"the point $p=\alpha-1$"讨论）。

---

## 5. 负向迭代：控制 $\inf$

**引理 5.1.** 对任意固定 $s_0>0$，存在 $c_0=c_0(n,p,s_0)>0$ 使得

$$
\Phi(-s_0,\,B_3)\ \le\ c_0^{-1}\,\inf_{B_1}\bar u,
\qquad\text{即}\qquad
\inf_{B_1}\bar u\ \ge\ c_0\,\Phi(-s_0,B_3). \tag{5.1}
$$

**证明.** 取初始指数 $t_0=-s_0<0$，令

$$
t_k=\chi^{k}t_0\ (\to-\infty),\qquad
\rho_k=1+2^{1-k}\in(1,3],\quad \rho_0=3,\ \rho_k\downarrow 1 .
$$

（核验 $\rho_0=1+2=3$，$\rho_k-\rho_{k+1}=2^{1-k}-2^{-k}=2^{-k}$。）所有 $t_k<0<p-1$，故 (4.3$^-$) 在每步 $(\rho,\rho')=(\rho_k,\rho_{k+1})$、$t=t_k$ 适用，且 $\chi t_k=t_{k+1}$：

$$
\Phi(t_{k+1},\rho_{k+1})\ \ge\ A_k\,\Phi(t_k,\rho_k),\qquad
A_k:=\Bigl[\frac{C M^{(p-1)/p}}{\rho_k-\rho_{k+1}}\Bigr]^{p/t_k}. \tag{5.2}
$$

因 $t_k<0$ 而方括号 $\ge1$，故 $A_k\le1$，反向不等式 (5.2) 把较负指数的 $\Phi$ 从下界住较不负指数的 $\Phi$。迭代 $k=0,\dots,m-1$：

$$
\Phi(t_m,\rho_m)\ \ge\ \Bigl(\prod_{k=0}^{m-1}A_k\Bigr)\,\Phi(t_0,\rho_0)
=:P_m\,\Phi(-s_0,B_3). \tag{5.3}
$$

**乘积收敛.** 取对数（$\log A_k=\frac{p}{t_k}\log\frac{CM^{(p-1)/p}}{2^{-k}}$，$t_k=\chi^k t_0$）：

$$
\log P_m=\sum_{k=0}^{m-1}\frac{p}{\chi^{k}t_0}
\Bigl[\log(CM^{(p-1)/p})+k\log 2\Bigr].
$$

由 $\chi>1$，级数 $\sum_k\chi^{-k}$ 与 $\sum_k k\chi^{-k}$ 均收敛，且 $M$ 一致有界（§4），故 $\log P_m\to L>-\infty$，即 $P_m\to c_0:=e^{L}>0$，仅依赖 $n,p,s_0$。

**取极限 $m\to\infty$.** 此时 $t_m\to-\infty$，$\rho_m\downarrow1$。对固定半径 $1$ 内的负幂平均，由

$$
\Phi(t_m,\rho_m)=\Bigl(\int_{B_{\rho_m}}\bar u^{t_m}\Bigr)^{1/t_m},
$$

而 $\rho_m\downarrow1$ 使 $B_{\rho_m}\downarrow \overline{B_1}$。注意 $\bar u^{t_m}$（$t_m<0$）在 $\bar u$ 小处大，故

$$
\Bigl(\int_{B_{\rho_m}}\bar u^{t_m}\Bigr)^{1/t_m}
\ \xrightarrow[m\to\infty]{}\ \operatorname*{ess\,inf}_{B_1}\bar u .
$$

（这是 $\|f\|_{L^{q}}\to\|f\|_{L^\infty}$ 当 $q\to+\infty$ 的标准事实用于 $f=\bar u^{-1}$、$q=|t_m|$，再取倒数；半径从 $\rho_m\downarrow1$ 的收缩只使下确界不减，极限取 $B_1$ 上下确界。）于是由 (5.3)

$$
\inf_{B_1}\bar u\ \ge\ c_0\,\Phi(-s_0,B_3)\ \ge\ c_0\,\Phi(-s_0,B_2),
$$

最后一步因 $B_2\subset B_3$ 使 $\int_{B_2}\bar u^{-s_0}\le\int_{B_3}\bar u^{-s_0}$ 而 $-s_0<0$ 反序后 $\Phi(-s_0,B_2)\ge\Phi(-s_0,B_3)$……此处需小心方向，故我们保留 $B_3$ 版本 (5.1)，桥接将在 $B_3$ 上进行。$\blacksquare$

> **方向核对.** $\Phi(\tau,\rho)=(\int_{B_\rho}\bar u^\tau)^{1/\tau}$。固定 $\tau<0$，半径增大 $\rho\uparrow$ 使 $\int\bar u^\tau$ 增大，而 $1/\tau<0$ 使 $\Phi$ 减小：故 $\Phi(-s_0,B_3)\le\Phi(-s_0,B_2)$。因此 (5.1) 给出的 $\inf_{B_1}\bar u\ge c_0\Phi(-s_0,B_3)$ 是较强的；下游桥接需要的是 $\Phi(-s_0,B_3)$ 形式，正好匹配 §6 在 $B_3$ 上的 John–Nirenberg 估计。

---

## 6. 对数情形与 John–Nirenberg 桥接（Serrin Case IV）

负向迭代控制了负指数 $\Phi(-s_0,\cdot)$；正向迭代将控制正指数 $\Phi(s,\cdot)$。要把两者接起来，需要一个把 $\Phi(s_0)$ 与 $\Phi(-s_0)$（小 $s_0>0$）相连的估计。这正是 $\beta=1-p$（$t=0$）的奇异情形，对应 $v=\log\bar u$ 的 BMO 估计。

**引理 6.1（对数能量估计）.** 设 $v=\log\bar u$。对任意球 $B_\rho(z)$ 满足 $B_{2\rho}(z)\subset B_4$，有

$$
\frac{1}{|B_\rho(z)|}\int_{B_\rho(z)}|\nabla v|^{p}\,dx\ \le\ C(n,p)\,\rho^{-p}. \tag{6.1}
$$

**证明.** 取 $\beta=1-p$（$t=0$），测试函数 $\varphi=\eta^{p}\bar u^{1-p}$。仍有 $\bar u^{1-p}$ 有界（$\bar u\ge\epsilon$）、$\varphi\ge0$ 可用。梯度

$$
\nabla\varphi=p\eta^{p-1}\bar u^{1-p}\nabla\eta+(1-p)\eta^{p}\bar u^{-p}\nabla\bar u .
$$

代入 (2.1)：

$$
0\le (1-p)\int\eta^{p}\bar u^{-p}|\nabla\bar u|^{p}
+p\int\eta^{p-1}\bar u^{1-p}|\nabla\bar u|^{p-2}\nabla\bar u\cdot\nabla\eta .
$$

注意 $\nabla v=\bar u^{-1}\nabla\bar u$，故 $\bar u^{-p}|\nabla\bar u|^{p}=|\nabla v|^{p}$，$\bar u^{1-p}|\nabla\bar u|^{p-1}=|\nabla v|^{p-1}$。因 $1-p<0$，移项得

$$
(p-1)\int\eta^{p}|\nabla v|^{p}
\le p\int\eta^{p-1}|\nabla v|^{p-1}|\nabla\eta| .
$$

Young 不等式 $\eta^{p-1}|\nabla v|^{p-1}|\nabla\eta|\le \delta\eta^p|\nabla v|^p+C_\delta|\nabla\eta|^p$，取 $\delta$ 小使主项被吸收：

$$
\int\eta^{p}|\nabla v|^{p}\le C(n,p)\int|\nabla\eta|^{p} .
$$

对 $B_{2\rho}(z)$ 取 $\eta\equiv1$ 于 $B_\rho(z)$、$\operatorname{supp}\eta\subset B_{2\rho}(z)$、$|\nabla\eta|\le 2/\rho$，得 $\int_{B_\rho(z)}|\nabla v|^p\le C\rho^{-p}|B_{2\rho}|=C'\rho^{n-p}$，除以 $|B_\rho|=\omega_n\rho^n$ 即 (6.1)。

> 为使任意子球 $B_\rho(z)\subset B_3$ 的 $B_{2\rho}(z)$ 仍落在 $B_4$ 内，只需对 $B_3$ 内贴近边界的子球改用扩张因子 $1+\theta$（$\theta=1/4$）代替 $2$，结论 (6.1) 形式不变（常数随 $\theta$ 改变）。$\blacksquare$

**推论 6.2（$v\in\mathrm{BMO}$）.** 由 Poincaré 不等式，对每个 $B_\rho(z)\subset B_3$，

$$
\frac{1}{|B_\rho(z)|}\int_{B_\rho(z)}|v-v_{B_\rho(z)}|\,dx
\le C\rho\Bigl(\frac{1}{|B_\rho(z)|}\int_{B_\rho(z)}|\nabla v|^{p}\,dx\Bigr)^{1/p}
\le C(n,p),
$$

其中 $v_{B}=\dfrac{1}{|B|}\int_B v$。即 $\|v\|_{\mathrm{BMO}(B_3)}\le C_0(n,p)$。

**引理 6.3（John–Nirenberg，Serrin 引理 7）.** 若 $\|v\|_{\mathrm{BMO}(B_3)}\le C_0$，则存在 $s_0=s_0(n,p)>0$ 与 $C_1=C_1(n,p)$ 使

$$
\Bigl(\frac{1}{|B_3|}\int_{B_3}e^{\,s_0 v}\,dx\Bigr)\Bigl(\frac{1}{|B_3|}\int_{B_3}e^{-s_0 v}\,dx\Bigr)\le C_1 . \tag{6.2}
$$

**桥接.** 因 $e^{\pm s_0 v}=\bar u^{\pm s_0}$，(6.2) 即

$$
\frac{1}{|B_3|}\int_{B_3}\bar u^{\,s_0}\,dx\ \le\ C_1\Bigl(\frac{1}{|B_3|}\int_{B_3}\bar u^{-s_0}\,dx\Bigr)^{-1}.
$$

两边开方变形：

$$
\Phi(s_0,B_3)=\Bigl(\frac{1}{|B_3|}\int_{B_3}\bar u^{s_0}\,dx\Bigr)^{1/s_0}|B_3|^{1/s_0\cdot 0}\!,
$$

为简洁直接用平均值形式。由 (6.2)，

$$
\Bigl(\frac{1}{|B_3|}\int_{B_3}\bar u^{s_0}\,dx\Bigr)^{1/s_0}
\le C_1^{1/s_0}\Bigl(\frac{1}{|B_3|}\int_{B_3}\bar u^{-s_0}\,dx\Bigr)^{-1/s_0}. \tag{6.3}
$$

右端正是 $-s_0$ 的"调和型平均"，结合引理 5.1。记平均值版本

$$
\widehat\Phi(\tau,\rho):=\Bigl(\frac{1}{|B_\rho|}\int_{B_\rho}\bar u^{\tau}\,dx\Bigr)^{1/\tau},
$$

则 (6.3) 写作 $\widehat\Phi(s_0,B_3)\le C_1^{1/s_0}\,\widehat\Phi(-s_0,B_3)$。而引理 5.1 给出 $\widehat\Phi(-s_0,B_3)\le c_0^{-1}\inf_{B_1}\bar u$（把 (5.1) 中 $\Phi$ 换成 $\widehat\Phi$ 只差体积常数 $\omega_n 3^n$，吸收进常数）。于是

$$
\widehat\Phi(s_0,B_3)\ \le\ C_2(n,p)\,\inf_{B_1}\bar u . \tag{6.4}
$$

这就把一个小正指数 $s_0$ 的平均与 $\inf_{B_1}\bar u$ 连上了——已是一个弱 Harnack 不等式（指数 $s_0$）。剩下只需把指数从 $s_0$ 提升到任意 $s<\chi(p-1)$。

---

## 7. 正向有限迭代与定理证明

**引理 7.1（正幂提升）.** 设 $0<s<\chi(p-1)$。则存在 $C=C(n,p,s)$ 使

$$
\widehat\Phi(s,B_2)\ \le\ C\,\widehat\Phi(s_0,B_3), \tag{7.1}
$$

其中 $s_0=s_0(n,p)>0$ 是引理 6.3 给出的桥接指数。

**证明.** 因 $s<\chi(p-1)$，取整数 $j\ge1$ 使 $\chi^{-j}s\le s_0$（可行，因 $\chi>1$）。定义指数链

$$
\tau_i=\chi^{i}\,(\chi^{-j}s)=\chi^{\,i-j}s,\qquad i=0,1,\dots,j,
$$

则 $\tau_0=\chi^{-j}s\le s_0$，$\tau_j=s$，且 $\tau_{i+1}=\chi\tau_i$。关键核验每步起点指数 $\tau_i<p-1$ 以保证 (4.3$^+$) 可用：

$$
\tau_i\le \tau_{j-1}=\chi^{-1}s=\frac{s}{\chi}<\frac{\chi(p-1)}{\chi}=p-1.\ \checkmark
$$

（即所有用作 $t$ 的指数 $\tau_0,\dots,\tau_{j-1}$ 都 $<p-1$，最后一步把 $\tau_{j-1}$ 提到 $\chi\tau_{j-1}=s$。）

取递减半径 $\rho_i=2+2^{-i}\in(2,3]$，$\rho_0=3$，$\rho_j\downarrow 2$，$\rho_i-\rho_{i+1}=2^{-i-1}$。对每步 $i=0,\dots,j-1$ 用 (4.3$^+$)（$t=\tau_i>0$，$\chi\tau_i=\tau_{i+1}$）：

$$
\Phi(\tau_{i+1},\rho_{i+1})\le
\Bigl[\frac{CM_i^{(p-1)/p}}{\rho_i-\rho_{i+1}}\Bigr]^{p/\tau_i}\Phi(\tau_i,\rho_i),
$$

其中 $M_i=1+(|\gamma_i|/|\beta_i|)^{p'}$，$\gamma_i=\tau_i/p$，$\beta_i=\tau_i-(p-1)\in[-(p-1),\,-(p-1)+\tau_{j-1}]$，故 $|\beta_i|\ge (p-1)-\tau_{j-1}=(p-1)(1-s/(\chi(p-1)))>0$，从而 $M_i\le M_*(n,p,s)<\infty$。这是常数在 $s\to\chi(p-1)$ 时爆破的来源（与最优性一致）。

连乘 $j$ 步（$j=j(n,p,s)$ 有限）：

$$
\Phi(s,\rho_j=2)\le \Bigl(\prod_{i=0}^{j-1}[\cdots]^{p/\tau_i}\Bigr)\,\Phi(\tau_0,\rho_0=3)
= C(n,p,s)\,\Phi(\tau_0,B_3).
$$

最后把 $\Phi$ 换成平均值 $\widehat\Phi$（差体积常数），并用 $\tau_0\le s_0$ 时 $\widehat\Phi(\tau_0,B_3)\le \widehat\Phi(s_0,B_3)$（同球上 $L^q$ 平均随 $q$ 不减，Jensen），得 (7.1)。$\blacksquare$

**主定理的证明.** 串联三段估计（均在 $R=1$ 归约下，球 $\subset B_4$）：

$$
\widehat\Phi(s,B_2)
\overset{(7.1)}{\le}C\,\widehat\Phi(s_0,B_3)
\overset{(6.4)}{\le}C\,\inf_{B_1}\bar u .
$$

即

$$
\Bigl(\frac{1}{|B_2|}\int_{B_2}\bar u^{s}\,dx\Bigr)^{1/s}\le C(n,p,s)\,\inf_{B_1}\bar u .
$$

令 $\epsilon\to0^+$（$\bar u=u+\epsilon\downarrow u$，左端由单调收敛、右端由 $\inf$ 连续递减），得

$$
\Bigl(\frac{1}{|B_2|}\int_{B_2}u^{s}\,dx\Bigr)^{1/s}\le C\,\inf_{B_1}u .
$$

最后由 §2 的伸缩 $y\mapsto x/R$ 恢复一般半径，$B_1\to B_R$、$B_2\to B_{2R}$、超解域 $B_4\to B_{4R}$，即得 (WH)：

$$
\Bigl(\frac{1}{|B_{2R}|}\int_{B_{2R}}u^{s}\,dx\Bigr)^{1/s}\le C(n,p,s)\,\inf_{B_R}u . \qquad\blacksquare
$$

---

## 8. 推论与说明

**推论 8.1（强极小值原理）.** 非负 $p$-超解 $u$ 在连通区域 $\Omega$ 上若在某内点取到 $\inf=0$，则 $u\equiv0$。

*证明.* 若 $u(x_0)=\inf_\Omega u=0$，对包含 $x_0$ 的小球用 (WH)：$\bigl(\frac{1}{|B_{2R}|}\int_{B_{2R}}u^s\,dx\bigr)^{1/s}\le C\inf_{B_R}u\le C\,u(x_0)=0$，故 $u\equiv0$ 于 $B_{2R}$。连通性 + 标准链式覆盖论证给出 $u\equiv0$。$\square$

**推论 8.2（完整 Harnack）.** 若 $u$ 既是非负超解又是次解（即 $p$-调和，$\Delta_p u=0$），则可补上 Serrin Case I（$\beta>0$，正幂迭代到 $+\infty$ 得 $\sup u$ 控制），与 (WH) 合并即得完整 Harnack 不等式

$$
\sup_{B_R}u\le C\inf_{B_R}u .
$$

**说明 8.3（边界情形 $p\ge n$）.** 证明用到 Sobolev 嵌入 $W^{1,p}\hookrightarrow L^{p^*}$（$p<n$）。

- $p=n$：$\chi$ 可取任意大（$p^*$ 任意大），(WH) 对**任意** $s<\infty$ 成立，迭代用 $\tilde\alpha$-Sobolev（Serrin 定理 2、6 的修改），上界指数 $\chi(p-1)\to\infty$。
- $p>n$：由 Morrey 嵌入，$W^{1,p}_{\mathrm{loc}}\hookrightarrow C^{0,1-n/p}$，超解自动连续且局部有界，Harnack 取指数型 (Serrin 定理 9)。

**说明 8.4（低阶项）.** 若把方程换成 Serrin 的一般结构 (6)，只需在 Caccioppoli 与对数估计中携带系数项 $b,c,d,e,f,g$，用 Hölder + Sobolev 估计（如 Serrin (16) 之后逐项处理），结论变为

$$
\Bigl(\frac{1}{|B_{2R}|}\int_{B_{2R}}u^{s}\,dx\Bigr)^{1/s}\le C\bigl(\inf_{B_R}u+k\bigr),
$$

附加常数 $k$ 即 Serrin 定理 5 中的结构常数。纯 $p$-Laplace 时 $k=0$。

---

## 9. 用到的标准工具汇总

- **(S) Sobolev 不等式.** $p<n$，紧支 $\psi$：$\|\psi\|_{p^*}\le C_S\|\nabla\psi\|_p$，$p^*=np/(n-p)$。
- **(P) Poincaré 不等式.** $\dfrac{1}{|B|}\int_{B}|v-v_B|\,dx\le C\rho\bigl(\dfrac{1}{|B|}\int_B|\nabla v|^p\,dx\bigr)^{1/p}$。
- **(Y) Young 不等式.** $ab\le\delta a^{p'}+C_\delta b^{p}$，$\frac1p+\frac1{p'}=1$，$C_\delta=C(p)\delta^{-(p-1)}$。
- **(JN) John–Nirenberg 引理.** $\|v\|_{\mathrm{BMO}}\le C_0\Rightarrow$ 存在 $s_0,C_1$ 使 $\bigl(\dfrac{1}{|B|}\int_B e^{s_0v}\,dx\bigr)\bigl(\dfrac{1}{|B|}\int_B e^{-s_0v}\,dx\bigr)\le C_1$。
- **($L^q\to L^\infty$).** $\|f\|_{L^q(B)}/|B|^{1/q}\to\operatorname{ess\,sup}_B f$（$q\to\infty$）；用于负幂取倒数得 $\inf$。

---

*文献.* J. Serrin, *Local behavior of solutions of quasi-linear equations*, Acta Math. **111** (1964), 247–302. 本文是该文定理 5 在 $\mathcal A=|p|^{p-2}p$、$\mathcal B=0$、仅超解假设下的完整处理。相关现代处理另见 Trudinger (1967) 及 DiBenedetto, *Degenerate Parabolic Equations* (1993)。








