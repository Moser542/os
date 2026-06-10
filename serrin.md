LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

BY

JAMES SERRIN

University of Minnesota, U.S.A.

This paper deals with the local behavior of solutions of quasi-linear partial differential equations of second order in $n \ge 2$ independent variables. We shall be concerned specifically with the *a priori* majorization of solutions, the nature of removable singularities, and the behavior of a positive solution in the neighborhood of an isolated singularity. Corresponding results are for the most part well known for the case of the Laplace equation; roughly speaking, our work constitutes an extension of these results to a wide class of non-linear equations.

Throughout the paper we are concerned with real quasi-linear equations of the general form

$$
\operatorname{div} \mathcal{A}(x, u, u_x) = \mathcal{B}(x, u, u_x). \quad (1)
$$

Here $\mathcal{A}$ is a given vector function of the variables $x, u, u_x$, $\mathcal{B}$ is a given scalar function of the same variables, and $u_x = (\partial u/\partial x_1, \dots, \partial u/\partial x_n)$ denotes the gradient of the dependent variable $u = u(x)$, where $x = (x_1, \dots, x_n)$. The structure of (1) is determined by the functions $\mathcal{A}(x, u, p)$ and $\mathcal{B}(x, u, p)$. We assume that they are defined for all points $x$ in some connected open set (domain) $\Omega$ of the Euclidean number space $E^n$, and for all values of $u$ and $p$. Furthermore, they are to satisfy inequalities of the form

$$
\left. \begin{array}{l} |\mathcal{A}| \le a |p|^{\alpha-1} + b |u|^{\alpha-1} + e, \\ |\mathcal{B}| \le c |p|^{\alpha-1} + d |u|^{\alpha-1} + f, \\ p \cdot \mathcal{A} \ge a^{-1} |p|^{\alpha} - d |u|^{\alpha} - g. \end{array} \right\} \quad (2)
$$

Here $\alpha > 1$ is a fixed exponent, $a$ is a positive constant, and the coefficients $b$ through $g$ are measurable functions of $x$, contained in certain definite Lebesgue classes over $\Omega$ (see Chapter I).

---

JAMES SERRIN

The generality of these assumptions naturally requires that equation (1) be interpreted in a weak sense. Let $D$ be a subdomain of $\Omega$, and let $u$ be a function having strong derivatives $u_x$ which are locally of class $L_\alpha$ over $D$. Then $u$ will be called a *weak solution* (or simply a *solution*) of (1) in $D$ if

$$
\int (\phi_x \cdot \mathcal{A} + \phi \mathcal{B}) dx = 0 \quad (3)
$$

for any continuously differentiable function $\phi = \phi(x)$ with compact support in $D$. Obviously any function which satisfies (1) in the classical sense would be a solution in the sense just defined, though of course not conversely.

Before turning to a description of results, it is worth noting that the above structure includes linear elliptic equations, where $\alpha=2$, and also the Euler equations of a wide class of regular as well as non-regular variational problems. The reader may consult reference [22], where this observation is made more explicit.

The main body of the paper is divided into three chapters. In Chapter I we consider various *a priori* estimates concerning the majorization of solutions. To begin with, Theorem 1 states that a solution $u$ in $D$ is essentially bounded on any compact subset $D'$ of $D$, the bound depending only on the structure of (1), on the $L_\alpha$ norm of $u$ over $D$, and on the geometry of $D$ and $D'$. If $u$ is continuous in the closure of $D$, one can further estimate the maximum of $u$ in terms of its $L_\alpha$ norm together with the maximum of its boundary values (Theorem 3). The most important result of the first chapter is an inequality of Harnack type, Theorem 5, which generalizes to non-linear equations a recent result of Moser for linear equations. This theorem is basic for much of the following work. Finally, in Theorem 8 we show that solutions of (1) are necessarily Hölder continuous, possibly after redefinition on a set of measure zero. A more detailed outline of the contents of this chapter is impossible here; the reader is referred directly to the paper for more specific conclusions.

The proofs are based on the iteration technique introduced by Moser in references [16] and [17], and at the same time make strong use of the general Sobolev inequalities. We must also remark on the papers of Stampacchia, Morrey, and Ladyzhenskaya and Uraltseva, whose spirit is much the same as that of the first chapter here. In particular, Ladyzhenskaya and Uraltseva have proved by quite different methods the Hölder continuity of bounded solutions of (1), under conditions rather similar to (2).

The second chapter deals with the general problem of removable singularities. If we consider Laplace's equation, it is known that a set of capacity zero constitutes a removable singularity for a bounded harmonic function, while, on the other hand, a

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

249

single point is removable provided only that the solution is $o(\log r)$ or $o(r^{2-n})$ in the neighborhood. For sets of intermediate size a corresponding removable singularity theorem was recently discovered by Carleson [1, p. 78], the idea there being to relate the Hausdorff dimension of the singular set to the Lebesgue class of the solution. The following result extends Carleson's theorem to all equations of the general form (1), (2).

Let $Q$ be a compact set of $s$-capacity zero, (1) where $\alpha \le s \le n$, and let $D$ be a domain in $\Omega$. Suppose that $u$ is a continuous solution of (1) in the set $D-Q$, and that

$$
u \in L_{\theta(1+\delta)},
$$

where $\theta = s(\alpha - 1)/(s - \alpha)$ and $\delta$ is some positive number. Then $u$ can be defined on the set $Q$ so that the resulting function is a continuous solution of (1) in the entire domain $D$.

In order to see this result more clearly, let us consider its implications for the Laplace equation (where $\alpha=2$). When $n=2$ nothing new is obtained, for then $s=2$ and we simply regain the result that a set of ordinary capacity zero is removable for a bounded ($L_\infty$) solution. When $n>2$, however, $s$ can vary from 2, where we obtain the usual result, to $n$, where we get the result that a set of $n$-capacity zero is removable provided that $u \in L_{n/(n-2)+\delta}$. Since a single point has $n$-capacity zero, this case of the theorem is seen to be associated with the usual growth condition at an isolated singularity. In other words, when $n>2$ the above result constitutes an interpolation theorem of the desired sort. (Actually our result is not quite as sharp for Laplace's equation as the one obtained by Carleson, though, of course, it does apply to a larger class of equations. We add that our work was done independently of Carleson's, and that the overlap was discovered only after the manuscript had been submitted for publication. Other work of a similar nature is due to Picone [19].)

In addition to the above result we shall also prove the following removable singularity theorem, which has the advantage of a considerably less abstract hypothesis.

Let $Q$ be a smooth manifold of dimension $m \le n - \alpha$, and let $D$ be a domain in $\Omega$. Suppose that $u$ is a continuous solution of (1) in the set $D-Q$, and that

$$
\begin{aligned} u \in L_{\theta(1+\delta)} & \quad \text{if } m < n - \alpha, \\ u = O(|\log \xi|^{1-\delta}) & \quad \text{if } m = n - \alpha, \end{aligned}
$$

where $\theta = (n-m)(\alpha-1)/(n-m-\alpha)$, $\delta$ is some positive number, and $\xi$ is the distance from $Q$. Then $u$ can be defined on $Q$ so that the resulting function is a continuous solution of (1) in all of $D$.

(1) Cf. Section 7. We note that any non-empty set has positive $(n+\varepsilon)$-capacity, so that only values $s \le n$ need be considered.

---

JAMES SERRIN

The preceding theorems raise obvious questions concerning the existence of solutions of (1) having non-removable singularities. In Chapter III we investigate this problem in considerably more detail for the special equation

$$
\operatorname{div} \mathcal{A}(x, u, u_x) = 0 \quad (\alpha \le n). \qquad (4)
$$

It is shown that at an isolated singularity a positive solution of (4) has precisely the order of growth $r^{(\alpha-n)/(\alpha-1)}$ if $\alpha < n$ and $\log 1/r$ if $\alpha = n$. (1) For linear equations of the special form $(a_{ij}(x) u_{,i}, j=0)$ a corresponding result is due to Royden [20]; cf also [10, 17]. A weaker version for the non-linear case was given earlier by the author [21]. Our present proof is basically the same as in [20], though the reader will see that the idea there serves only as a theme upon which numerous variations have been played. We may also mention that in the case of linear equations of the general form $a_{ij}u_{,ij} + b_i u_{,i} = 0$ there are corresponding isolated singularity theorems, requiring however, some continuity of the coefficients, and not necessarily providing an explicit order of growth at the singularity [3, 4, 6].

In Section 13 we show under suitable conditions that there exist solutions of (4) with precisely the behavior indicated above. A corresponding result for linear equations is due to Littman, Stampacchia, and Weinberger. The final section of the paper contains some further results for linear equations. Although these theorems are quite special in comparison with the rest of the work in the paper, they have an interest in their own right, and indicate to some extent the underlying differences between linear and non-linear equations.

I wish finally to thank Professor Hans Weinberger for his interest in this work, and for several quite helpful suggestions.

I. Majorization of solutions

In this chapter we shall consider various *a priori* estimates for solutions of the equation

$$
\operatorname{div} \mathcal{A}(x, u, u_x) = \mathcal{B}(x, u, u_x). \qquad (5)
$$

It will be assumed that the functions $\mathcal{A}(x, u, p)$ and $\mathcal{B}(x, u, p)$ are defined for all values of $u$ and $p$, and for all points $x$ in some fixed domain $\Omega$. Moreover, we suppose that they satisfy inequalities of the form

(1) An explicit example is provided by the equation

$$
\operatorname{div} (u_x | u_x|^{\alpha-2}) = 0,
$$

which has the solutions $Ar^{(\alpha-n)/(\alpha-1)} + B$ and $A \log r + B$ when $\alpha \neq n$ and $\alpha = n$ respectively.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

251

$$
\left. \begin{aligned} |\mathcal{A}| &\le a |p|^{\alpha-1} + b |u|^{\alpha-1} + e, \\ |\mathcal{B}| &\le c |p|^{\alpha-1} + d |u|^{\alpha-1} + f, \\ p \cdot \mathcal{A} &\ge |p|^{\alpha} - d |u|^{\alpha} - g, \end{aligned} \right\} \quad (6)
$$

for $x \in \Omega$ and all values of $u$ and $p$. Here $\alpha > 1$ is a fixed exponent, $a$ is a positive constant, and $b$ through $g$ are measurable functions on $\Omega$ (the slightly simpler form of (6), as compared with (2), can be achieved by a simple normalization). If $1 < \alpha < n$ we assume that $b$ through $g$ are in the respective Lebesgue classes

$$
b, e \in L_{n/(\alpha-1)}; \quad c \in L_{n/(1-\varepsilon)}; \quad d, f, g \in L_{n/(\alpha-\varepsilon)}, \quad (7)
$$

$\varepsilon$ being some positive number less than or equal to one. If $\alpha = n$ we suppose that $b$ through $g$ satisfy

$$
b, e \in L_{n/(n-1-\varepsilon)}; \quad c \in L_{n/(1-\varepsilon)}; \quad d, f, g \in L_{n/(n-\varepsilon)}, \quad (8)
$$

again with $\varepsilon$ some positive number less than or equal to one. Since the remaining case $\alpha > n$ is somewhat anomalous, we shall discuss it separately in Section 5. In any event, the discrepancy between the conditions required for the various cases $1 < \alpha < n$, $\alpha = n$, and $\alpha > n$ seems to be an essential part of the situation. Finally, certain alternative hypotheses will be considered in the concluding section of the chapter.

Now let $D$ be a subdomain of $\Omega$, and let $u = u(x)$ be a function having strong derivatives which are locally of class $L_\alpha$ over $D$. As already explained in the introduction, $u$ will be called a *solution* of (5) in $D$ if

$$
\int (\phi_x \cdot \mathcal{A} + \phi \mathcal{B}) dx = 0 \quad (9)
$$

for any continuously differentiable function $\phi = \phi(x)$ with compact support in $D$. In writing equation (9) it is tacitly assumed that the functions $\mathcal{A} = \mathcal{A}(x, u, u_x)$ and $\mathcal{B} = \mathcal{B}(x, u, u_x)$ are measurable, as will certainly be the case in all reasonable situations. Since $u_x$ is locally in $L_\alpha$, it follows that also

$$
u \in \begin{cases} L_{\alpha^*} & \text{if } \alpha < n, \\ L_\sigma & \text{if } \alpha = n \end{cases}
$$

locally in $D$, where $\alpha^* = \alpha n/(n - \alpha)$ is the Sobolev conjugate of $\alpha$, and $\sigma$ is any positive real number. Thus, using assumptions (7) and (8), it is a straightforward consequence of Hölder's inequality that $\mathcal{A}(x, u, u_x)$ is locally in $L_{\alpha/(\alpha-1)}$ while $\mathcal{B}(x, u, u_x)$ is locally in $L_{(\alpha^*)'}$ if $\alpha < n$, or locally in $L_{1+\delta}$ if $\alpha = n$, where $(\alpha^*)'$ is the Hölder conjugate of $\alpha^*$,

---

252

JAMES SERRIN

and $\delta = \varepsilon/2(n - \varepsilon)$. It follows therefore that if $u$ is a solution of (5), then (9) holds not only for continuously differentiable functions $\phi$, but in fact for any $\phi$ with strong derivatives in $L_\alpha$ and with compact support in $D$. This remark will be of considerable importance later on.

## 0. Preliminary lemmas

The theorems of the following sections require some preparatory results which we group together here.

LEMMA 1. Let $a_i$, $i=1, \dots, N$, be non-negative real numbers, and let $\alpha$ be a positive exponent. Then

$$
\lambda \sum a_i^\alpha \le (\sum a_i)^\alpha \le \Lambda \sum a_i^\alpha,
$$

where $\lambda = \text{Min}(1, N^{\alpha-1})$ and $\Lambda = \text{Max}(1, N^{\alpha-1})$.

Proof. We may assume without loss of generality that $\alpha \ne 1$ and $\sum a_i = 1$. The maximum of the quantity $\sum a_i^\alpha$ is then easily found to occur either when all the $a_i$ are equal, or (endpoint maximum) when all but one $a_i$ are zero. This proves the left-hand inequality. The right-hand result is obtained the same way.

LEMMA 2. Let $\alpha$ be a positive exponent, and let $a_i, \beta_i$, $i=1, \dots, N$, be two sets of $N$ real numbers such that $0 < a_i < \infty$ and $0 \le \beta_i < \alpha$. Suppose that $z$ is a positive number satisfying the inequality

$$
z^\alpha \le \sum a_i z^{\beta_i}.
$$

Then

$$
z \le C \sum (a_i)^{\gamma_i},
$$

where $C$ depends only on $N$, $\alpha$, and $\beta_i$, and where $\gamma_i = (\alpha - \beta_i)^{-1}$.

Proof. We make use of Young's inequality

$$
ab \le \frac{1}{p} a^p + \frac{1}{q} a^q,
$$

where $1/p + 1/q = 1$. Then if $0 < \beta < \alpha$ and $a > 0$ we have

$$
az^\beta = \left(\frac{a}{\varepsilon}\right) \cdot (\varepsilon z^\beta) \le \frac{\beta}{\alpha} (\varepsilon z^\beta)^{\alpha/\beta} + \frac{\alpha - \beta}{\alpha} \left(\frac{a}{\varepsilon}\right)^{\alpha/(\alpha - \beta)}
$$

Putting $\varepsilon = (\alpha/2N\beta)^{\beta/\alpha}$ yields therefore

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

253

$$
az^{\beta} \le (1/2N) z^{\alpha} + (2Na)^{\alpha/(\alpha-\beta)}. \qquad (10)
$$

Note also that (10) holds trivially when $\beta=0$. Now applying (10) to each term of the sum $\sum a_i z^{\beta_i}$, we obtain at once

$$
z^{\alpha} \le \sum \{1/2N) z^{\alpha} + (2Na_i)^{\alpha/(\alpha-\beta_i)}\},
$$

whence by transposition there arises

$$
z^{\alpha} \le 2 \sum (2Na_i)^{\alpha \gamma_i}.
$$

The required conclusion follows immediately from Lemma 1.

The next four lemmas are general calculus inequalities, due basically to Sobolev and Morrey. A simple proof of Lemmas 3 and 4 is given in reference [18], and Lemma 5 can be obtained by quite similar methods. Although Lemma 6 is essentially well-known, we include a proof for completeness.

Now let $\psi = \psi(x)$ be a measurable function on an open set $D$, and let $p$ be a real number, $1 \le p \le \infty$. The $L_p$ norm of $\psi$ is defined by

$$
\|\psi\|_{p,D} = \left( \int_D |\psi|^p dx \right)^{1/p}, \quad (p < \infty); \quad \|\psi\|_{\infty,D} = \text{ess sup}_D |\psi|.
$$

For simplicity we shall write $\|\psi\|_p$ rather than $\|\psi\|_{p,D}$ when the domain $D$ is apparent from the context.

LEMMA 3 (Morrey). Let $\psi$ be a strongly differentiable function on the unit ball $|x| < 1$, and suppose that $\|\psi_x\|_{\alpha}$ is finite for some $\alpha > n$. Then $\psi$ is (essentially) Hölder continuous, with

$$
|\psi(x) - \psi(y)| \le \text{Const.} |x - y|^{1-n/\alpha} \|\psi_x\|_{\alpha},
$$

the constant depending only on $\alpha$ and $n$.

LEMMA 4 (Sobolev). Let $\psi$ be a strongly differentiable function with compact support in $E^n$, and suppose that $\|\psi_x\|_{\alpha}$ is finite for some $\alpha < n$. Set $\alpha^* = \alpha n/(n - \alpha)$. Then $\psi$ is in $L_{\alpha^*}$ and

$$
\|\psi\|_{\alpha^*} \le \text{Const.} \|\psi_x\|_{\alpha},
$$

where the constant depends only on $\alpha$ and $n$.

In the next lemma, we use $\varrho$ to denote the distance from a point $x$ to the hyperplane $x_1 = \dots = x_s = 0$, $1 \le s \le n$, while $\sigma$ is some fixed positive number.

---

254

JAMES SERRIN

LEMMA 5. Let $\psi$ be a strongly differentiable function defined in the domain $\varrho > \sigma$ and having compact support in $E^n$. Suppose that $\|\psi_x\|_\alpha$ is finite for some $\alpha < n$. Then $\psi$ is in $L_{\alpha^*}$ and

$$
\|\psi\|_{\alpha^*} \leqslant \text{Const. } \|\psi_x\|_\alpha
$$

the constant depending only on $\alpha$ and $n$.

LEMMA 6. Let $\psi$ be a strongly differentiable function defined in an open ball $S$ of radius $h$. Then if $\psi_S \equiv |S|^{-1} \int_S \psi \, dx$, we have

$$
\|\psi - \psi_S\|_1 \leqslant \text{Const. } h \|\psi_x\|_1,
$$

the constant depending only on $n$.

Proof. Let $x$ and $y$ be two points in $S$, and set $\varrho = |x - y|$. Then, assuming that $\psi \in C^1$, we have

$$
\psi(y) - \psi(x) = \int_0^\varrho (\partial\psi/\partial\varrho') \, d\varrho' \leqslant \int_0^{2h} |\psi_x| \, d\varrho'
$$

(setting $|\psi_x| \equiv 0$ at points outside $S$). Multiplying both sides by $dy = \varrho^{n-1} d\varrho \, d\omega$ and integrating over $S$ yields

$$
|S| \cdot |\psi_S - \psi(x)| \leqslant \frac{(2h)^n}{n} \iint |\psi_x| \, d\varrho' \, d\omega = \frac{(2h)^n}{n} \int_S |\psi_x| \, \varrho^{-n+1} \, dy.
$$

Then by the well-known convolution inequality of Young,

$$
|S| \cdot \|\psi_S - \psi\|_1 \leqslant \frac{(2h)^n}{n} \|\psi_x\|_1 \cdot \|\varrho^{-n+1}\|_1 = \text{Const. } h^{n+1} \|\psi_x\|_1.
$$

This completes the proof when $\psi$ is continuously differentiable. The general case follows by standard approximation arguments.

The final lemma is due to John and Nirenberg. Its use in connection with the *a priori* estimation of solutions of differential equations already occurs in the paper of Moser which we have discussed in the introduction.

LEMMA 7. Let $\psi$ be a summable function on the unit ball $S_0$, and suppose that

$$
\int_S |\psi - \psi_S| \, dx \leqslant |S|
$$

for every open ball $S \subset S_0$. Then there exist constants $\lambda$ and $\mu$, depending only on $n$, such that

$$
\int_{S_0} e^{\lambda\psi} \, dx \cdot \int_{S_0} e^{-\lambda\psi} \, dx \leqslant \mu^2. \qquad (11)
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

255

The conclusion of the theorem of John and Nirenberg is actually that

$$
\int_{S_0} e^{\lambda|\psi-\psi_0|} dx \le \mu,
$$

but (11) is an immediate consequence of this inequality.

We close the section by noting a useful derivation rule in the theory of strong differentiation. Let $G$ be a piecewise smooth function of the real variable $u$, $-\infty < u < +\infty$, with corners at the points $l_1, \dots, l_N$. Suppose also that $G$ satisfies a uniform Lipschitz condition. Then if $u(x)$ is strongly differentiable in a domain $D$, the composite function $G(u(x))$ is also strongly differentiable in $D$, and

$$
G(u)_x = \begin{cases} G'(u) u_x, & \text{where } u \neq l_1, \dots, l_N, \\ 0, & \text{where } u = l_1, \dots, l_N. \end{cases} \quad (12)
$$

Formula (12) of course defines only a particular representative of $G(u)_x$, as is only natural since strong derivatives are, technically, equivalence classes of measurable functions. In particular, changing $u$ and $u_x$ on a set of measure zero alters the representative but not the equivalence class.

An interesting consequence of (12) is that the strong derivative of a function $u$ is zero almost everywhere on any set where $u$ is constant. Indeed set

$$
G(u) = \text{Max}(0, u), \quad H(u) = \text{Min}(0, u),
$$

and note that

$$
u = G(u) + H(u), \quad u_x = G(u)_x + H(u)_x.
$$

Evaluating the second relation on the set where $u=0$ yields the desired conclusion for the case when the constant is zero. The general result follows at once.

1. Majorization of $|u|$

We shall show in this section that weak solutions of (5) are locally bounded. This is of course obvious in case $\alpha > n$ by virtue of Lemma 3. The remaining cases are considerably more difficult, and will be treated separately.

Let $P$ be a fixed point in the basic domain $\Omega$, and let $S(R)$ denote the open ball of radius $R$ centered at $P$. For simplicity we use the symbol $\| \cdot \|_{p,R}$ to denote the $L_p$ norm of a function over $S(R)$.

**THEOREM 1.** Let $u$ be a weak solution of equation (5) defined in some ball $S(2R) \subset \Omega$. Suppose that $\alpha < n$ and that conditions (6) and (7) hold. Then

17-642946 Acta mathematica. 111. Imprimé le 8 juin 1964

---

256

JAMES SERRIN

$$
\|u\|_{\infty, R} \le CR^{-n/\alpha} (\|u\|_{\alpha, 2R} + kR^{n/\alpha})
$$

and

$$
\|u_x\|_{\alpha, R} \le CR^{-1} (\|u\|_{\alpha, 2R} + kR^{n/\alpha}),
$$

where $C$ and $k$ are constants depending only on the structure of (5). In particular

$$
C = C(\alpha, n, \varepsilon; a, \|b\|, R^\varepsilon \|c\|, R^\varepsilon \|d\|),
$$

$$
k = (\|e\| + R^\varepsilon \|f\|)^{1/(\alpha-1)} + (R^\varepsilon \|g\|)^{1/\alpha},
$$

the norms of the coefficients $b$ through $g$ being taken in the respective Lebesgue spaces (7).

*Proof.* We consider first the case when $R=1$, with the solution correspondingly defined in the open ball $S(2) \subset \Omega$. Set

$$
\bar{u} = |u| + k, \quad x \in S(2),
$$

where $k = (\|e\| + \|f\|)^{1/(\alpha-1)} + \|g\|^{1/\alpha}$. Then obviously

$$
\left. \begin{aligned} |\mathcal{A}| &\le a |p|^{\alpha-1} + \bar{b} |\bar{u}|^{\alpha-1}, \\ |\mathcal{B}| &\le c |p|^{\alpha-1} + \bar{d} |\bar{u}|^{\alpha-1}, \\ p \cdot \mathcal{A} &\ge |p|^{\alpha} - \bar{d} |\bar{u}|^{\alpha}, \end{aligned} \right\} \quad (13)
$$

with $\bar{b} = b + k^{1-\alpha} e$, $\bar{d} = d + k^{1-\alpha} f + k^{-\alpha} g$. Moreover, the norms of $\bar{b}$ and $\bar{d}$ are bounded,

$$
\|\bar{b}\| \le \|b\| + 1, \quad \|\bar{d}\| \le \|d\| + 2.
$$

The proof now rests on an appropriate choice of the test function in relation (9).

For fixed numbers $q \ge 1$ and $l > k$ we define the functions

$$
F(\bar{u}) = \begin{cases} \bar{u}^q & \text{if } k \le \bar{u} \le l, \\ q l^{q-1} \bar{u} - (q-1) l^q & \text{if } l \le \bar{u}, \end{cases}
$$

and

$$
G(u) = \operatorname{sign} u \cdot \{F(\bar{u}) F'(\bar{u})^{\alpha-1} - q^{\alpha-1} k^{\beta}\}, \quad -\infty < u < \infty,
$$

where $q$ and $\beta$ are related by $\alpha q = \alpha + \beta - 1$. Evidently $F$ is a continuously differentiable function of the variable $\bar{u}$, which is linear beyond the "cutoff" value $l$. Similarly $G$ is a piecewise smooth function of $u$, with corners at $u = \pm (l-k)$. Now let $\eta = \eta(x)$ be a non-negative smooth function with compact support in $S(2)$, and put

$$
\phi(x) = \eta^{\alpha} G(u), \quad (u = u(x)).
$$

Since $G$ is linear in $u$ for $|u| > l-k$, it follows from the preceding section that $\phi$ has strong derivatives in $L_\alpha$. Thus $\phi$ is admissible in (9).

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

257

Now in the set where $|u| \neq l-k$ we have obviously

$$
\phi_x = \alpha \eta^{\alpha-1} \eta_x G + \eta^{\alpha} G' u_x,
$$

with

$$
G' = \begin{cases} q^{-1} \beta(F')^{\alpha} & \text{if } |u| < l-k, \\ (F')^{\alpha} & \text{if } |u| > l-k. \end{cases}
$$

Therefore, using (13) and the fact that $|G| \leqslant F(F')^{\alpha-1}$ one has

$$
\begin{aligned} \phi_x \cdot \mathcal{A} + \phi \mathcal{B} &\geqslant \eta^{\alpha} G' \{|u_x|^{\alpha} - \bar{d} |\bar{u}|^{\alpha}\} - \alpha \eta^{\alpha-1} |\eta_x G| \{a |u_x|^{\alpha-1} + \bar{b} |\bar{u}|^{\alpha-1}\} \\ &\quad - \eta^{\alpha} |G| \{c |u_x|^{\alpha-1} + \bar{d} |\bar{u}|^{\alpha-1}\} \\ &\geqslant |\eta F' \bar{u}_x|^{\alpha} - \alpha a |\eta_x F| \cdot |\eta F' \bar{u}_x|^{\alpha-1} - \alpha \bar{b} |\eta_x F| \cdot |\eta F' \bar{u}_x|^{\alpha-1} - c \eta F |\eta F' \bar{u}_x|^{\alpha-1} \\ &\quad - \bar{d} \{q^{-1} \beta |\eta F' \bar{u}_x|^{\alpha} + \eta F |\eta F' \bar{u}_x|^{\alpha-1}\}, \end{aligned} \quad (14)
$$

valid wherever $|u| \neq l-k$. (1) The last inequality may be further simplified by setting $v = v(x) = F(\bar{u})$. Since $\bar{u}F' \leqslant qF$ we get

$$
\begin{aligned} \phi_x \cdot \mathcal{A} + \phi \mathcal{B} &\geqslant |\eta v_x|^{\alpha} - \alpha a |\eta_x v| \cdot |\eta v_x|^{\alpha-1} - \alpha q^{\alpha-1} \bar{b} |\eta_x v| \cdot (\eta v)^{\alpha-1} \\ &\quad - c \eta v |\eta v_x|^{\alpha-1} - (1+\beta) q^{\alpha-1} \bar{d}(\eta v)^{\alpha}. \end{aligned} \quad (15)
$$

In the set where $|u| = l-k$ we have $\phi_x = \alpha \eta^{\alpha-1} \eta_x G$ and $u_x = \bar{u}_x = 0$ (a.e.), so that (15) holds also on this set. We may therefore integrate (15) over $S(2)$, with the result

$$
\begin{aligned} \|\eta v_x\|_{\alpha}^{\alpha} &\leqslant \alpha a \int |\eta_x v| \cdot |\eta v_x|^{\alpha-1} dx + \alpha q^{\alpha-1} \int \bar{b} |\eta_x v| \cdot (\eta v)^{\alpha-1} dx \\ &\quad + \int c \eta v |\eta v_x|^{\alpha-1} dx + (1+\beta) q^{\alpha-1} \int \bar{d}(\eta v)^{\alpha} dx. \end{aligned} \quad (16)
$$

Here for simplicity we have written $\| \cdot \|_{\alpha}$ rather than $\| \cdot \|_{\alpha, 2}$.

The terms on the right-hand side of the preceding inequality can be estimated by using Hölder's inequality together with Lemma 4. Thus

$$
\begin{aligned} \int |\eta_x v| \cdot |\eta v_x|^{\alpha-1} dx &\leqslant \|\eta_x v\|_{\alpha} \|\eta v_x\|_{\alpha}^{\alpha-1}, \\ \int \bar{b} |\eta_x v| \cdot (\eta v)^{\alpha-1} dx &\leqslant \|\bar{b}\|_{n/(\alpha-1)} \|\eta_x v\|_{\alpha} \|\eta v\|_{\alpha}^{\alpha-1} \\ &\leqslant C \|\eta_x v\|_{\alpha} \|(\eta v)_x\|_{\alpha}^{\alpha-1} \\ &\leqslant C \{\|\eta_x v\|_{\alpha}^{\alpha} + \|\eta_x v\|_{\alpha} \|\eta v_x\|_{\alpha}^{\alpha-1}\}. \end{aligned}
$$

(1) The substitution $|u_x| = |\bar{u}_x|$ is obviously valid in the set where $|u| \neq 0$. It also holds when $u=0$, since $u_x=0$ almost everywhere on this set.

---

258

JAMES SERRIN

The letter $C$ here denotes a constant (which usually changes from one line to the next) depending only on the quantities listed in the statement of the theorem. Similarly

$$
\begin{align*}
\int c \eta v |\eta v_x|^{\alpha-1} dx &= \int c (\eta v)^\varepsilon (\eta v)^{1-\varepsilon} |\eta v_x|^{\alpha-1} dx \\
&\le \|c\|_{n/(1-\varepsilon)} \|\eta v\|_\alpha^\varepsilon \|\eta v\|_{\alpha^*}^{1-\varepsilon} \|\eta v_x\|_\alpha^{\alpha-1} \\
&\le C \|\eta v\|_\alpha^\varepsilon \{ \|\eta_x v\|_\alpha^{1-\varepsilon} \|\eta v_x\|_\alpha^{\alpha-1} + \|\eta v_x\|_\alpha^{\alpha-\varepsilon} \},
\end{align*}
$$

and

$$
\begin{align*}
\int \bar{d}(\eta v)^\alpha dx &= \int \bar{d}(\eta v)^\varepsilon (\eta v)^{\alpha-\varepsilon} dx \\
&\le \|\bar{d}\|_{n/(\alpha-\varepsilon)} \|\eta v\|_\alpha^\varepsilon \|\eta v\|_{\alpha^*}^{\alpha-\varepsilon} \\
&\le C \|\eta v\|_\alpha^\varepsilon \{ \|\eta_x v\|_\alpha^{\alpha-\varepsilon} + \|\eta v_x\|_\alpha^{\alpha-\varepsilon} \}.
\end{align*}
$$

If the four previous estimates are inserted into the right-hand side of (16), and we set

$$
z = \|\eta v_x\|_\alpha / \|\eta_x v\|_\alpha, \quad \zeta = \|\eta v\|_\alpha / \|\eta_x v\|_\alpha,
$$

the result may be written

$$
z^{\alpha} \le C[z^{\alpha-1} + q^{\alpha-1}(1+z^{\alpha-1}) + \zeta^{\varepsilon}(z^{\alpha-1} + z^{\alpha-\varepsilon}) + (1+\beta)q^{\alpha-1}\zeta^{\varepsilon}(1+z^{\alpha-\varepsilon})]. \quad (17)
$$

Applying Lemma 2 and simplifying the result, one obtains (since $1 + \beta \le (\alpha + 1)q$)

$$
z \le C q^{\alpha/\varepsilon} (1 + \zeta),
$$

or in terms of the original quantities

$$
\| \eta v_x \|_\alpha \le C q^{\alpha/\varepsilon} (\| \eta v \|_\alpha + \| \eta_x v \|_\alpha). \quad (18)
$$

Another use of Lemma 4 yields finally

$$
\| \eta v \|_{\alpha^*} \le C q^{\alpha/\varepsilon} (\| \eta v \|_\alpha + \| \eta_x v \|_\alpha). \quad (19)
$$

The preceding inequalities (18) and (19) are the basic estimates of the paper; they will appear in one form or another in almost all of the following results.

To proceed with the proof of Theorem 1, let $h$ and $h'$ be real numbers satisfying $h' < h \le 2$. Let the function $\eta$ be chosen so that $\eta = 1$ in $S(h')$, $0 \le \eta \le 1$ in $S(h)$, and identically zero outside $S(h)$. We can do this, moreover, in such a way that $\max |\eta_x| = 2(h - h')^{-1}$. Setting this function into (18) and (19) yields immediately

$$
\| v_x \|_{\alpha, h'} \le C q^{\alpha/\varepsilon} (h - h')^{-1} \| v \|_{\alpha, h} \quad (20)
$$

and

$$
\| v \|_{\alpha^*, h'} \le C q^{\alpha/\varepsilon} (h - h')^{-1} \| v \|_{\alpha, h}. \quad (21)
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

259

We may let $l \to \infty$ in inequality (21). Since $v \to \bar{u}^q$, one obtains by virtue of Lebesgue's monotone convergence theorem,

$$
\| \bar{u}^q \|_{\alpha^*, h'} \le C q^{\alpha/\varepsilon} (h - h')^{-1} \| \bar{u}^q \|_{\alpha, h}. \quad (22)
$$

Note that this is valid irrespective of the finiteness of either norm. Finally, (22) may be simplified by setting

$$
p = \alpha q = \alpha + \beta - 1, \quad \kappa = \alpha^*/\alpha = n/(n-\alpha),
$$

whence it becomes

$$
\| \bar{u} \|_{\kappa p, h'} \le [C(p/\alpha)^{\alpha/\varepsilon} (h - h')^{-1}]^{\alpha/p} \| \bar{u} \|_{p, h}. \quad (23)
$$

The required conclusion follows by iteration of this inequality. We set, for $v=0, 1, 2, \dots$,

$$
p_v = \kappa^v \alpha,
$$

and $h_v = 1 + 2^{-v}$, $h'_v = h_{v+1}$, whence (23) becomes

$$
\| \bar{u} \|_{p_{v+1}, h_{v+1}} \le C^{1/\kappa^v} K^{\nu/\kappa^v} \| \bar{u} \|_{p_v, h_v},
$$

where $K = 2\kappa^{\alpha/\varepsilon}$. Iteration yields

$$
\| \bar{u} \|_{p_{v+1}, h_{v+1}} \le C^{\sum 1/\kappa^v} K^{\sum \nu/\kappa^v} \| \bar{u} \|_{\alpha, 2} \le C \| \bar{u} \|_{\alpha, 2},
$$

since both series are convergent. Letting $v \to \infty$, and observing that $\| \bar{u} \|_{\infty, 1} \le \lim \| \bar{u} \|_{p_v, h_v}$, there results

$$
\| \bar{u} \|_{\infty, 1} \le C \| \bar{u} \|_{\alpha, 2}.
$$

Recalling that $\bar{u} = |u| + k$ then yields the conclusion

$$
\| u \|_{\infty, 1} \le C \{ \| u \|_{\alpha, 2} + k \}.
$$

This proves the first part of the theorem for the case $R=1$. The second part follows immediately by setting $q=1$, $h'=1$, $h=2$ in (20).

To complete the proof it remains only to show that the general case $R \ne 1$ can be obtained from the special case $R=1$. This involves only a simple change of linear dimension, however, which the reader may carry out for himself. Theorem 1 is therefore completely proved.

**THEOREM 2.** Let $u$ be a weak solution of equation (5) defined in some open ball $S(2R) \subset \Omega$. Suppose that $\alpha = n$ and that conditions (6) and (8) hold. Then

---

260

JAMES SERRIN

$$
\|u\|_{\infty, R} \le CR^{-1} (\|u\|_{n, 2R} + kR)
$$

and

$$
\|u_x\|_{n, R} \le CR^{-1} (\|u\|_{n, 2R} + kR),
$$

where $C$ and $k$ are constants depending only on the structure of (5). In particular

$$
C = C(n, \varepsilon; a, R^\varepsilon \|b\|, R^\varepsilon \|c\|, R^\varepsilon \|d\|)
$$

and

$$
k = (R^\varepsilon \|e\| + R^\varepsilon \|f\|)^{1/(n-1)} + (R^\varepsilon \|g\|)^{1/n}.
$$

*Proof.* Although this follows the same pattern as the proof of Theorem 1, certain alterations are necessary because the Sobolev inequalities must be applied in a slightly different way. Up to and including inequality (16) there are, of course, no changes. The various integrals in (16) are then estimated as follows, with $\tilde{\alpha} = n(1 + \varepsilon/2n)^{-1}$ and $\varepsilon' = \varepsilon(n+1)/2n$,

$$
\int b |\eta_x v| \cdot (\eta v)^{n-1} dx \le \|b\|_{n/(n-1-\varepsilon)} \|\eta_x v\|_{n/(1+\varepsilon')} \|\eta v\|_{\tilde{\alpha}^*}^{n-1}
$$

$$
\le C \|\eta_x v\|_{n/(1+\varepsilon')} \| (\eta v)_x \|_{\tilde{\alpha}}^{n-1}
$$

$$
\le C \|\eta_x v\|_n \| (\eta v)_x \|_n^{n-1}
$$

$$
\le C \{ \|\eta_x v\|_n^n + \|\eta_x v\|_n \|\eta v_x\|_n^{n-1} \},
$$

$$
\int c \eta v |\eta v_x|^{n-1} dx = \int c (\eta v)^{\varepsilon/2} (\eta v)^{1-\varepsilon/2} |\eta v_x|^{n-1} dx
$$

$$
\le \|c\|_{n/(1-\varepsilon)} \|\eta v\|_{\tilde{\alpha}}^{\varepsilon/2} \|\eta v\|_{\tilde{\alpha}^*}^{1-\varepsilon/2} \|\eta v_x\|_{\tilde{\alpha}}^{n-1}
$$

$$
\le C \|\eta v\|_n^{\varepsilon/2} \{ \|\eta_x v\|_n^{1-\varepsilon/2} \|\eta v_x\|_n^{n-1} + \|\eta v_x\|_n^{n-\varepsilon/2} \},
$$

and

$$
\int d(\eta v)^n dx = \int d(\eta v)^{\varepsilon/2} (\eta v)^{n-\varepsilon/2} dx
$$

$$
\le \|d\|_{n/(n-\varepsilon)} \|\eta v\|_{\tilde{\alpha}}^{\varepsilon/2} \|\eta v\|_{\tilde{\alpha}^*}^{n-\varepsilon/2}
$$

$$
\le C \|\eta v\|_n^{\varepsilon/2} \{ \|\eta_x v\|_n^{n-\varepsilon/2} + \|\eta v_x\|_n^{n-\varepsilon/2} \}.
$$

This leads exactly as in Theorem 1 to the inequality

$$
\|\eta v_x\|_n \le Cq^{2n/\varepsilon} (\|\eta v\|_n + \|\eta_x v\|_n).
$$

Application of the Sobolev inequality with exponent $\tilde{\alpha}$ gives next, as in Theorem 1,

$$
\|v\|_{\tilde{\alpha}^*, h'} \le Cq^{2n/\varepsilon} (h - h')^{-1} \|v\|_{n, h}.
$$

The rest of the proof is exactly the same as Theorem 1, except that now $\varkappa = \tilde{\alpha}^*/n = 2n/\varepsilon$.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

261

*Remark.* Both Theorems 1 and 2 remain true for the equation

$$
\mathrm{div} \, \mathcal{A}(x, u, u_x) = \mathcal{B}(x, u, u_x) + \mathcal{C}(x, u),
$$

where the functions $\mathcal{A}$ and $\mathcal{B}$ are the same as before, while $\mathcal{C}$ is subject only to the simple restriction $u\mathcal{C}(x, u) \ge 0$. The only change which this requires in the proof is to note that the integral of the left side of (15) is now equal to $-\int \phi \mathcal{C} dx$, and is therefore non-positive. Then (16) holds as before, and the rest of the proof is identical.

## 2. Uniform estimates. A maximum principle

The estimate of Theorem 1 can be made uniform over the whole domain of definition of the solution, provided that $u$ is continuous in the neighborhood of the boundary. More precisely we have the following result, whose statement will be restricted for simplicity to the case $\alpha < n$.

**THEOREM 3.** Let $u$ be a weak solution of (5) in a domain $D \subset \Omega$. Suppose $u \le M$ on the boundary of $D$, in the sense that for every $\varepsilon' > 0$ there exists a neighborhood of the boundary in which $u \le M + \varepsilon'$. Assume also that $\alpha < n$ and that conditions (6) and (7) hold. (1) Then

$$
\max u \le C(|D|^{-1/\alpha} \|\tilde{u}\|_{\alpha, D} + k) + M, \quad (\tilde{u} = \mathrm{Max}(0, u - M)), \quad (24)
$$

where $C$ and $k$ depend only on the structure of (5). In particular

$$
C = C(\alpha, n, \varepsilon; |D|^{\varepsilon/n} \|c\|, |D|^{\varepsilon/n} \|d\|)
$$

and

$$
k = (|D|^{\varepsilon/n} \|f\|)^{1/(\alpha-1)} + (|D|^{\varepsilon/n} \|g\|)^{1/\alpha},
$$

where the norms of the coefficients $c$ through $g$ are taken in the respective Lebesgue spaces (7).

*Remark.* The symbol $\max$ in (24) of course stands for *essential supremum*. This agreement will be followed also in later theorems.

We should also mention that a result similar to Theorem 3 was obtained by Stampacchia [23, 24] and Mazya [11] in the case of linear divergence structure equations.

(1) The inequality $|\mathcal{A}| \le a|p|^{\alpha-1} + b|u|^{\alpha-1} + e$ is in fact unnecessary, except that we must of course require $\mathcal{A}(x, u, u_x) \in L_{\alpha/(\alpha-1)}$.

---

262

JAMES SERRIN

Proof. We assume first that $|D|=1$, and define for $x \in D$,

$$
\bar{u} = \operatorname{Max}(M + \varepsilon', u) + k - M - \varepsilon'.
$$

Then obviously we have

$$
|\mathcal{B}| \le c |p|^{\alpha-1} + \bar{d} |\bar{u}|^{\alpha-1}, \quad p \cdot \mathcal{A} \ge |p|^{\alpha} - \bar{d} |\bar{u}|^{\alpha}, \quad (25)
$$

with $\|\bar{d}\|$ bounded as in the proof of Theorem 1. The proof now rests on an appropriate choice of the test function $\phi$. We consider two real functions $F(\bar{u})$ and $G(u)$, the function $F(\bar{u})$ being the same as in Theorem 1, while

$$
G(u) = F(\bar{u}) F'(\bar{u})^{\alpha-1} - q^{\alpha-1} k^{\beta}, \quad -\infty < u < \infty.
$$

Evidently $G$ is a piecewise smooth function of $u$, with corners at $u = M + \varepsilon'$ and $M + \varepsilon' + (l-k)$. Moreover, $G \equiv 0$ for $u \le M + \varepsilon'$ and $G$ is linear for $u > M + \varepsilon' + (l-k)$. Thus it is clear that the function

$$
\phi(x) = G(u), \quad (u = u(x)),
$$

is admissible in (9).

For $u > M + \varepsilon'$ and different from $M + \varepsilon' + (l-k)$ we have $\phi_x = G'(u) u_x$, with

$$
G' = \begin{cases} q^{-1} \beta (F')^{\alpha} & \text{if } u < M + \varepsilon' + (l-k), \\ (F')^{\alpha} & \text{if } u > M + \varepsilon' + (l-k). \end{cases}
$$

Hence, setting $v = v(x) = F(\bar{u})$, we obtain as in the proof of Theorem 1

$$
\phi_x \cdot \mathcal{A} + \phi \mathcal{B} \ge |v_x|^{\alpha} - cv |v_x|^{\alpha-1} - (1 + \beta) q^{\alpha-1} dv^{\alpha}, \quad (26)
$$

valid in the set indicated above. Outside this range we have $\phi_x = 0$ and $\bar{u}_x = 0$ almost everywhere, so that (26) in fact holds almost everywhere in $D$. Therefore, integrating over $D$ and using (9), we have

$$
\|v_x\|_{\alpha}^{\alpha} \le \int cv |v_x|^{\alpha-1} dx + (1 + \beta) q^{\alpha-1} \int dv^{\alpha} dx. \quad (27)
$$

These terms on the right side can be estimated by using Hölder's inequality together with Lemma 4. (1) Thus

(1) The function $v$ has not compact support, of course, but $v - k^q$ does. Thus from Lemma 4

$$
\|v - k^q\|_{\alpha^*} \le \text{Const.} \quad \|(v - k^q)_x\|_{\alpha},
$$

and hence $\|v\|_{\alpha^*} \le \text{Const.} \quad \|v_x\|_{\alpha} + k^q |D|^{1/\alpha^*} \le \text{Const.} \quad \|v_x\|_{\alpha} + |D|^{-1/n} \|v\|_{\alpha}$.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

263

$$
\begin{align*}
\int cv |v_x|^{\alpha-1} dx &= \int cv^\varepsilon v^{1-\varepsilon} |v_x|^{\alpha-1} dx \\
&\le \|c\|_{n/(1-\varepsilon)} \|v\|_{\alpha}^{\varepsilon} \|v\|_{\alpha^*}^{1-\varepsilon} \|v_x\|_{\alpha}^{\alpha-1} \\
&\le C \{ \|v\|_{\alpha}^{\varepsilon} \|v_x\|_{\alpha}^{\alpha-\varepsilon} + \|v\|_{\alpha} \cdot \|v_x\|_{\alpha}^{\alpha-1} \}, \\
\int \bar{d}v^{\alpha} dx &= \int \bar{d}v^{\varepsilon} v^{\alpha-\varepsilon} dx \\
&\le \|\bar{d}\|_{n/(\alpha-\varepsilon)} \|v\|_{\alpha}^{\varepsilon} \|v\|_{\alpha^*}^{\alpha-\varepsilon} \\
&\le C \{ \|v\|_{\alpha}^{\varepsilon} \|v_x\|_{\alpha}^{\alpha-\varepsilon} + \|v\|_{\alpha}^{\alpha} \}.
\end{align*}
$$

Inserting these estimates into (27), and setting $z = \|v_x\|_{\alpha} / \|v\|_{\alpha}$, yields

$$
z^{\alpha} \le C[z^{\alpha-\varepsilon} + z^{\alpha-1} + q^{\alpha}(z^{\alpha-\varepsilon} + 1)],
$$

whence by Lemma 2,

$$
z \le C q^{\alpha/\varepsilon},
$$

that is

$$
\|v_x\|_{\alpha} \le C q^{\alpha/\varepsilon} \|v\|_{\alpha}. \quad (28)
$$

Applying Lemma 4 once more (see the preceding footnote) gives finally

$$
\|v\|_{\alpha^*} \le C q^{\alpha/\varepsilon} \|v\|_{\alpha}. \quad (29)
$$

We may now carry out the iteration process of Theorem 1, with the important exception that there is no necessity to reduce the radius at each step. The final result is clearly

$$
\|\tilde{u}\|_{\infty} \le C \|\tilde{u}\|_{\alpha}. \quad (30)
$$

Recalling the definition of $\tilde{u}$ this is easily seen to imply

$$
\max u \le M + \varepsilon' + C(\|\tilde{u}\|_{\alpha} + k).
$$

To obtain the required conclusion we let $\varepsilon' \to 0$, and then normalize back to the given value of $|D|$.

**THEOREM 4.** Let $u$ satisfy the hypotheses of Theorem 3. Then there exists a constant $D_0$, depending only on the structure of equation (5), such that if $|D| \le D_0$ then $\max u \le M + Ck$.

*Proof.* It is convenient to make use of the calculations already carried out during the proof of Theorem 3. Retaining the assumption that $|D|=1$, we obtain respectively from Hölder's inequality, Lemma 4 (footnote), and inequality (28) written for $q=1$,

---

264

JAMES SERRIN

$$
\|\bar{u}\|_{\alpha} \le \|\bar{u}\|_{\alpha^*} \le \text{Const. } \|\bar{u}_x\|_{\alpha} + k \le C \|\bar{u}\|_{\alpha} + k. \quad (31)
$$

Now suppose that in the original definition of $\bar{u}$ the constant $k$ is replaced by $\theta^{-1}k$ where $\theta$ is a (small) positive number to be determined later. Then in place of (31) we obtain

$$
\|\bar{u}\|_{\alpha} \le C \|\bar{u}\|_{\alpha} + \theta^{-1} k. \quad (31')
$$

It will be important to assess the dependence of $C$ on the parameters $\|c\|$, $\|d\|$, and $\theta$. Assuming that $\|c\|$, $\|d\|$, and $\theta$ are all $\le 1$, say, one easily finds that

$$
C = \text{Const. } (\|c\| + \|d\|^{1/\alpha} + \theta^{(\alpha-1)/\alpha}),
$$

where the Const. depends only on $\alpha$, $n$, and $\varepsilon$. Clearly if $\theta (\le 1)$ is chosen suitably small, and if $\|c\| + \|d\| \le \theta$, then we may take $C \le \frac{1}{2}$. Consequently we have from (31')

$$
\|\bar{u}\|_{\alpha} \le 2 \theta^{-1} k.
$$

Substituting this into (30) yields finally $\|\bar{u}\|_{\infty} \le Ck$, that is to say, $\max u \le M + Ck$. The proof is completed by observing that the values of $\|c\|$, $\|d\|$ which actually arise through normalization to unit volume are $|D|^{\varepsilon/n} \|c\|$ and $|D|^{\varepsilon/n} \|d\|$, whence we may take $D_0 = \theta^{n/\varepsilon} (\|c\| + \|d\|)^{-n/\varepsilon}$.

*Remarks.* If $c=d=0$ in (6) then $D_0 = \infty$ and the maximum principle holds for arbitrary bounded regions $D$.

Finally, we observe that these results also hold if the hypothesis $u \le M$ on the boundary is replaced by the assumption that $u$ is the strong limit in $W_{\alpha}^{1}(D)$ of continuous functions which are $\le M$ on the boundary of $D$. We leave the details to the reader.

### 3. The Harnack inequality

The following theorem of Harnack type will be used to estimate the Hölder continuity of solutions of (5), and will also be of importance in our later discussion of the behavior of a solution near an isolated singularity. The main idea of the proof is the same as in Moser's celebrated paper, though the details are considerably more delicate and involved.

**THEOREM 5.** Let $u$ be a non-negative weak solution of equation (5) in some open ball $S(3R) \subset \Omega$. Assume that $\alpha < n$ and that conditions (6) and (7) hold. Then

$$
\max u \le C (\min u + k) \quad \text{in } S(R),
$$

where $C$ and $k$ are constants depending only on the structure of (5), as in Theorem 1.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

265

*Proof.* It is enough to prove the result for the case $R=1$, with the solution correspondingly defined in an open ball $S(3)$. By Theorem 1 the solution is bounded on any compact subset of $S(3)$. Thus if $\eta$ is a non-negative smooth function with compact support in $S(3)$, then

$$
\phi(x) = \eta^{\alpha} \bar{u}^{\beta}, \quad \bar{u} = u + k + \varepsilon'
$$

is admissible in (9) for any real value of $\beta$ and any $\varepsilon' > 0$. It is our purpose to insert this function into (9), and in this way to derive an estimate similar to (18). The resulting calculations are slightly different in the ranges

$$
\beta < 1 - \alpha, \quad 1 - \alpha < \beta < 0, \quad \beta > 0,
$$

while the values $\beta = 1 - \alpha$ and $\beta = 0$ are singular. We take up these various cases in order.

I. $\beta > 0$. Here the calculation is essentially the same as that of Theorem 1, with $v = \bar{u}^q$ and $q$ and $\beta$ related by $\alpha q = \alpha + \beta - 1$. In carrying out the details it is helpful to note that $\bar{u}^q$ and $\bar{u}^\beta$ here correspond to $F(\bar{u})$ and Const. $G(u)$ in Theorem 1. The main difference is that there is no longer a cutoff value $l$, so that we must always use the formulas of Theorem 1 corresponding to the range $|u| < l - k$. This means, in particular, that the factor $q^{-1}\beta$ should be inserted in front of the first term on the right sides of (14) and (15), and in front of the term on the left side of (16) and (17). Thus we have finally

$$
\beta z^{\alpha} \le C [q z^{\alpha-1} + q^{\alpha}(1 + z^{\alpha-1}) + q \zeta^{\varepsilon}(z^{\alpha-1} + z^{\alpha-\varepsilon}) + (1 + \beta) q^{\alpha} \zeta^{\varepsilon}(1 + z^{\alpha-\varepsilon})], \quad (32)
$$

the notation being the same as in Theorem 1. Applying Lemma 2 then leads to

$$
z \le C q^{\alpha/\varepsilon} (1 + \beta^{-1})^{1/\varepsilon} (1 + \zeta),
$$

where we have used the fact that $q > (\alpha - 1)/\alpha$. Thus

$$
\| \eta v_x \|_{\alpha} \le C q^{\alpha/\varepsilon} (1 + \beta^{-1})^{1/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}). \quad (33)
$$

Choosing $\eta$ as in Theorem 1 there results, in conclusion,

$$
\| v \|_{\alpha^*, h'} \le C q^{\alpha/\varepsilon} (h - h')^{-1} (1 + \beta^{-1})^{1/\varepsilon} \| v \|_{\alpha, h}, \quad (v = \bar{u}^q). \quad (34)
$$

II. $1 - \alpha < \beta < 0$. This goes as Case I, except that now $q^{-1}\beta$ is negative and inequalities (14) and (15) must run the opposite way. Otherwise there are no essential changes, and we obtain finally

---

266

JAMES SERRIN

$$
\|v\|_{\alpha^*, h'} \le C(h - h')^{-1} (1 - \beta^{-1})^{1/\epsilon} \|v\|_{\alpha, h}, \quad (v = \bar{u}^q), \quad (35)
$$

(the term $q^{\alpha/\epsilon}$ can be omitted since $0 < q < 1$).

III. $\beta < 1 - \alpha$. This goes exactly as Case I, except that $q$ is negative and absolute values are necessary. The result is

$$
\|v\|_{\alpha^*, h'} \le C(h - h')^{-1} (1 + |q|)^{\alpha/\epsilon} \|v\|_{\alpha, h}, \quad (v = \bar{u}^q)
$$

(here one uses the fact that $|\beta| > \alpha - 1$). Since the case $\beta = 0$ is trivial there remains only case

IV. $\beta = 1 - \alpha$. Substituting the functions

$$
\phi = \eta^{\alpha} \bar{u}^{1-\alpha}, \quad \phi_x = \alpha(\eta/\bar{u})^{\alpha-1} \eta_x + (1-\alpha)(\eta/\bar{u})^{\alpha} u_x
$$

directly into relation (9), we obtain with the help of (13)

$$
\begin{aligned} \phi_x \cdot \mathcal{A} + \phi \mathcal{B} &\le (1-\alpha)(\eta/\bar{u})^{\alpha} \{|u_x|^{\alpha} - \bar{d} |\bar{u}|^{\alpha}\} \\ &\quad + \alpha |\eta_x| \cdot (\eta/\bar{u})^{\alpha-1} \{a |u_x|^{\alpha-1} + \bar{b} |\bar{u}|^{\alpha-1}\} + \eta^{\alpha} \bar{u}^{1-\alpha} \{c |u_x|^{\alpha-1} + \bar{d} |\bar{u}|^{\alpha-1}\} \\ &= (1-\alpha) |\eta v_x|^{\alpha} + \alpha a |\eta_x| \cdot |\eta v_x|^{\alpha-1} + \alpha \bar{b} \eta^{\alpha-1} |\eta_x| + c \eta |\eta v_x|^{\alpha-1} + \alpha \bar{d} \eta^{\alpha}, \end{aligned}
$$

where $v = v(x) = \log \bar{u}$. Hence integrating over $S(3)$ there results

$$
(\alpha - 1) \|\eta v_x\|_{\alpha}^{\alpha} \le \alpha a \int |\eta_x| \cdot |\eta v_x|^{\alpha-1} dx + \alpha \int \bar{b} \eta^{\alpha-1} |\eta_x| dx + \int c \eta |\eta v_x|^{\alpha-1} dx + \alpha \int \bar{d} \eta^{\alpha} dx. \quad (36)
$$

Before estimating the integrals on the right-hand side, it is convenient to specialize the function $\eta$. Let $S$ be an arbitrary open ball of radius $h$ contained in $S(2)$. We choose $\eta$ so that $\eta = 1$ in $S$ and $0 \le \eta \le 1$ in $S(3) - S$. This may be done, moreover, in such a way that the support of $\eta$ is contained in a concentric sphere about $S$ of radius $(3/2)h$, and so that $\text{Max} |\eta_x| = 3/h$. Then by Hölder's inequality we have the estimates

$$
\begin{aligned} \int |\eta_x| \cdot |\eta v_x|^{\alpha-1} dx &\le C h^{(n-\alpha)/\alpha} \|\eta v_x\|_{\alpha}^{\alpha-1}, \\ \int \bar{b} \eta^{\alpha-1} |\eta_x| dx &\le C h^{n-\alpha}, \\ \int c \eta |\eta v_x|^{\alpha-1} dx &\le C h^{(n-\alpha)/\alpha} \|\eta v_x\|_{\alpha}^{\alpha-1}, \\ \int \bar{d} \eta^{\alpha} dx &\le C h^{n-\alpha}, \end{aligned}
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

267

where conditions (7) have been used at each stage. Inserting the preceding inequalities into (36) there follows

$$
\| \eta v_x \|_{\alpha}^{\alpha} \le C [h^{(n-\alpha)/\alpha} \| \eta v_x \|_{\alpha}^{\alpha-1} + h^{n-\alpha}].
$$

Thus by Lemma 2 we have $\|v_x\|_{\alpha,S} \le Ch^{(n-\alpha)/\alpha}$, since $\eta \equiv 1$ in $S$. Finally by Lemma 6 and a simple use of Hölder's inequality we obtain

$$
\|v - v_S\|_1 \le Ch \|v_x\|_1 \le Ch^{1+n(\alpha-1)/\alpha} \|v_x\|_{\alpha} \le Ch^n,
$$

$$
\text{that is} \qquad \int_S |v - v_S| dx \le C |S|, \quad (v = \log \bar{u}). \qquad (37)
$$

This estimate, valid for any ball $S$ contained in $S(2)$, completes the discussion of case IV.

This being accomplished, the required conclusion will now be obtained by an iteration process somewhat similar to that of Theorem 1. For any real number $p \ne 0$ we define

$$
\Phi(p, h) = \left( \int_{S(h)} |\bar{u}|^p dx \right)^{1/p},
$$

(thus for $p \ge 1$ we have $\Phi(p, h) = \|\bar{u}\|_{p, h}$). Now from (37) and Lemma 7 it follows that

$$
\int_{S(2)} e^{p_0 v} dx \cdot \int_{S(2)} e^{-p_0 v} dx \le 2^{2n} \mu^2,
$$

where $p_0 = \lambda/C$; the constant $C$ is here the same as in (37), while $\lambda$ and $\mu$ depend only on the dimension. Since $v = \log \bar{u}$ this inequality may be rewritten simply

$$
\Phi(p_0, 2) \le C \Phi(-p_0, 2). \qquad (38)
$$

Next, putting $p = \alpha q = \alpha + \beta - 1$ in (34) and (35), taking the $q$th root of each side, and combining the results in a single inequality, we obtain

$$
\Phi(\kappa p, h') \le [C(h - h')^{-1} (1 + |\beta|^{-1})^{1/\varepsilon} (1 + p)^{\alpha/\varepsilon}]^{\alpha/p} \Phi(p, h), \qquad (39)
$$

where $\kappa = \alpha^*/\alpha$ and $p$ is any positive number other than $\alpha - 1$. We wish to iterate this inequality, beginning with $\Phi(p_0, 2)$ and setting generally

$$
p_v = \kappa^v p_0, \quad v = 0, 1, 2, \dots,
$$

and $h_v = 1 + 2^{-v}$, $h'_v = h_{v+1}$. In order that (39) be applicable at each stage, the successive iterates $p_v$ must avoid the point $p = \alpha - 1$. To accomplish this in a definite way we

---

268

JAMES SERRIN

shall in fact choose a new initial value $p'_0 \le p_0$ so that the point $p = \alpha - 1$ lies midway between some two consecutive iterates of $p'_0$. The value $p'_0$ being thus fixed, we observe that at all stages of the iteration process one has

$$
|\beta| = |p - (\alpha - 1)| \ge \frac{\alpha(\alpha - 1)}{2n - \alpha}.
$$

The term $(1 + |\beta|^{-1})^{1/\epsilon}$ in (39) can thus be absorbed into the general constant $C$. Application of the iteration process just described then leads, as in the proof of Theorem 1, to the inequality

$$
\max_{S(1)} \bar{u} \le C \Phi(p'_0, 2). \quad (40)
$$

It remains to examine the inequality of Case III. Again setting $p = \alpha q$ and taking $q$th roots, this inequality becomes

$$
\Phi(\kappa p, h') \ge [C(h - h') (1 + |p|)^{\alpha/\epsilon}]^{\alpha/p} \Phi(p, h),
$$

where the sign is reversed since $p$ and $q$ are now negative. Iterating as before, with $p_v = -\kappa^v p_0$ and $h_v = 1 + 2^{-v}$, $h'_v = h_{v+1}$, there results without difficulty

$$
\Phi(p_{v+1}, h_{v+1}) \ge C^{-1} \Phi(-p_0, 2).
$$

Letting $v \to \infty$ then establishes the inequality

$$
\min_{S(1)} \bar{u} \ge C^{-1} \Phi(-p_0, 2). \quad (41)
$$

The proof is now easily completed. From (40), (38), and (41), and a simple application of Hölder's inequality, (1) we have

$$
\max_{S(1)} \bar{u} \le C \Phi(p'_0, 2) \le C \Phi(p_0, 2) \le C \Phi(-p_0, 2) \le C \min_{S(1)} \bar{u}.
$$

Since $\bar{u} = u + k + \varepsilon'$ this implies in turn $\max u \le C(\min u + k + \varepsilon')$. Letting $\varepsilon' \to 0$ concludes the demonstration.

THEOREM 6. Let $u$ be a non-negative weak solution of (5) in some open ball $S(3R) \subset \Omega$. Assume that $\alpha = n$ and that conditions (6) and (8) hold. Then

$$
\max u \le C(\min u + k) \quad \text{in} \quad S(R),
$$

where $C$ and $k$ are constants depending only on the structure of (5), as in Theorem 2.

(1) To obtain $\Phi(p_0, 2) \le C \Phi(p_0, 2)$. In particular we find

$$
\Phi(p'_0, 2) \le |S(2)|^{1/p'_0 - 1/p_0} \Phi(p_0, 2),
$$

where the exponent can be assumed less than $(\kappa - 1)/p_0$ since surely one can choose $p'_0 > \kappa^{-1} p_0$.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

269

The proof may be omitted, since it is simply a modification of the preceding argument, in exactly the same way as Theorem 2 was a modification of Theorem 1. A Harnack inequality for the case $\alpha > n$ will be proved in Section 5.

## 4. Applications. Hölder continuity of solutions

The Harnack inequalities of the foregoing section can be extended without difficulty so as to apply to arbitrary regions $D$. In particular, the following result holds.

**THEOREM 7.** If $u$ is a non-negative weak solution of (5) in a domain $D$, and if $D'$ is any compact subset of $D$, then

$$
\max u \le C'(\min u + k') \quad \text{in } D',
$$

where $C'$ depends only on the structure of equation (5) and on the domains $D$ and $D'$, and $k' = (\|e\| + \|f\|)^{1/(\alpha-1)} + \|g\|^{1/\alpha}$.

The proof is standard, depending only on covering $D'$ with spheres and on a simple chaining argument.

We turn now to a fundamental estimate of the Hölder continuity of solutions of (5). It is enough to consider the case $\alpha \le n$, for when $\alpha > n$ the result is immediate from Morrey's lemma. Also, if $\alpha < n$, it will be supposed that $e$ is in a more restrictive Lebesgue class than originally supposed, namely

$$
e \in L_{n/(\alpha-1-\varepsilon)},
$$

($\varepsilon$ should now be less than both 1 and $\alpha-1$). In this case the parameter $k$ in Theorems 5 and 6 has the form

$$
k = (R^{\varepsilon} \|e\| + R^{\varepsilon} \|f\|)^{1/(\alpha-1)} + (R^{\varepsilon} \|g\|)^{1/\alpha}.
$$

We may now prove

**THEOREM 8.** Let $u$ be a weak solution of (5) in a domain $D \subset \Omega$, Then $u$ is (essentially) Hölder continuous in $D$. Moreover, if $|u| \le L$ in $D$ and if $D'$ is any compact subset of $D$, then

$$
|u(x) - u(y)| \le H(k' + L) |x - y|^{\lambda}, \quad x, y \in D',
$$

where $\lambda = \lambda(\alpha, n, \varepsilon; a, \|b\|, \|c\|, \|d\|)$, and $H$ depends only on the structure of (5) and on the geometry of $D$ and $D'$.

---

270

JAMES SERRIN

*Proof.* It will first be shown that $u$ is Hölder continuous at any fixed point $P$ in $D$. The general result will then follow easily.

Thus let $P$ be a point of $D$, and let $R$ be chosen so that the ball $S(R)$ has compact closure in $D$. By a suitable change of variables we may suppose $R=1$. The expressions

$$
M(r) = \max_{S(r)} u, \quad \mu(r) = \min_{S(r)} u
$$

are then well defined for $0 < r \le 1$, and it follows that both functions

$$
\bar{u} = M - u \quad \text{and} \quad \bar{\mu} = u - \mu
$$

are non-negative in $S(r)$. Obviously $\bar{u}$ satisfies the differential equation

$$
\operatorname{div} \bar{A}(x, \bar{u}, \bar{u}_x) = \bar{B}(x, \bar{u}, \bar{u}_x)
$$

with $\bar{A}(x, \bar{u}, \bar{p}) = A(x, M - \bar{u}, -\bar{p})$ and a similar formula for $\bar{B}$. These quantities clearly obey the inequalities

$$
|\bar{A}| \le a |\bar{p}|^{\alpha-1} + \bar{b} |\bar{u}|^{\alpha-1} + \bar{e}, \quad \text{etc.,}
$$

where $\bar{b} = 2^\alpha b$, $\bar{e} = e + 2^\alpha b L^{\alpha-1}$, etc. Thus we may apply Theorem 5 (or Theorem 6) to $\bar{u}$ in the open ball $S(r)$, with the result

$$
M - \mu' = \max_{S(r/3)} \bar{u} \le C (\min_{S(r/3)} \bar{u} + \bar{k}) = C(M - M' + \bar{k}), \quad 0 < r \le 1, \quad (42)
$$

where $M' = M'(r) = M(r/3)$, $\mu' = \mu'(r) = \mu(r/3)$. In this inequality the constant $C$ depends on the variables listed in the theorem, while

$$
\bar{k} = (r^\varepsilon \|\bar{e}\| + r^\varepsilon \|\bar{f}\|)^{1/(\alpha-1)} + (r^\varepsilon \|\bar{g}\|)^{1/\alpha}.
$$

In the same way, we have

$$
M' - \mu = \max_{S(r/3)} \bar{\mu} \le C (\min_{S(r/3)} \bar{\mu} + \bar{k}) = C(\mu' - \mu + \bar{k}). \quad (43)
$$

Adding (42) and (43) and transposing terms then gives

$$
M' - \mu' \le \frac{C-1}{C+1} (M - \mu) + \frac{2C\bar{k}}{C+1}. \quad (44)
$$

Now $\bar{k} \le k_0 r^\varepsilon/\alpha$ where $k_0 = (\|\bar{e}\| + \|\bar{f}\|)^{1/(\alpha-1)} + (\|\bar{g}\|)^{1/\alpha}$. Thus setting

$$
\vartheta = \frac{C-1}{C+1}, \quad \tau = \frac{2Ck_0}{C+1},
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

271

and denoting the oscillation $M - \mu$ of $u$ in $S(r)$ by $\omega(r)$, we may write (44) in the form

$$
\omega(r/3) \le \vartheta\{\omega(r) + \tau r^{\varepsilon/\alpha}\}, \quad 0 < r \le 1.
$$

Since $\omega(r)$ is an increasing function, it is clear that for any number $s \ge 3$ one has also

$$
\omega(r/s) \le \vartheta\{\omega(r) + \tau r^{\varepsilon/\alpha}\}, \quad 0 < r \le 1.
$$

Iteration of this relation from $r=1$ to successively smaller radii yields

$$
\omega(s^{-\nu}) \le \vartheta^{\nu}\{\omega(1) + \tau[1 + (\vartheta s^{\varepsilon/\alpha})^{-1} + \dots + (\vartheta s^{\varepsilon/\alpha})^{-\nu+1}]\}, \quad (45)
$$

valid for $\nu = 1, 2, 3, \dots$. Now choose $s$ according to the relation

$$
\vartheta s^{\varepsilon/\alpha} = 2, \quad (s \ge 4).
$$

whence from (45) follows

$$
\omega(s^{-\nu}) \le \vartheta^{\nu}\{\omega(1) + 2\tau\}. \quad (46)
$$

For any fixed $\varrho$, $0 < \varrho \le s^{-1}$, let $\nu$ be chosen such that $s^{-\nu-1} < \varrho \le s^{-\nu}$. Then by virtue of (46),

$$
\omega(\varrho) \le \omega(s^{-\nu}) \le \vartheta^{\nu}\{\omega(1) + 2\tau\}. \quad (47)
$$

Now one easily checks that $\omega(1) + 2\tau \le C(L + k)$. In addition, if $\gamma$ is defined by the relation $2^{-\gamma} = \vartheta$, then we have $\vartheta = s^{-\lambda}$ where $\lambda = \varepsilon\gamma/\alpha(\gamma + 1) > 0$. Therefore (47) implies

$$
\omega(\varrho) \le C(L + k) \varrho^{\lambda}, \quad \varrho \le 2^{-(\gamma+1)\alpha/\varepsilon},
$$

$$
\text{or when } R \ne 1, \quad \omega(\varrho) \le C(L + k) (\varrho/R)^{\lambda}, \quad \varrho \le 2^{-(\gamma+1)\alpha/\varepsilon} R. \quad (48)
$$

This proves that $u$ is essentially Hölder continuous at $P$.

It is a trivial, though not entirely simple, task to show that we can redefine $u$ on a set of measure zero so that the resulting function is Hölder continuous at every point of $D$. Leaving aside this demonstration, the first part of the theorem is therefore proved. The second part follows easily from the estimate (48), using a simple chaining argument (choose $R = \text{Min}(1, \xi)$, where $\xi$ is the distance from $D'$ to the boundary of $D$).

## 5. The Harnack inequality for $\alpha > n$

In the foregoing sections we have considered the majorization and continuity of solutions when $\alpha \le n$. The situation for $\alpha > n$ is somewhat different, since by Morrey's lemma solutions are necessarily bounded and Hölder continuous on compact subsets

18-642946 *Acta mathematica*. 111. Imprimé le 9 juin 1964

---

272

JAMES SERRIN

of their domain of definition. For this reason we may confine our discussion solely to the Harnack inequality.

We retain the basic structure (6), and assume further that

$$
b, e \in L_{\alpha/(\alpha-1)}; \quad c \in L_{\alpha}; \quad d, f, g \in L_1. \qquad (49)
$$

Then the following result holds.

THEOREM 9. Let $u$ be a non-negative weak solution of (5) in some open ball $S(2R) \subset \Omega$. Assume that $\alpha > n$ and that conditions (6) and (49) hold. Then for any two points $x, y$ in $S(R)$ we have

$$
u(x) \le \{u(y) + k\} \exp \{C(|x-y|/R)^{1-n/\alpha}\}, \qquad (50)
$$

where $C = C(\alpha, n; a, R^{(\alpha-n)/\alpha} \|b\|, R^{(\alpha-n)/\alpha} \|c\|, R^{\alpha-n} \|d\|)$

and $k = (R^{(\alpha-n)/\alpha} \|e\| + R^{\alpha-n} \|f\|)^{1/(\alpha-1)} + (R^{\alpha-n} \|g\|)^{1/\alpha}$,

the norms of the coefficients being taken in the respective Lebesgue spaces (49).

Proof. Suppose first that $R=1$. Let $\eta$ be a smooth function with compact support in $S(2)$, such that $\eta=1$ in $S(1)$, and $0 \le \eta \le 1$ in $S(2) - S(1)$. Now set

$$
\phi(x) = \eta^{\alpha} \bar{u}^{1-\alpha}
$$

in (9), where $\bar{u} = u + k + \varepsilon'$. Then, as in Case IV of the proof of Theorem 5, we find

$$
(\alpha - 1) \|\eta v_x\|_{\alpha}^{\alpha} \le \alpha \int a |\eta_x| \cdot |\eta v_x|^{\alpha-1} dx + \alpha \int b \eta^{\alpha-1} |\eta_x| dx + \int c \eta |\eta v_x|^{\alpha-1} dx + \alpha \int d \eta^{\alpha} dx.
$$

Here $v = \log \bar{u}$, and $\bar{b}$ and $\bar{d}$ are defined as in Theorem 1. We may assume that $\text{Max} |\eta_x| = 2$, hence by Hölder's inequality

$$
\|\eta v_x\|_{\alpha}^{\alpha} \le C[1 + \|\eta v_x\|_{\alpha}^{\alpha-1}].
$$

Application of Lemma 2 then yields (since $\eta \equiv 1$ in $S(1)$)

$$
\|v_x\|_{\alpha} \le C, \qquad (51)
$$

the integral being taken over the unit ball $S(1)$.

Since $\|v_x\|_{\alpha}$ is finite we conclude from Morrey's lemma that $v$ is Hölder continuous in $S(1)$,

$$
|v(x) - v(y)| \le C |x - y|^{1-n/\alpha}.
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

273

But $v = \log \bar{u}$, so that this implies

$$
\bar{u}(x) \le \bar{u}(y) e^{C|x-y|^{1-n/\alpha}}, \quad (x, y \in S(1)).
$$

Recalling the definition of $\bar{u}$, the required inequality now follows immediately. The case $R \ne 1$ offers no additional difficulty, and the theorem is proved.

As an immediate consequence of Theorem 9 we have the result that

$$
\max u \le C(\min u + k);
$$

this is, of course, considerably weaker than the actual inequality (50).

## 6. Generalizations

We begin by noting that certain equations which nominally do not fall into the categories above can in fact be considered as special cases. In particular, in case $\alpha < n$ let us suppose that (6) is replaced by

$$
\begin{aligned} |\mathcal{A}| &\le a(|p|^{\alpha-1} + |u|^{(\alpha-1)/\zeta} + e), \\ |\mathcal{B}| &\le a(|p|^{\alpha-\zeta} + |u|^{(\alpha-\zeta)/\zeta} + f), \\ p \cdot \mathcal{A} &\ge |p|^{\alpha} - a(|u|^{\alpha/\zeta} + g), \end{aligned}
$$

where $\zeta = (n - \alpha + \alpha\varepsilon)/n$. If we now consider a *fixed solution* $u$, we can set

$$
b(x) = a|u|^{(\alpha-1)(1-\zeta)/\zeta}, \quad c(x) = a|u_x|^{1-\zeta}, \quad d(x) = a|u|^{\alpha(1-\zeta)/\zeta}
$$

and it is easily verified (assuming that $u_x \in L_\alpha$, $u \in L_{\alpha^*}$) that conditions (7) are in fact satisfied. Thus the conclusions of Theorems 1, 3, 4, 7, and 8 remain valid, with the exception that the coefficient $C$ now must depend on the $W_\alpha^1$ norm of the solution. A similar result holds when $\alpha \ge n$, but it is not necessary to carry this out in detail.

A slightly different situation arises if we know *a priori* that $u$ is *bounded*. Then under genuinely weaker conditions it is possible to carry through the arguments leading to the Harnack inequality and the Hölder continuity of solutions. Since a result of this sort will not be required in the later sections of the paper, we shall not pause to consider the situation in any detail. It may be remarked, however, that the arguments of references [8], [9] are in general based on such an *a priori* estimate for the magnitude of $u$, which partially explains the difference between their hypotheses and ours.

In conclusion, there has been some interest in the situation when the "inhomogeneous" terms $e, f, g$ do not lie in the respective Lebesgue spaces (7). For this case we have the following results, analogous to Theorems 1, 3, and 4.

---

274

JAMES SERRIN

THEOREM 1'. Let the hypotheses of Theorem 1 be satisfied, with the exception that $e \in L_{r*}$, $f \in L_r$, $g \in L_t$, where

$$
\frac{1}{\alpha-1} \left( \frac{1}{r} - \frac{\alpha}{n} \right) = \frac{1}{\alpha} \left( \frac{1}{t} - \frac{\alpha}{n} \right) = \frac{1}{\sigma}
$$

and $\sigma$ is some number in the range $\alpha^* \le \sigma < \infty$. Then

$$
\|u\|_{\sigma,R} \le CR^{n/\sigma-n/\alpha} (\|u\|_{\alpha, 2R} + kR^{n/\alpha}),
$$

where $C$ and $k$ depend only on the structure of equation (5).

Proof. This proceeds in the same way as Theorem 1, except that we take the initial substitution in the form $\bar{u} = |u|$. It is clear that certain terms involving $e, f, g$ must then be carried along in relations (14) through (23). In particular, to the right side of (16) one must add the expression

$$
\alpha q^{\alpha-1} \int e |\eta_x v| \cdot (\eta v)^{\beta/q-1} dx + q^{\alpha-1} \int f(\eta v)^{\beta/q} dx + \beta q^{\alpha-1} \int g(\eta v)^{\alpha(q-1)/q} dx.
$$

These integrals can be estimated only if $q \le \sigma/\alpha^*$. For example, with this restriction on $q$ one has

$$
\begin{aligned} \int e |\eta_x v| \cdot (\eta v)^{\beta/q-1} dx &\le \|e\|_{r*} \|\eta_x v\|_{\alpha} \|\eta v\|_{\alpha^*}^{\beta/q-1} \\ &\le C(\|e\|_{r*}^{\alpha q/(\alpha-1)} + \|\eta_x v\|_{\alpha}^{\alpha}) + \text{Const.} \|\eta v_x\|_{\alpha}^{\alpha}, \end{aligned}
$$

where the constant in front of $\|\eta v_x\|_{\alpha}^{\alpha}$ can be taken as small as we like. The remaining two integrals likewise have similar estimates. Thus, by following the steps of Theorem 1, one obtains in place of (23)

$$
\|u\|_{\kappa p, h'} \le C(h-h')^{-\alpha/p} \{\|u\|_{p, h} + \|e\|_{r*}^{1/(\alpha-1)} + \|f\|_{r}^{1/(\alpha-1)} + \|g\|_{t}^{1/\alpha}\},
$$

valid for $p = \alpha q \le \sigma/\kappa$. The required conclusion now follows by a finite iteration of this inequality.

THEOREM 3'. Let the hypotheses of Theorem 3 hold, with the exception that $e, f, g$ are assumed to be in the preceding Lebesgue classes. Then

$$
\|\tilde{u}\|_{\sigma,D} \le C|D|^{1/\sigma-1/\alpha} (\|\tilde{u}\|_{\alpha,D} + |D|^{1/\alpha}k),
$$

where $\tilde{u} = \text{Max}(0, u - M)$ and $C$ and $k$ are constants depending only on the structure of (5).

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

275

This is proved by the argument of Theorem 3, beginning with the substitution $\tilde{u} = \text{Max}(0, u - M - \varepsilon')$. The details can be omitted, as also in the case of

THEOREM 4'. Let $u$ satisfy the hypotheses of Theorem 3'. Then there exists a constant $D_0$, depending only on the structure of equation (5), such that if $|D| \le D_0$ then

$$
\|\tilde{u}\|_{\sigma,D} \le C|D|^{1/\sigma} k, \\ \text{where } \tilde{u} = \text{Max}(0, u - M).
$$

There are also similar results for the case $\sigma < \alpha^*$, though the proofs are quite a bit more delicate. Since this case is somewhat artificial (recall that $u$ is always locally in class $L_{\alpha^*}$), the discussion may be omitted.

## II. Removable singularities

The methods of Chapter I will here be used to prove two basic theorems concerning the removable singularities of solutions of equation (5). We shall retain the structure outlined in the opening discussion of Chapter I, with the exception that $e$ will be assumed in $L_{n/(\alpha-1-\varepsilon)}$ rather than $L_{n/(\alpha-1)}$.

We may further confine the discussion to the case $\alpha \le n$, for the alternate case $\alpha > n$ can admit no removable singularity theorems of the ordinary sort. Indeed, consider the equation

$$
\operatorname{div} (u_x |u_x|^{\alpha-2}) = 0
$$

with $\alpha > n$. It is easily checked that $u = r^{(\alpha-n)/(\alpha-1)}$ is a bounded solution in the domain $0 < r < 1$. On the other hand, the origin is definitely a non-removable singularity for this solution, since if $\phi$ is a continuously differentiable function with compact support in the unit open ball, then

$$
\int \phi_x \cdot u_x |u_x|^{\alpha-2} dx = - \left( \frac{\alpha - n}{\alpha - 1} \right)^{\alpha-1} \omega_n \phi(0),
$$

and this need not vanish. That is, when $\alpha > n$ there can exist bounded solutions with non-removable isolated singularities. The above example indicates in addition the type of behavior one can expect at an isolated singularity when $\alpha < n$, and will therefore be useful in testing the sharpness of some of our later results.

## 7. Statement of results

In the following it is convenient to restrict consideration to continuous solutions of (5), that is, weak solutions which have furthermore the property of being continuous

---

276

JAMES SERRIN

functions. This involves no real loss of generality, of course, since by Theorem 8 any weak solution can be made continuous by appropriately redefining it on a set of measure zero.

We shall require also the notion of capacity. Let $Q$ be a bounded set in $E^n$. The $s$-capacity of $Q$, $1 \le s < \infty$, is defined to be

$$
\inf \int |\psi_x|^s dx,
$$

where the infimum is taken over all continuously differentiable functions $\psi$ which are $\ge 1$ on $Q$ and have compact support in $E^n$ (if $s \ge n$, we require compact support in some fixed sphere $|x| < R_0$). When $s=2$ this definition reduces to the familiar one of potential theory. We may now state our fundamental result.

**THEOREM 10.** Let $Q$ be a compact set of $s$-capacity zero, where $\alpha \le s \le n$, and let $D$ be a domain in $\Omega$. Suppose that $u$ is a continuous solution of (5) in the set $D-Q$, and that for some $\delta > 0$ we have

$$
u \in L_{\theta(1+\delta)}, \quad \theta = s(\alpha - 1)/(s - \alpha). \qquad (52)
$$

Then $u$ can be defined on the set $Q$ so that the resulting function is a continuous solution of (5) in all of $D$. The exponent $\theta$ in (52) is best possible.

As a special case, if the $\alpha$-capacity of $Q$ is zero, then $Q$ is a removable singularity for any bounded solution of (5).

This theorem has several corollaries which further clarify its meaning, and relate the size of the exceptional set to the classical concepts of *potential theoretic capacity* and *Hausdorff dimension*. (Definitions of these concepts appear in references [1] and [26], and in other places; they may be omitted here since the corollaries will not be used in the sequel.)

**COROLLARY 1.** Let $Q$ be a compact manifold of Hausdorff dimension $m$, and let $D$ be a domain in $\Omega$. Suppose that $m < n - \alpha$. Let $u$ be a continuous solution of (5) in $D-Q$, such that for some $\delta > 0$

$$
u \in L_{\theta(1+\delta)}, \quad \theta = (n-m)(\alpha-1)/(n-m-\alpha). \qquad (53)
$$

Then $u$ can be defined on the set $Q$ so that the resulting function is a continuous solution of (5) in all of $D$.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

277

*Proof.* Let $\Lambda_p$ denote the Hausdorff $p$-measure of the manifold $Q$. Then clearly $\Lambda_{m+\varepsilon}=0$ for any $\varepsilon>0$. This implies (cf. [26]) that the $s$-capacity of $Q$ is zero, where $s=n-m-\varepsilon$. On the other hand, by (53)

$$
u \in L_{\kappa}, \quad \kappa = \frac{s(\alpha-1)}{(s-\alpha)} (1+\delta'),
$$

provided $\varepsilon$ is suitably small. It now follows from Theorem 10 that $Q$ is removable.

**COROLLARY 2.** Let $Q$ be a compact manifold of potential theoretic $\lambda$-capacity zero, and let $D$ be a domain in $\Omega$. Suppose also that $0 \le \lambda < n - \alpha$ or that $\lambda = n - \alpha$ and $\alpha \ge 2$. Let $u$ be a continuous solution of (5) in $D - Q$, such that for some $\delta > 0$

$$
u \in L_{\theta(1+\delta)}, \quad \theta = (n - \lambda) (\alpha - 1) / (n - \lambda - \alpha).
$$

Then $u$ can be defined on the set $Q$ so that the resulting function is a continuous solution of (5) in all of $D$.

*Proof.* If $0 \le \lambda < n - \alpha$, then by [26], Theorem A, the $s$-capacity of $Q$ is zero, where $s = n - \lambda - \varepsilon$. Thus $Q$ is removable, as in Corollary 1. If $\lambda = n - \alpha$ and $\alpha \ge 2$, then $\lambda \le n - 2$ and by [26], Theorem A, the $\alpha$-capacity of $Q$ is zero. Since $u \in L_\infty$ in the present case, we conclude once more from Theorem 10 that $Q$ is removable.

Another slightly different version of Theorem 10 can be given if we replace the Lebesgue class hypothesis on $u$ by a strict growth property. For this purpose we understand that a smooth manifold of co-dimension $s$ is a compact set in $E^n$ with the property that there exists a $C^1$ diffeomorphism $x \to y$ of $E^n$ onto itself such that the image of the manifold lies in the hyperplane $y_1 = \dots = y_s = 0$.

**THEOREM 11.** Let $Q$ be a smooth manifold of co-dimension $s$, where $\alpha \le s \le n$, and let $D$ be a domain in $\Omega$. Suppose that $u$ is a continuous solution of (5) in $D - Q$, and that for some $\delta > 0$ we have

$$
u = \begin{cases} O(\xi^{(\alpha-s)/(\alpha-1)+\delta}) & \text{if } s > \alpha, \\ O(|\log \xi|^{1-\delta}) & \text{if } s = \alpha, \end{cases}
$$

where $\xi$ is the distance from $Q$. Then $u$ can be defined on the manifold $Q$ so that the resulting function is a solution of (5) in the whole domain $D$. (1)

(1) If $Q$ is a single point, and $r$ denotes the distance to this point, the hypothesis of Theorem 11 becomes $u = O(r^{(\alpha-n)/(\alpha-1)+\delta})$ or $O(|\log r|^{1-\delta})$. When $\alpha=2$ this further reduces to $u = O(r^{2-n+\delta})$ or $O(|\log r|^{1-\delta})$, as might be expected. Earlier results of this type appear in [6] and [21].

---

278

JAMES SERRIN

When $s > \alpha$ this theorem is a special case of Corollary 1 (if desired, the reader may show directly that $Q$ has $s$-capacity zero and so reduce the result directly to Theorem 10). The case $s = \alpha$, on the other hand, requires its own separate proof.

The proof of Theorem 10 will be given in the next section. Following this we prove the logarithmic case of Theorem 11. Finally, in Section 10 we prove a lemma on capacity which was crucial at one stage in the demonstration of Theorem 10.

There is some interest in the existence of solutions with non-removable singularities. In the following chapter we shall take up this question in some detail for the special equation $\operatorname{div} A(x, u_x) = 0$. Here we shall only remark that if a positive solution of (5) has a non-removable isolated singularity at a point $P$, then the solution necessarily tends to infinity at $P$. Indeed by Theorem 10 or 11 there must exist a sequence of points $x_v$, $v = 1, 2, \dots$, tending to $P$, such that $u(x_v) \to \infty$. We now wish to apply the Harnack inequality (Theorem 7) in annular domains about $P$. For simplicity of notation suppose $P$ is the origin. Then by normalizing each sphere $|x| = |x_v|$ to radius 1 and applying Theorem 7 we obtain

$$
\mu_v = \min_{|x|=|x_v|} u(x) \to \infty.
$$

Finally by Theorem 4 one sees that (for sufficiently large $v$)

$$
u(x) \ge \operatorname{Min}(\mu_v, \mu_{v+1}) - Ck, \quad |x_{v+1}| \le |x| \le |x_v|.
$$

The required conclusion follows at once. It should be noted that this argument is essentially the same as one in reference [6].

## 8. Proof of Theorem 10

It is enough to show that $u$ can be made a continuous solution in the neighborhood of any point of $D$. Thus let $P$ be in $D$ and let $R$ be such that the ball $S(2R)$ is also in $D$. By a suitable change of variables it may be supposed that $R=1$. As in the proof of Theorem 1 we define

$$
\bar{u} = |u| + k, \quad x \in S(2) - Q,
$$

where $k = 1 + (\|e\| + \|f\|)^{1/(\alpha-1)} + \|g\|^{1/\alpha}$. We now introduce an appropriate test function $\phi(x)$. Let $\eta$ and $\bar{\eta}$ be non-negative smooth functions, $\eta$ having compact support in $S(2)$, and $\bar{\eta}$ vanishing in some neighborhood of $Q$. Then since $u$ is locally bounded and has strong derivatives which are locally in $L_\alpha$, it is clear that the function

$$
\phi(x) = (\eta\bar{\eta})^\alpha \operatorname{sign} u \cdot \{\bar{u}^\beta - k^\beta\}
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

279

is admissible in (9) for any $\beta > 0$. The resulting calculation (1) is essentially the same as in Theorems 1 and 5, and gives the results

$$
\| \eta \bar{\eta} v_x \|_{\alpha} \le C q^{\alpha/\varepsilon} (1 + \beta^{-1})^{1/\varepsilon} (\| \eta \bar{\eta} v \|_{\alpha} + \| (\eta \bar{\eta})_x v \|_{\alpha}), \quad (54)
$$

$$
\| \eta \bar{\eta} v \|_{\alpha*} \le C q^{\alpha/\varepsilon} (1 + \beta^{-1})^{1/\varepsilon} (\| \eta \bar{\eta} v \|_{\alpha} + \| (\eta \bar{\eta})_x v \|_{\alpha}), \quad (55)
$$

where $v = \bar{u}^q$ and $\alpha q = \alpha + \beta - 1$.

We now require a lemma, whose proof will be deferred until Section 10. In order to formulate the lemma more simply we use the notation $U(Q)$ to denote the class of smooth functions $\bar{\eta}(x)$ which satisfy $0 \le \bar{\eta} \le 1$ and vanish in some neighborhood of $Q$.

LEMMA 8. Let $Q$ be a compact set of $s$-capacity zero, $1 \le s \le n$. Then there exists a sequence of functions $\bar{\eta}^{(v)}$ contained in $U(Q)$ such that $\bar{\eta}^{(v)} \to 1$ almost everywhere, while $\| \bar{\eta}_x^{(v)} \|_s \to 0$.

Now consider the term $\| \bar{\eta}_x v \|_{\alpha}$ which appears in both (54) and (55). We have, if $s > \alpha$,

$$
\| \bar{\eta}_x v \|_{\alpha} = \int |\bar{\eta}_x|^\alpha \bar{u}^{\alpha q} dx \le \| \bar{\eta}_x \|_s^\alpha \left( \int \bar{u}^{\alpha q s/(s-\alpha)} dx \right)^{1-\alpha/s}.
$$

Choosing $\beta = \beta_0 = \delta(\alpha - 1)$ one finds that $\alpha q s / (s - \alpha) = (\alpha + \beta - 1) s / (s - \alpha) = \theta(1 + \delta)$, whence using the hypothesis (52),

$$
\| \bar{\eta}_x v \|_{\alpha} \le \text{Const.} \| \bar{\eta}_x \|_s. \quad (56)
$$

On the other hand, if $s = \alpha$ then $\theta = \infty$ and by hypothesis $u \in L_\infty$ and $\| \bar{\eta}_x v \|_{\alpha} \le \text{Const.} \| \bar{\eta}_x \|_{\alpha}$. This being shown, let us replace $\bar{\eta}$ in (54) and (55) by the elements $\bar{\eta}^{(v)}$ given by Lemma 8. Then letting $v \to \infty$, we obtain from the dominated convergence theorem

$$
\| \eta v_x \|_{\alpha} \le C q^{\alpha/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}), \quad (57)
$$

$$
\| \eta v \|_{\alpha*} \le C q^{\alpha/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}), \quad (58)
$$

where the norms are taken over $S(2) - Q$, and the constant $C$ now depends also on the value of $\delta$.

If $\eta$ is now chosen as in Theorem 1, inequality (58) may be written in the form

$$
\Phi(\varkappa p_0, h') \le [C(p_0/\alpha)^{\alpha/\varepsilon} (h - h')^{-1}]^{\alpha/p_0} \Phi(p_0, h), \quad (59)
$$

where $p_0 = \alpha + \beta_0 - 1 = (\alpha - 1)(1 + \delta)$, and $\Phi(p, h) = (\int_{S(h)-Q} \bar{u}^p dx)^{1/p}$.

(1) For simplicity we suppose that $\alpha < n$. The case $\alpha = n$ requires only trivial changes (cf. Theorem 2).

---

280

JAMES SERRIN

We wish to proceed as in Theorem 1, obtaining a corresponding inequality for each $p > p_0$. This requires a more delicate choice of the test function than previously. For $q \ge q_0 = p_0/\alpha$ and $l > k$, we define

$$
F(\bar{u}) = \begin{cases} \bar{u}^q & \text{if } k \le \bar{u} \le l, \\ q_0^{-1} [q l^{q-q_0} u^{q_0} + (q_0 - q) l^q] & \text{if } l \le \bar{u}, \end{cases}
$$

$$
\text{and} \quad G(u) = \operatorname{sign} u \cdot \{F(\bar{u}) F'(\bar{u})^{\alpha-1} - q^{\alpha-1} k^{\beta}\}, \quad -\infty < u < \infty,
$$

where $q$ and $\beta$ are related by $\alpha q = \alpha + \beta - 1$. Evidently $F$ is a continuously differentiable function of $\bar{u}$, and $G$ is a piecewise smooth function of $u$, with corners at $u = \pm (l - k)$. Moreover, these functions have the properties

$$
F \le (q/q_0) l^{q-q_0} \bar{u}^{q_0}, \quad \bar{u} F' \le qF,
$$

and

$$
G' \ge \begin{cases} q^{-1} \beta(F')^{\alpha} & \text{if } |u| < l - k, \\ q_0^{-1} \beta_0(F')^{\alpha} & \text{if } |u| > l - k. \end{cases}
$$

The first two of these inequalities are quite simple to establish. The third arises from the calculations (1)

$$
G'(u) = (F')^{\alpha} + (\alpha - 1) FF''(F')^{\alpha-2}
$$

$$
= (F')^{\alpha} + (\alpha - 1) \left( \frac{q-1}{q} \right) (F')^{\alpha} = q^{-1} \beta(F')^{\alpha}
$$

if $\bar{u} < l$, and

$$
G'(u) = (F')^{\alpha} + (\alpha - 1) FF''(F')^{\alpha-2}
$$

$$
\ge (F')^{\alpha} + (\alpha - 1) \left( \frac{q_0 - 1}{q_0} \right) (F')^{\alpha} = q_0^{-1} \beta_0(F')^{\alpha}
$$

when $\bar{u} > l$. We may now substitute

$$
\phi(x) = (\eta \bar{\eta})^{\alpha} G(u), \quad (u = u(x))
$$

into (9). Since $|G| \le F(F')^{\alpha-1}$, one finds exactly as in Theorem 1 that

$$
\| \eta \bar{\eta} v \|_{\alpha^*} \le C q^{\alpha/\varepsilon} (\| \eta \bar{\eta} v \|_{\alpha} + \| (\eta \bar{\eta})_x v \|_{\alpha}),
$$

where $v = v(x) = F(\bar{u})$.

Since $v \le \text{Const. } \bar{u}^{q_0}$, it is clear as in the earlier part of the proof that $\| \bar{\eta}_x v \|_{\alpha} \le \text{Const. } \| \bar{\eta}_x \|_s$. Thus replacing $\bar{\eta}$ by $\bar{\eta}^{(\nu)}$ and letting $v \to \infty$, we obtain

$$
\| \eta v \|_{\alpha^*} \le C q^{\alpha/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}).
$$

(1) For the range $\bar{u} > l$ we use the relation $q_0 \le 1$, which is in turn equivalent to $\beta_0 \le 1$ and hence to $\delta \le (\alpha - 1)^{-1}$. But this last inequality can always be assumed without loss of generality.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

281

Here we may let $l \to \infty$. Since $v \to \bar{u}^q$ there results by Lebesgue's theorem

$$
\|\eta \bar{u}^q\|_{\alpha^*} \le C q^{\alpha/\varepsilon} (\|\eta \bar{u}^q\|_{\alpha} + \|\eta_x \bar{u}^q\|_{\alpha}).
$$

Finally, choosing $\eta$ as in Theorem 1 (and as in the earlier part of the proof) yields

$$
\Phi(\varkappa p, h') \le [C(h - h')^{-1} (p/\alpha)^{\alpha/\varepsilon}]^{\alpha/p} \Phi(p, h), \quad (60)
$$

where $p = \alpha q \ge p_0$. We emphasize that (60) is valid whether or not the integrals involved are finite.

Now iterate the inequalities (59), (60) starting with $p = p_0$. This clearly yields the conclusion

$$
\|\bar{u}\|_{\infty} \le C \|\bar{u}\|_{p_0}, \quad (61)
$$

where the left hand norm is over the set $S(1) - Q$ and the right-hand norm is over $S(2) - Q$. But $\|\bar{u}\|_{p_0} \le \|\bar{u}\|_{\theta(1+\delta)}$, so that the right side of (61) is finite. Thus we have shown that $u$ is uniformly bounded on the set $S(1) - Q$.

It remains to establish that $u$ can be made a continuous solution of (5) in all of $S(1)$. Choosing $\eta$ so that $\eta \equiv 1$ in $S(1)$, we have from (57)

$$
\|v_x\|_{\alpha, 1} \le \text{Const.} \quad \|v\|_{\alpha, 2},
$$

that is
$$ \int \bar{u}^{\beta_0 - 1} |u_x|^\alpha dx \le \text{Const.} \int \bar{u}^{\alpha q_0} dx \le \text{Const.} $$

Since $\beta_0 \le 1$ and $\bar{u}$ is bounded in $S(1) - Q$, this proves that $u_x$ is in $L_\alpha$ on the set $S(1) - Q$.

A set of capacity zero is also a set of measure zero (see the corollary in section 10). We shall show that if $u$ is arbitrarily set equal to zero on $Q$ the resulting function is strongly differentiable in $S(1)$. Indeed, for any smooth function $\phi$ with compact support in $S(1) - Q$, we have

$$
\int u \phi_x dx = - \int \phi u_x dx.
$$

Setting $\phi = \eta \bar{\eta}$, where $\eta$ has compact support in $S(1)$, then yields

$$
\int u(\eta \bar{\eta}_x + \bar{\eta} \eta_x) dx = - \int \eta \bar{\eta} u_x dx.
$$

Thus replacing $\bar{\eta}$ by $\bar{\eta}^{(v)}$ and letting $v \to \infty$, we obtain from the dominated convergence theorem

---

282

JAMES SERRIN

$$
\int u\eta_x dx = - \int \eta u_x dx, \qquad (62)
$$

the integrals being evaluated over the set $S(1) - Q$. If one arbitrarily sets $u_x = 0$ on $Q$, relation (62) becomes valid over all of $S(1)$. But this is just the condition that $u$ be strongly differentiable in $S(1)$, and the assertion is proved.

Finally, the functions $\mathcal{A}(x, u, u_x)$ and $\mathcal{B}(x, u, u_x)$ are clearly in $L_{\alpha/(\alpha-1)}$ and $L_{(\alpha^*)}$ over $S(1)$, and

$$
\int (\phi_x \cdot \mathcal{A} + \phi \mathcal{B}) dx = 0
$$

when $\phi$ has compact support in $S(1) - Q$. Again setting $\phi = \eta\bar{\eta}$, we easily obtain in the limit as $v \to \infty$,

$$
\int (\eta_x \cdot \mathcal{A} + \eta \mathcal{B}) dx = 0,
$$

valid whenever $\eta$ has compact support in $S(1)$. It follows that $u$, as defined over $Q$, is a weak solution of (5) in the ball $S(1)$. Finally by Theorem 8 we can redefine $u$ on a set of measure zero so that it is Hölder continuous in $S(1)$. Since this redefinition cannot effect the values of $u$ on $S(1) - Q$, where it is already continuous, we see that by suitably assigning values to $u$ on the set $Q$, it becomes a continuous solution of (5) in $S(1)$, that is, in a non-empty neighborhood of the point $P$. This completes the main part of the proof. It remains only to show that the exponent $\theta = s(\alpha - 1)/(s - \alpha)$ is best possible, and to prove Lemma 8.

In order to show that $\theta$ is the best possible exponent, consider the equation

$$
\operatorname{div} (u_x |u_x|^{\alpha-2}) = 0,
$$

and let $Q$ be the hyperplane $x_1 = \dots = x_s = 0$. Clearly $Q$ has $s$-capacity zero. Now one checks easily that the function

$$
u = \begin{cases} \varrho^{(\alpha-s)/(\alpha-1)}, & \alpha < s \\ \log \varrho, & \alpha = s, \end{cases} \qquad (63)
$$

is a solution, where $\varrho$ denotes the distance to $Q$. Moreover, if $\alpha < s$ then

for any $\varepsilon' > 0$, while if $\alpha = s$ then

$$
u \in L_{\sigma}
$$

for any $\sigma < \infty$. Thus an exponent smaller than $\theta$ in (52) would allow the solution (63) into competition, and the conclusion of the theorem would become impossible.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

283

9. The logarithmic case of Theorem 11

By a smooth change of variables, leaving the form of inequalities (6) invariant, it may be assumed that $Q$ is contained in the set

$$
x_1 = \dots = x_s = 0, \quad |x| \le 3, \qquad (64)
$$

and that $D$ in turn includes the ball $|x| < 2$. In fact, we may even suppose that $Q$ is precisely (64), for this at most enlarges the singular set.

Now, retaining the notation of the preceding section, let us make the same substitution

$$
\phi(x) = (\eta\bar{\eta})^{\alpha} \operatorname{sign} u \cdot \{\bar{u}^{\beta} - k^{\beta}\}, \quad (\beta > 0),
$$

in relation (9). Then we find, by separating out the terms involving $\bar{\eta}_x$,

$$
\begin{aligned} q^{-1} \beta \| \eta \bar{\eta} v_x \|_{\alpha}^{\alpha} &\le \alpha a \int |\eta_x v| \cdot |\eta \bar{\eta} v_x|^{\alpha-1} dx + \alpha q^{\alpha-1} \int \bar{b} |\eta_x v| \cdot (\eta \bar{\eta} v)^{\alpha-1} dx \\ &\quad + \int c \eta v |\eta \bar{\eta} v_x|^{\alpha-1} dx + (1+\beta) q^{\alpha-1} \int d(\eta \bar{\eta} v)^{\alpha} dx \\ &\quad + \alpha \int |\bar{\eta}_x v| \cdot (a |\eta v_x|^{\alpha-1} + q^{\alpha-1} \bar{b} (\eta v)^{\alpha-1}) dx, \end{aligned} \qquad (65)
$$

where it is assumed that both $\eta$ and $\bar{\eta}$ are less than or equal to one. Next, let $\varrho$ denote the distance to $Q$, and for fixed $\sigma > 0$ choose

$$
\bar{\eta}(x) = \begin{cases} 0 & \text{if } \varrho \le \sigma \\ 1 & \text{if } \varrho \ge \sigma + h, \end{cases}
$$

and linear in the interval $\sigma \le \varrho \le \sigma + h$. Now consider the effect of letting $h \to 0$ while keeping $\sigma$ fixed. Since $|\bar{\eta}_x| = h^{-1}$ it is clear from Lebesgue's differentiation theorem that, for almost all values of $\sigma$,

$$
\int |\bar{\eta}_x v| \cdot (a |\eta v_x|^{\alpha-1} + q^{\alpha-1} \bar{b} |\eta v|^{\alpha-1}) dx \to \oint_{\varrho=\sigma} v(a |\eta v_x|^{\alpha-1} + q^{\alpha-1} \bar{b} |\eta v|^{\alpha-1}) ds.
$$

The limit process on the remaining terms of (65) is trivial, hence we have for almost all values of $\sigma$,

$$
\begin{aligned} q^{-1} \beta \| \eta v_x \|_{\alpha}^{\alpha} &\le \alpha a \int |\eta_x v| \cdot |\eta v_x|^{\alpha-1} dx + \alpha q^{\alpha-1} \int \bar{b} |\eta_x v| \cdot (\eta v)^{\alpha-1} dx \\ &\quad + \int c \eta v |\eta v_x|^{\alpha-1} dx + (1+\beta) q^{\alpha-1} \int d(\eta v)^{\alpha} dx \\ &\quad + \alpha \oint_{\varrho=\sigma} v(a |\eta v_x|^{\alpha-1} + q^{\alpha-1} \bar{b} |\eta v|^{\alpha-1}) ds, \end{aligned}
$$

---

284

JAMES SERRIN

the volume integrals being taken over the set where $\varrho > \sigma$. The first four terms on the right may be estimated as in Theorem 1 (we assume $\alpha < n$ for simplicity), with the exception that Lemma 4 must be replaced by the slightly different Lemma 5. Thus we obtain with the help of Lemma 2,

$$
\|\eta v_x\|_{\alpha} \le C(1 + \beta^{-1})^{1/\varepsilon} q^{\alpha/\varepsilon} (\|\eta v\|_{\alpha} + \|\eta_x v\|_{\alpha}) + C \beta^{-1/\alpha} q I(\sigma)^{1/\alpha}, \quad (66)
$$

where

$$
I(\sigma) = \oint_{\varrho=\sigma} v(|\eta v_x|^{\alpha-1} + \bar{b} |\eta v|^{\alpha-1}) ds.
$$

Now by Hölder's inequality and Lemma 1

$$
I(\sigma) \le (2 \oint v^\alpha ds)^{1/\alpha} \left( \oint (|\eta v_x|^\alpha + \bar{b}^{\alpha/(\alpha-1)} |\eta v|^\alpha) ds \right)^{(\alpha-1)/\alpha},
$$

while by hypothesis

$$
\oint v^\alpha ds = \oint \bar{u}^{\alpha q} ds \le \bar{C} \sigma^{s-1} |\log \sigma|^{(\alpha+\beta-1)(1-\delta)},
$$

where $\bar{C}$ is some constant. Since $s = \alpha$ in the present case, one has by setting $\beta = \beta_0 = \delta(\alpha - 1)$ and $\varepsilon' = \delta^2$,

$$
\oint v^\alpha ds \le \bar{C}(\sigma |\log \sigma|^{1-\varepsilon'})^{\alpha-1}.
$$

Furthermore, since $s > 1$ it is easy to see that the terms $\|\eta v\|_{\alpha}$ and $\|\eta_x v\|_{\alpha}$ in (66) are uniformly bounded as $\sigma \to 0$. Let us set

$$
J = J(\sigma) = \int_{\varrho>\sigma} |\eta v_x|^\alpha dx, \quad \Psi = \Psi(x) = \bar{b}^{\alpha/(\alpha-1)} |\eta v|^\alpha.
$$

Then noting that $J'(\sigma) = - \oint |\eta v_x|^\alpha ds$ and using the preceding estimates, a straightforward calculation establishes that (66) may be written in the form

$$
(J - K)^{\alpha/(\alpha-1)} \le \bar{C} \sigma |\log \sigma|^{1-\varepsilon'} \left( -J' + \oint \Psi ds \right), \quad (67)
$$

where

$$
K = C^\alpha q^{\alpha/\varepsilon} (\|\eta v\|_{\alpha} + \|\eta_x v\|_{\alpha})^\alpha,
$$

the norms in the preceding line being taken over the set where $\varrho > 0$, that is, over the complement of $Q$.

We assert that $J \le K$ for all $\sigma > 0$. Indeed, suppose to the contrary that at some value $\sigma = \sigma_0$ we have $J(\sigma_0) > K$. Since $J$ increases as $\sigma$ decreases we have also $J > K$ in the interval $0 < \sigma \le \sigma_0$. Thus setting $H(\sigma) = J(\sigma) - K$ in (67) it may be rewritten

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

285

$$
\frac{1}{\sigma |\log \sigma|^{1-\varepsilon'}} \leqslant - \frac{\bar{C}H'}{H^{\alpha/(\alpha-1)}} + \frac{\bar{C}}{H(\sigma_0)^{\alpha/(\alpha-1)}} \oint \Psi ds,
$$

valid for almost all values of $\sigma$ in the interval $0 < \sigma \leqslant \sigma_0$. Integration of both sides from $\sigma$ to $\sigma_0$ yields

$$
\frac{1}{\varepsilon'} (|\log \sigma|^{\varepsilon'} - |\log \sigma_0|^{\varepsilon'}) \leqslant (\alpha - 1) \bar{C} \left[ \frac{1}{H(\sigma_0)^{1/(\alpha-1)}} - \frac{1}{H(\sigma)^{1/(\alpha-1)}} \right] + \frac{\bar{C}}{H(\sigma_0)^{\alpha/(\alpha-1)}} \int_{\sigma < \varrho < \sigma_0} \Psi dx. \quad (68) \\ \text{But} \quad \int \Psi dx \leqslant \left( \int \bar{b}^{n/(\alpha-1)} dx \right)^{\alpha/n} \left( \int |\eta v|^{\alpha n/(n-\alpha)} dx \right)^{1-\alpha/n},
$$

and the right side is uniformly bounded as $\sigma \to 0$, (recall that $u = O(|\log \varrho|^{1-\delta})$). The right hand side of (68) therefore remains bounded as $\sigma \to 0$, while the left-hand side becomes infinite. This contradiction proves the assertion $J \leqslant K$. Interpreting this in terms of the original functions yields

$$
\| \eta v_x \|_{\alpha} \leqslant C q^{\alpha/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}),
$$

where the norms are taken over the complement of $Q$, and the constant $C$ depends only on $\delta$ and on the structure of equation (5). Finally, applying the Sobolev inequality (Lemma 5) we obtain

$$
\| \eta v \|_{\alpha^*} \leqslant C q^{\alpha/\varepsilon} (\| \eta v \|_{\alpha} + \| \eta_x v \|_{\alpha}).
$$

The preceding two inequalities are the analogues in the present case of (57) and (58) in the foregoing section.

The remainder of the proof is exactly the same as before, except that the limit process $v \to \infty$ must be replaced by the present technique of differential equations. Theorem 11 is thus completely proved.

## 10. Capacity

Here we shall prove Lemma 8, and also present some simple results about $s$-capacity which will be useful in the sequel.

*Proof of Lemma 8.* For simplicity we shall consider only the case $s < n$, the remaining case $s = n$ being treated by similar methods. Now according to hypothesis, there exists a sequence of continuously differentiable functions $\psi^{(\nu)}$ with compact support in $E^n$, $\geqslant 1$ on $Q$, and such that

---

286

JAMES SERRIN

$$
\int |\psi_x^{(v)}|^s dx \le 1/v. \qquad (69)
$$

The function $2\psi^{(v)}$ is $> 1$ in some neighborhood of $Q$. Consider then the truncated functions

$$
\bar{\psi}^{(v)} = \begin{cases} 0, & \text{where } \psi^{(v)} < 0, \\ 2\psi^{(v)}, & \text{where } 0 \le 2\psi^{(v)} \le 1, \\ 1, & \text{where } 2\psi^{(v)} > 1. \end{cases}
$$

Evidently $\bar{\psi}^{(v)}$ is strongly differentiable, equals one in some neighborhood of $Q$, and satisfies

$$
\int |\bar{\psi}_x^{(v)}|^s dx \le 2^s \int |\psi_x^{(v)}|^s dx \le 2^s/v. \qquad (70)
$$

Moreover, $\bar{\psi}^{(v)}$ has compact support in $E^n$. Therefore by Lemma 4 and (70),

$$
\|\bar{\psi}^{(v)}\|_{s*} \le \text{Const.}/v.
$$

Consequently $\bar{\psi}^{(v)}$ converges to zero in measure, whence for some subsequence (still denoted by $\bar{\psi}^{(v)}$) we have

$$
\bar{\psi}^{(v)} \to 0 \text{ almost everywhere.} \qquad (71)
$$

This being shown, it is easy to see that the sequence $\bar{\eta}^{(v)} = 1 - \bar{\psi}^{(v)}$ fulfills the conditions of the lemma, with the single exception that each $\bar{\eta}^{(v)}$ is only Lipschitz continuous and not continuously differentiable. This defect can be removed by a suitable mollification, or alternately one can easily justify the direct substitution of $\bar{\eta}^{(v)}$ for $\bar{\eta}$. This completes the proof.

**COROLLARY.** If $Q$ is a compact set of $s$-capacity zero, $1 \le s \le n$, then $|Q| = 0$.

*Proof.* The function $\bar{\psi}^{(v)}$ above is equal to one on $Q$ for each value of $v$. On the other hand, $\bar{\psi}^{(v)} \to 0$ almost everywhere. Hence obviously $|Q| = 0$.

**LEMMA 9.** If $\psi$ is any continuous strongly differentiable function with compact support in $E^n$, and if $\psi \ge 1$ on $Q$, then

$$
\int |\psi_x|^s dx \ge \text{Cap}_s Q.
$$

*Proof.* If the result were not true we could construct a continuously differentiable function $\bar{\psi}$ with compact support in $E^n$, such that $\bar{\psi} \ge 1$ on $Q$ and $\|\bar{\psi}_x\|_s^s < \text{Cap}_s Q$,

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

287

which would be impossible. The construction involves first multiplying $\psi$ by $(1 + \varepsilon')$, so that the resulting function is $\ge (1 + \varepsilon')$ on $Q$, and then forming a smooth integral average. The details may be omitted.

LEMMA 10. For a ball $S(R)$ of radius $R$ we have

$$
\mathrm{Cap}_{\alpha} S(R) = \begin{cases} \omega_n \left(\frac{n-\alpha}{\alpha-1}\right)^{\alpha-1} R^{n-\alpha} & (1 < \alpha < n), \\ \omega_n \log (R_0/R)^{1-n} & (\alpha = n). \end{cases}
$$

Proof. Suppose first that $\alpha < n$, and set $\tau = (\alpha - n)/(\alpha - 1)$. The function

$$
h = h(r) = \frac{r^{\tau} - R_0^{\tau}}{R^{\tau} - R_0^{\tau}},
$$

where $r = |x|$ and $R_0 > R$, is then a solution of the differential equation

$$
\mathrm{div} (u_x |u_x|^{\alpha-2}) = 0, \qquad (72)
$$

that is, the Euler equation of the variational problem $\int |u_x|^\alpha dx = \text{Minimum}$. Evidently $h=0$ when $r=R_0$ and $h=1$ when $r=R$. By standard comparison arguments in the calculus of variations it follows that

$$
\| \psi_x \|_{\alpha} \ge \| h_x \|_{\alpha} \quad (\text{over } R < r < R_0),
$$

where $\psi$ is any continuously differentiable function $\ge 1$ on $S(R)$ and with compact support in $r < R_0$. Therefore it is clear that

$$
\mathrm{Cap}_{\alpha} S(R) \ge \lim_{R_0 \to \infty} \| h_x \|_{\alpha}^{\alpha}.
$$

Similarly by setting $\psi(x) = 0$ for $r \ge R_0$, $\psi(x) = h(r)$ for $R < r < R_0$, and $\psi(x) = 1$ for $r \le R$, and using Lemma 9 we have

$$
\mathrm{Cap}_{\alpha} S(R) \le \lim_{R_0 \to \infty} \| h_x \|_{\alpha}^{\alpha}.
$$

The required conclusion follows immediately from the calculation

$$
\| h_x \|_{\alpha}^{\alpha} = \omega_n |\tau / (R^{\tau} - R_0^{\tau})|^{\alpha-1}.
$$

The case $\alpha = n$ is handled in the same way, except that $h(r) = \log (r/R_0)/\log (R/R_0)$.

This result indicates the close connection between $\alpha$-capacity and equation (72), a connection well-known if $\alpha = 2$.

19-642946 Acta mathematica. 111. Imprimé le 9 juin 1964

---

288

JAMES SERRIN

11. A remark concerning the case $\alpha=1$

The result of Theorem 10 can be generalized to apply to equation (5) even for the case $\alpha=1$, that is, when the functions $\mathcal{A}$ and $\mathcal{B}$ satisfy

$$
|\mathcal{A}| \leqslant \text{Const.}, \quad |\mathcal{B}| \leqslant f,
$$

and

$$
p \cdot \mathcal{A} \geqslant |p| - d|u| - g
$$

with $d, f, g \in L_{n/(1-\varepsilon)}$. Indeed we have the following

THEOREM 10'. Let $Q$ be a compact set of 1-capacity zero, and let $D$ be a domain in $\Omega$. Suppose that $u$ is a solution of (5) in the set $D-Q$, and that the functions $\mathcal{A}$ and $\mathcal{B}$ satisfy the conditions above. Then, if

$$
u \in L_{\delta}
$$

for some $\delta > 0$, we can define $u$ on the set $Q$ so that the resulting function is a solution of (5) in all of $D$.

Proof. Let $S(2)$ be an open ball in $D$, and define

$$
\bar{u} = |u| + k, \quad \bar{u}_l = \text{Min}(l, \bar{u}),
$$

where $k = 1 + \|g\|$, and $l$ is some large constant. We introduce the test function

$$
\phi = (\eta\bar{\eta}) \text{sign } u \cdot \{\bar{u}_l^\beta - k^\beta\}, \quad x \in S(2) - Q,
$$

as in the proof of Theorem 10. In the set where $\bar{u} < l$ we have

$$
\phi_x \cdot \mathcal{A} + \varphi \mathcal{B} \geqslant (\eta\bar{\eta}) |v_x| - \text{Const.} (\eta\bar{\eta})_x v - (\beta \bar{d} + f) \eta\bar{\eta} v,
$$

where we have put $v = \bar{u}_l^\beta$. Similarly, when $\bar{u} \geqslant l$

$$
\phi_x \cdot \mathcal{A} + \varphi \mathcal{B} \geqslant - \text{Const.} (\eta\bar{\eta})_x l^\beta - f \eta\bar{\eta} l^\beta \\ \geqslant (\eta\bar{\eta}) |v_x| - \text{Const.} (\eta\bar{\eta})_x v - (\beta \bar{d} + f) \eta\bar{\eta} v
$$

since $v = l^\beta$ in this set. Hence as in the proof of Theorem 1 (or Theorem 10), we may derive the relations

$$
\|\eta\bar{\eta} v_x\|_1 \leqslant C(1 + \beta)^{1/\varepsilon} (\|\eta\bar{\eta} v\|_1 + \|(\eta\bar{\eta})_x v\|_1)
$$

and

$$
\|\eta\bar{\eta} v\|_{1*} \leqslant C(1 + \beta)^{1/\varepsilon} (\|\eta\bar{\eta} v\|_1 + \|(\eta\bar{\eta})_x v\|_1).
$$

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

289

Now the term $\|\bar{\eta}_x v\|$ which appears in both preceding lines satisfies the inequality $\|\bar{\eta}_x v\|_1 \le l^\beta \|\bar{\eta}_x\|_1$. Hence replacing $\bar{\eta}$ by $\bar{\eta}^{(v)}$ and letting $v \to \infty$, we obtain

$$
\|\eta v_x\|_1 \le C(1 + \beta)^{1/\varepsilon} (\|\eta v\|_1 + \|\eta_x v\|_1) \quad (73)
$$

and

$$
\|\eta v\|_1^* \le C(1 + \beta)^{1/\varepsilon} (\|\eta v\|_1 + \|\eta_x v\|_1). \quad (74)
$$

Here we may let $l \to \infty$. Since $v \to \bar{u}^\beta$ and $v_x \to (\bar{u}^\beta)_x$, it follows from the monotone convergence theorem that (73) and (74) hold with $v$ replaced by $\bar{u}^\beta$.

Iteration of (74) beginning with $\beta = \delta$ establishes that $\bar{u}$ is bounded in $S(1) - Q$. The rest of the proof is then the same as in Theorem 10. It should be remarked, however, that since there is no analogue of Theorem 8 for the case $\alpha = 1$ the *continuity* of the solution remains an open problem; in special cases (e.g. the minimal surface equation in two dimensions) one may, of course, be able to settle this question by an independent investigation.

In conclusion, we note that Theorem 10' is quite similar in both hypothesis and conclusion to a well known removable singularity theorem due to Finn.

### III. Isolated singularities

A detailed description of the behavior of solutions at an isolated singularity seems to require some specialization of equation (5). We shall consider the equation

$$
\operatorname{div} \mathcal{A}(x, u, u_x) = 0, \quad (\alpha \le n), \quad (75)
$$

which is, of course, sufficiently general to include the Euler equations of variational problems with integrand independent of $u$. It will be assumed that the function $\mathcal{A}(x, u, p)$ satisfies the conditions

$$
|\mathcal{A}| \le a |p|^{\alpha-1} + b |u|^{\alpha-1} + e, \quad p \cdot \mathcal{A} \ge |p|^{\alpha} - d |u|^{\alpha} - g, \quad (76)
$$

where $b, d, e$ and $g$ are measurable functions defined in the basic domain $\Omega$ and contained in the respective Lebesgue classes

$$
b \in L_{n/(\alpha-1)}; \quad e \in L_{n/(\alpha-1-\varepsilon)}; \quad d, g \in L_{n/(\alpha-\varepsilon)}; \quad (77)
$$

(when $\alpha = n$ we require further that $b \in L_{n/(n-1-\varepsilon)}$).

In Section 12 we shall consider the general behavior of a solution at an isolated non-removable singularity. The final sections of the paper establish the existence of solutions with positive singularities under suitable additional conditions.

---

290

JAMES SERRIN

12. Behavior of solutions at an isolated singularity

Under the assumptions (76, 77) noted above we have the following basic result.

THEOREM 12. Let $u$ be a continuous solution of (75) in the set $D - \{0\}$, where $D$ is a domain in $\Omega$. Suppose that $u \ge L$, for some constant $L$. Then either $u$ has a removable singularity at 0, or else

$$
u \approx \begin{cases} r^{(\alpha-1)/(\alpha-1)}, & \alpha < n, \\ \log 1/r, & \alpha = n, \end{cases} \qquad (78)
$$

in the neighborhood of the origin. (Here $f \approx g$ means that $C' \le f/g \le C''$ where $C'$ and $C''$ are positive constants.)

Proof. Let $\Theta$ be a strongly differentiable function with compact support in $D$, which is identically 1 in some neighborhood of the origin. We assert that

$$
\int \Theta_x \cdot \mathcal{A} \, dx = \text{Const.} = K, \qquad (79)
$$

where the constant is independent of the particular choice of $\Theta$.

In order to see this, let $\Theta$ and $\bar{\Theta}$ be two functions satisfying the above condition (that is, with compact support in $D$ and identically 1 in a neighborhood of 0). Then $\phi = \bar{\Theta} - \Theta$ has compact support in $D - \{0\}$. Therefore

$$
\int (\bar{\Theta} - \Theta)_x \cdot \mathcal{A} \, dx = 0,
$$

or in other words,

$$
\int \bar{\Theta}_x \cdot \mathcal{A} \, dx = \int \Theta_x \cdot \mathcal{A} \, dx.
$$

This proves the assertion.

Now assume that the singularity at 0 is not removable. We must then prove that $u$ has the asymptotic behavior (78) at 0. Let $R$ be chosen so that $D$ contains the ball $r = |x| \le R$. We may assume without loss of generality, moreover, that $u < 0$ on the circumference $|x| = R$. By the remark at the end of Section 7 it is clear that $u \to \infty$ as $x \to 0$. Hence there exists some constant $\sigma_0 > 0$ such that $u > 0$ for $|x| \le \sigma_0$. Let $M = M(\sigma)$ and $\mu = \mu(\sigma)$ be respectively the maximum and minimum of $u$ on a given circumference $|x| = \sigma < \sigma_0$. Furthermore, for $\sigma < |x| < R$ let us define the function

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

291

$$
v = v(x, \sigma) = \begin{cases} 0 & \text{if } u(x) \le 0, \\ u(x) & \text{if } 0 < u(x) < \mu, \\ \mu & \text{if } u(x) \ge \mu. \end{cases}
$$

We may suppose the definition of $v$ is extended to all of $E^n$ by setting $v=0$ for $|x| \ge R$ and $v=\mu$ for $|x| \le \sigma$. Then $v$ is strongly differentiable in all space, has compact support in $D$, and is identically equal to $\mu$ in some neighborhood of the origin. Now for fixed $\sigma < \sigma_0$, and $\mu = \mu(\sigma)$, $v = v(x, \sigma)$, we have by (79)

$$
\mu K = \int v_x \cdot \mathcal{A}(x, u, u_x) dx = \int v_x \cdot \mathcal{A}(x, v, v_x) dx, \quad (80)
$$

since $v=u$ and $v_x=u_x$ almost everywhere in the set where $v_x \ne 0$ (see the remarks at the conclusion of Section 0). By inequality (76), moreover,

$$
\int v_x \cdot \mathcal{A}(x, v, v_x) dx \ge \int (|v_x|^\alpha - d|v|^\alpha - g) dx. \quad (81)
$$

The second term on the right may be estimated by Hölder's inequality and Lemma 4, thus (1)

$$
\int d|v|^\alpha dx \le \|d\|_{n/\alpha} \|v\|_{\alpha^*}^\alpha \le \text{Const.} \|d\|_{n/\alpha} \|v_x\|_\alpha^\alpha. \quad (82)
$$

Now the radius $R$ introduced at the beginning of the proof may be taken as small as we please, and therefore it is clear that we may suppose Const. $\|d\|_{n/\alpha} \le \frac{1}{2}$. Hence by (81) and (82)

$$
\int v_x \cdot \mathcal{A}(x, v, v_x) dx \ge \frac{1}{2} \int |v_x|^\alpha dx - C. \quad (83)
$$

Moreover, by Lemma 9 and Lemma 10, since $v \equiv \mu$ for $|x| \le \sigma$,

$$
\int |v_x|^\alpha dx \ge \omega_n \left( \frac{n-\alpha}{\alpha-1} \right)^{\alpha-1} \sigma^{n-\alpha} \mu^\alpha \quad (84)
$$

(assuming $\alpha < n$). Thus from (80), (83), and (84) follows

$$
\mu^\alpha \le \text{Const.} (\mu K + C) \begin{cases} \sigma^{\alpha-n}, & \alpha < n, \\ |\log \sigma|^{n-1}, & \alpha = n, \end{cases} \quad (85)
$$

valid for $\sigma < \sigma_0$.

(1) The calculation is given only for the case $\alpha < n$. If $\alpha = n$ only slight changes are necessary.

---

292

JAMES SERRIN

We assert that $K>0$. Indeed in the contrary case we obtain from (85)

$$
\mu \leqslant \text{Const.} \begin{cases} \sigma^{(\alpha-n)/\alpha}, & \alpha < n, \\ |\log \sigma|^{1-1/n}, & \alpha = n. \end{cases}
$$

But then by the Harnack inequality, (Theorem 7), the value $M = M(\sigma)$ obeys the same relation. Thus $u = O(r^{(\alpha-n)/\alpha})$ or $O(|\log r|^{1-1/n})$ depending on whether $\alpha < n$ or $\alpha = n$. Therefore by Theorem 11 the singularity at 0 is removable, which contradicts our initial assumption. The assertion thus being established, it now follows from (85) and Lemma 2 that

$$
\mu \leqslant \text{Const.} \begin{cases} \sigma^{(\alpha-n)/(\alpha-1)}, & \alpha < n, \\ |\log \sigma|, & \alpha = n. \end{cases} \quad (86)
$$

The next step in the proof is to obtain a reverse inequality (cf. (92) below) for the value $M$. To this end we introduce a new comparison function $V = V(x, \sigma)$ according to the formula

$$
V = \begin{cases} 0 & \text{when } |x| \geqslant R \\ \text{Max}(0, u) & \text{when } \sigma_0 < |x| < R \\ u & \text{when } \sigma \leqslant |x| \leqslant \sigma_0 \\ \text{Min}(M, u) & \text{when } 0 < |x| < \sigma \\ M & \text{when } |x| = 0. \end{cases}
$$

Evidently $V$ is continuous and strongly differentiable, has compact support in $D$, and $V \equiv M$ in some neighborhood of the origin. Moreover, for fixed $\sigma < \sigma_0$, and $\tau = (\alpha - n)/(\alpha - 1)$, we set (1)

$$
H = H(r, \sigma) = \begin{cases} 0 & \text{when } |x| \geqslant \sigma_0 \\ M \frac{r^\tau - \sigma_0^\tau}{\sigma^\tau - \sigma_0^\tau} & \text{when } \sigma < |x| < \sigma_0 \\ M & \text{when } |x| \leqslant \sigma. \end{cases}
$$

Again $H$ is strongly differentiable, has compact support in $D$, and $H \equiv M$ in a neighborhood of the origin. Thus letting $\Delta$ denote the annulus $\sigma < r < \sigma_0$, we have by (79),

$$
MK = \int H_x \cdot \mathcal{A} dx \leqslant \int_{\Delta} \left\{ \frac{1}{\alpha} \left| \frac{H_x}{\varepsilon} \right|^{\alpha} + \frac{\alpha - 1}{\alpha} |\varepsilon \mathcal{A}|^{\alpha/(\alpha-1)} \right\} dx, \quad (87)
$$

using Young's inequality. Now by (76)

(1) Cf. the preceding footnote.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

293

$$
\begin{align}
\int_{\Delta} |\mathcal{A}|^{\alpha/(\alpha-1)} dx &\le C \int_{\Delta} \{|u_x|^\alpha + b^{\alpha/(\alpha-1)} |u|^\alpha + e^{\alpha/(\alpha-1)}\} dx \nonumber \\
&= C \int_{\Delta} \{|u_x|^\alpha - 2d|u|^\alpha - 2g + (2d + b^{\alpha/(\alpha-1)})|u|^\alpha + (2g + e^{\alpha/(\alpha-1)})\} dx. \tag{88}
\end{align}
$$

The integral on the right side of (88) is only increased if it is extended over the set of points in $0 < |x| < R$ where $V = u$. Denoting this set by $\Delta'$ we have

$$
\begin{align}
\int_{\Delta'} (2d + b^{\alpha/(\alpha-1)}) |u|^\alpha dx &\le \int (2d + b^{\alpha/(\alpha-1)}) |V|^\alpha dx \nonumber \\
&\le \text{Const.} (\|d\|_{n/\alpha} + \|b\|_{n/(\alpha-1)}^{\alpha/(\alpha-1)}) \cdot \|V_x\|_\alpha^\alpha \nonumber \\
&= \text{Const.} (\|d\|_{n/\alpha} + \|b\|_{n/(\alpha-1)}^{\alpha/(\alpha-1)}) \cdot \int_{\Delta'} |u_x|_\alpha dx, \tag{89}
\end{align}
$$

since $V_x = u_x$ almost everywhere in $\Delta'$ and $V_x = 0$ almost everywhere in the complement of $\Delta'$. Again supposing that $R$ is suitably small, (89) implies

$$
\int_{\Delta'} (2d + b^{\alpha/(\alpha-1)}) |u|^\alpha dx \le \int_{\Delta'} |u_x|^\alpha dx.
$$

Substituting this into (88), and then using (76), yields

$$
\int_{\Delta} |\mathcal{A}|^{\alpha/(\alpha-1)} dx \le C \left( 1 + \int_{\Delta'} u_x \cdot \mathcal{A} dx \right) = C \left( 1 + \int V_x \cdot \mathcal{A} dx \right) = C(1 + MK). \quad (90)
$$

Combining (87) and (90) there results

$$
MK \le (1/\alpha \varepsilon^\alpha) \|H_x\|_\alpha^\alpha + C \varepsilon^{\alpha/(\alpha-1)} (1 + MK).
$$

Thus choosing $\varepsilon$ so that $C\varepsilon^{\alpha/(\alpha-1)} = \frac{1}{2}$, we obtain

$$
MK \le \text{Const.} \|H_x\|_\alpha^\alpha + 1.
$$

On the other hand, by the calculation of Lemma 10,

$$
\|H_x\|_\alpha^\alpha = \omega_n \left(\frac{n-\alpha}{\alpha-1}\right)^{\alpha-1} (\sigma^\tau - \sigma_0^\tau)^{1-\alpha} M^\alpha.
$$

$$
\text{Therefore} \qquad CM^\alpha \ge (MK-1) \begin{cases} (\sigma^\tau - \sigma_0^\tau)^{\alpha-1}, & \alpha < n, \\ |\log (\sigma/\sigma_0)|^{n-1}, & \alpha = n, \end{cases} \quad (91)
$$

valid for $\sigma < \sigma_0$. It has already been noted that $u \to \infty$ as $x \to 0$. Hence there exists some number $\sigma_1$, $0 < \sigma_1 < \sigma_0$, such that for all $\sigma \le \sigma_1$,

---

294

JAMES SERRIN

$$
MK \ge 2, \quad (\sigma/\sigma_0)^\tau \ge 2.
$$

It follows from (81), therefore, that

$$
M \ge \text{Const.} \begin{cases} \sigma^{(\alpha-n)/(\alpha-1)}, & \alpha < n, \\ |\log \sigma|, & \alpha = n, \end{cases} \quad (92)
$$

valid for all $\sigma \le \sigma_1$.

What has been shown, then, is (by (86)) that the minimum of $u$ grows at most at the rate $r^{(\alpha-n)/(\alpha-1)}$, while the maximum grows at least this fast. The required asymptotic estimate then follows from the Harnack inequality. Indeed, by (86) and Theorem 7 we have

$$
M \le C'(\mu + k') \le \text{Const.} \sigma^{(\alpha-n)/(\alpha-1)}, \quad (\sigma \le \sigma_1),
$$

while by (92) and Theorem 7

$$
\mu \ge M/C' - k' \ge \text{Const.} \sigma^{(\alpha-n)/(\alpha-1)}, \quad (\sigma \le \sigma_1)
$$

(in applying Theorem 7 one first normalizes each sphere $|x| = \sigma$ to unit radius). Thus (78) holds in a neighborhood of the origin, when $\alpha < n$. The result for $\alpha = n$ is obtained in the same way, and Theorem 12 is completed.

## 13. Existence of solutions with isolated singularities

The very light hypotheses required for the proof of Theorem 12 do not seem strong enough to prove the general existence of solutions having positive isolated singularities. We shall therefore restrict consideration in this section to the equation

$$
\operatorname{div} \mathcal{A}(x, u_x) = 0, \quad (\alpha \le n), \quad (93)
$$

where the function $\mathcal{A}$ is independent of $u$. In addition to the usual conditions on $\mathcal{A}$, we shall suppose that (93) also has the following four properties.

P1. For all $x \in \Omega$ and all values of $p$ and $q$

$$
(p - q) \cdot \{\mathcal{A}(x, p) - \mathcal{A}(x, q)\} \ge 0,
$$

with equality holding if and only if $p = q$.

P2. For smooth boundaries and smooth (continuous) boundary data there exist smooth (continuous) solutions of (93) taking on the given boundary data.

P3. The uniform limit of solutions of (93) is also a solution of (93), and

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

295

P4. Let $\Gamma$ denote a spherical annulus in $\Omega$ with center at the origin. By P2 there exists a solution $v$ of (93) in $\Gamma$, taking the constant values $m_0$ on the outer circumference and $m$ on the inner. Also by virtue of assumption P1 a weak maximum principle holds for the difference of any two solutions. Consequently at any point $P$ in $\Gamma$ the values $v(P)$ increase monotonically with $m$. As the final assumption, we suppose that $v(P)$ tends to infinity as $m$ does.

We observe that P1 is easily verified for linear elliptic equations, and also for variational problems whose integrands are strictly convex in the variable $p$. More generally if $\mathcal{A}$ is of class $C^1$ in $p$, then P1 follows from the condition that $\mathcal{A}_{i,k} \xi_i \xi_k$ be positive definite.

Assumption P2 is satisfied for a wide class of equations of the form (93), as shown by the work of Morrey, Ladyzhenskaya and Uraltseva, Gilbarg, and Stampacchia. It would be superfluous to elaborate on this, however, for on the one hand new classes of equations for which P2 holds will certainly be discovered, while on the other it seems that only in pathological circumstances will P2 generally fail.

Turning to assumption P3, it is not hard to see that it holds for linear equations, and for equations admitting an *a priori* estimate of the continuity modulus of the first derivative of solutions. P3 may also be established in case $\mathcal{A}(x, p)$ is continuous in all its variables, though this is more delicate and is stated merely for the record.

Assumption P4 is of rather a different sort, and we shall therefore note here a class of equations for which it is valid. In particular, suppose that $\mathcal{A}$ is of class $C^1$ in $x$ and $p$, at least for all suitably large values of $p$, and let

$$
\lambda = \lambda(x, p), \quad \Lambda = \Lambda(x, p)
$$

be respectively the minimum and maximum eigenvalues of the quadratic form $\mathcal{A}_{i,k} \xi_i \xi_k$ (by condition P1 it is clear that $\lambda \ge 0$). We now assume that the quantities

$$
\Lambda/\lambda \quad \text{and} \quad \left| \sum \frac{\partial \mathcal{A}_i}{\partial x_k} \right| / \lambda |p| \qquad (94)
$$

are uniformly bounded for suitably large values of $p$. (1) Then P4 holds.

To see this, suppose for definiteness that the annulus $\Gamma$ has outer radius 1 and inner radius $\sigma$, and consider the function

(1) This condition is satisfied by many of the equations studied in the recent literature (cf. [5], [8], [9], [15], [25], etc.).

---

296

JAMES SERRIN

$$
k = k(r) = (m - m_0) \frac{r^\gamma - 1}{\sigma^\gamma - 1} + m_0, \quad (\gamma = \text{Const.} < 0).
$$

$$
\text{Then} \quad \operatorname{div} \mathcal{A}(x, k_x) = (\mathcal{A}_{i,k} \xi_i \xi_k) k'' + (\mathcal{A}_{i,l} - \mathcal{A}_{i,k} \xi_i \xi_k) k'/r + \sum \frac{\partial \mathcal{A}_i}{\partial x_i} \\ \geq \lambda k'' + (n-1) \Lambda k'/r - \left| \sum \frac{\partial \mathcal{A}_i}{\partial x_k} \right|,
$$

where $\xi = x/r$ and the primes denote differentiation with respect to $r$. Now let $B$ be a bound for the quantities (94) when $p \geqslant N$, say. We choose $\gamma$ according to the relation

$$
1 - \gamma = nB.
$$

Therefore $|k_x| = -k' = -\gamma(m - m_0) (\sigma^\gamma - 1)^{-1} r^{\gamma-1}$ is greater than $N$ for all $m$ sufficiently large. Consequently for large $m$,

$$
\operatorname{div} \mathcal{A}(x, k_x) \geq -\lambda\gamma(m - m_0) (\sigma^\gamma - 1)^{-1} r^{\gamma-2} \cdot \{(1 - \gamma) - nB\} = 0.
$$

Thus by virtue of the maximum principle one has $v \geqslant k$, where $v$ is the solution postulated in assumption $P4$. But $k(P) \to \infty$ as $m \to \infty$, hence so does $v(P)$, completing the demonstration.

This completes our discussion of assumptions $P1$ through $P4$. We emphasize that the restrictions placed on (93) by these conditions are not particularly heavy, so that the following result holds in considerable generality.

**THEOREM 13.** Suppose that equation (93) admits the properties $P1$ through $P4$ listed above. Let smooth (continuous) boundary data $\psi = \psi(x)$ be assigned on the sphere $|x| = 1$, it being assumed that $|x| < 1$ is contained in $\Omega$.

Then there exists a one parameter, linearly ordered, family of solutions $G = G(x)$ in the domain $0 < |x| < 1$, taking on the given boundary values and satisfying

$$
G \approx \begin{cases} r^{(\alpha-n)!(\alpha-1)}, & \alpha < n, \\ \log 1/r, & \alpha = n, \end{cases} \qquad (95)
$$

in the neighborhood of the origin. The value of $G$ may be assigned arbitrarily at a given point $P$, subject only to the restriction $G(P) > w(P)$, where $w$ denotes the solution of (93) in the ball $|x| < 1$ which takes on the assigned boundary values.

*Remark.* By linearly ordered, we mean that if $G_1$ and $G_2$ are two different members of the family, then either $G_1 \leqslant G_2$ or $G_1 \geqslant G_2$ in $0 < |x| < 1$.

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

297

*Proof of Theorem 13.* We shall first construct a solution $G=G(x)$ in $0<|x|<1$ taking on the assigned boundary data, and with a prescribed value $\chi>w(P)$ at some fixed point $P$. It will then be shown that this solution satisfies (95), and finally that it can be assumed to increase as $\chi$ increases. By making the change of dependent variables $\bar{u}=u+\text{const.}$, with the constant suitably chosen, it may be supposed without loss of generality that $w \ge 0$. We assume this done, and then drop the bar on $u$.

Now let $\Gamma_\sigma$ denote the annulus $\sigma<|x|<1$, and let $v_{\sigma,m}$ be the particular solution of (93) in $\Gamma_\sigma$ which obeys the boundary conditions

$$
v=\psi \text{ on } |x|=1, \quad v=w+m \text{ on } |x|=\sigma.
$$

Obviously such a solution exists by assumption P2. We assert that $m$ can be chosen in such a way that

$$
v_{\sigma,m}(P) = \chi \qquad (96)
$$

(it is assumed that $\sigma$ is small enough for $P$ to be contained in $\Gamma_\sigma$). Indeed, if $m=0$ then obviously $v_{\sigma,m}=w$, while by the maximum principle the value $v_{\sigma,m}(P)$ continuously increases as $m$ increases. By assumption P4 it is evident that $v_{\sigma,m}(P)$ tends to infinity as $m$ does. Hence there exists a first value $m=m(\sigma)$ such that (96) holds. We shall henceforth write $v_\sigma$ for the function $v_{\sigma,m(\sigma)}$.

Now each function $v_\sigma$ is a positive solution of (93) in the corresponding annulus $\Gamma_\sigma$, and satisfies $v_\sigma(P)=\chi$. If we write $\theta=|x_P|$, then by the Harnack inequality (Theorem 7) we have for fixed $C'$ and $k'$

$$
v_\sigma(x) \le C'(\chi + k') \text{ on } |x| = \theta,
$$

so long as $\sigma \le \theta/2$. Let $W$ be the solution of (93) in the annulus $\Gamma_\theta$ taking on the boundary values

$$
W = \psi \text{ on } |x| = 1, \quad W = C'(\chi + k') \text{ on } |x| = \theta.
$$

Then according to the maximum principle

$$
w \le v_\sigma \le W \text{ in } \Gamma_\theta,
$$

valid for all $\sigma \le \theta/2$. We assert also that in each fixed annulus $h<|x|<1-h$ the functions $v_\sigma$ are uniformly bounded and equicontinuous, provided that $\sigma \le h/4$. Indeed by the Harnack inequality it is not hard to see that $v_\sigma$ must be uniformly bounded in $h/2<|x|<1$, when $\sigma \le h/4$. But then by Theorem 8 these functions are equicontinuous in $h<|x|<1-h$, as asserted.

---

298

JAMES SERRIN

Now consider the family $\{v_\sigma\}$ as $\sigma \to 0$. It is clear from what has already been shown that there is a sequence of values $\sigma_1, \sigma_2, \dots$ such that

$$
v_{\sigma_v}(x) \to \text{limit}, \quad 0 < |x| < 1,
$$

the convergence being uniform in any fixed annulus $h < |x| < 1 - h$, (Ascoli's theorem). We denote the limit by $G(x)$. Clearly $G(x)$ is a continuous function satisfying $G(P) = \chi$. Moreover,

$$
w \le G \le W \quad \text{in} \quad \Gamma_\theta.
$$

It thus follows that $G$ is continuous in $0 < |x| \le 1$ and takes the assigned boundary values on $|x| = 1$, as required.

That $G$ is a solution of (93) in $0 < |x| < 1$ follows immediately from property P3. It still must be shown that $G$ has the asymptotic behavior (95). By Theorem 12, however, any solution which is bounded below must either satisfy (95) or have a removable singularity at 0. It is therefore enough to show that $G$ cannot have a removable singularity. Thus suppose for contradiction that $G$ could be defined at 0 so as to be a solution in the entire ball $|x| < 1$. Then since $G = \psi$ on $|x| = 1$ we would necessarily have $G \equiv w$ by the maximum principle. This is impossible, however, since $G(P) = \chi > w(P)$. Thus (95) is established.

It remains to show that the above construction leads to a one parameter linearly ordered family of solutions. Let a dense denumerable set of values $\chi$ be chosen in the interval $(w(P), \infty)$. Then it is clear that, by a diagonal process, a fixed sequence $\sigma_1, \sigma_2, \dots$ can be used to define the functions $G$ corresponding to every $\chi$ in the set. But in this case the functions $v_{\sigma_v}$ corresponding to a particular value of $\chi$ are less than or equal to those belonging to a larger value of $\chi$ (recall the unique definition of each function $v_\sigma$). It follows that if $\chi_1$ and $\chi_2$ are two values in the set, with $\chi_1 < \chi_2$, then also $G_1 \le G_2$. Having thus obtained a monotone family of solutions $G$ for the values of $\chi$ in a dense set, it is now a simple matter to construct solutions for the omitted values of $\chi$, by taking limits of those already constructed. We may omit the details of this process, which depend of course on Theorem 8 and property P3. This completes the proof of Theorem 13.

14. Linear equations

The results of the preceding sections can be sharpened somewhat in case (93) is linear, that is, of the form

---

LOCAL BEHAVIOR OF SOLUTIONS OF QUASI-LINEAR EQUATIONS

299

$$
\frac{\partial}{\partial x_i} \left( a_{ij}(x) \frac{\partial u}{\partial x_j} \right) = 0, \qquad (97)
$$

where $\lambda\xi^2 \le a_{ij}\xi_i\xi_j \le \Lambda\xi^2$ and $\lambda$ and $\Lambda$ are positive constants. We note that assumptions P1 through P4 are satisfied in the present case—P1 quite obviously, P2 on the basis of the work of Ladyzhenskaya and Uraltseva, P3 in view of Theorem 1 and the weak compactness of $L_2$, and finally P4 by virtue of linearity. This being established, it follows that both Theorems 12 and 13 hold for equation (97), with $\alpha=2$. (1) In addition, we have the following supplementary results.

**THEOREM 14.** Let $G$ be a particular solution of (97) in the set $D - \{0\}$, such that $G \approx r^{2-n}$ or $G \approx \log 1/r$ depending on whether $n>2$ or $n=2$. Then every non-negative solution of (97) in $D - \{0\}$ has the form

$$
u = \text{Const. } G + w,
$$

where $w$ is a solution of (97) in the entire domain $D$.

*Remark.* It follows that in the case of equation (97) the one parameter family of solutions given by Theorem 13 is unique.

Theorem 14 is an exact analogue of Theorem 5 of reference [6], and is demonstrated by the same method. Note that the proof in [6] is restricted to two dimensions because the Harnack inequality used there was proved only for two variables; since in the present case we have a Harnack inequality irrespective of dimension, it is clear that the argument carries over intact.

**THEOREM 15.** Let $u$ be a continuous solution of (97) in the set $D - \{0\}$, where $D$ is a domain in $\Omega$. Suppose that $u = O(r^{2-n})$ or $u = O(\log 1/r)$, depending on whether $n>2$ or $n=2$. Then either $u$ has a removable singularity at 0, or else (possibly after multiplication by $-1$)

$$
u \approx \begin{cases} r^{2-n}, & n > 2, \\ \log 1/r, & n = 2, \end{cases} \qquad (98)
$$

in the neighborhood of the origin.

*Proof.* For a suitably large constant $A$ we have

$$
u + AG > 0
$$

in the neighborhood of the origin, where $G$ is some particular solution satisfying

(1) As we have remarked in the introduction, these special results are due originally to Royden and to Littman, Stampacchia, and Weinberger.

---

300

JAMES SERRIN

$G \approx r^{2-n}$ or $G \approx \log 1/r$ (such a function exists by Theorem 13). The function $u + AG$ is therefore a positive solution of (97) in some neighborhood of the origin. Consequently by Theorem 12 we have $u + AG \approx r^{2-n}$ or $\log 1/r$, and the required conclusion follows at once.

The above argument is essentially due to Gevrey, who proved a similar result for linear equations of the form $a_{ij}u,_{ij} + b_i u,_{i} + cu = 0$ with certain smoothness conditions placed on the coefficients $a_{ij}$.

*Remarks.* For the Laplace equation the result of Theorem 15 can be considerably improved. In fact in this case the hypothesis can be weakened to read

$$
u = o(r^{1-n}),
$$

without affecting the conclusion. For the general class of equations under consideration here, however, there is no immediately analogous result—that is, *the order of growth $O(r^{2-n})$ or $O(\log 1/r)$ is best possible in Theorem 15.*

Indeed, consider equation (97) with

$$
a_{ij} = \delta_{ij} + (a-1) x_i x_j / r^2, \quad (99)
$$

where $a$ is a constant greater than one (cf. [6], p. 336). One easily verifies that

$$
\xi^2 \le a_{ij} \xi_i \xi_j \le a \xi^2,
$$

so that (99) is an allowable set of coefficients. We consider solutions of the form

$$
u = H(x) f(r), \quad (100)
$$

where $H$ is a harmonic polynomial of degree $m$, and $r = |x|$. After a straightforward calculation we find that (100) satisfies (97), (99) provided $f = r^{2-m-n-\varepsilon}$ and $a$ and $\varepsilon$ are related by

$$
a = \frac{m(m+n-2)}{\varepsilon(\varepsilon+n-2)}, \quad (0 < \varepsilon < m).
$$

The solution (100) is therefore $O(r^{2-n-\varepsilon})$, that is, *there exist solutions of linear equations of the form (97) which are $O(r^{2-n-\varepsilon})$ for any preassigned $\varepsilon > 0$ and yet are not $\approx r^{2-n}$.*