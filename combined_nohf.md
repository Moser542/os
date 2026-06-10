1. Introduction

In 1844, in a short note [8] in the Comptes Rendus de l'Académie des Sciences, Paris, Augustin Cauchy published the first statement of what is now known as the Liouville theorem for bounded analytic functions:

*Any bounded entire function of a single complex variable must be constant.*

This classical theorem generalizes at once to real harmonic functions on $\mathbf{R}^n$ which are bounded only on one side:

*Let $n \ge 2$ and let $u$ be a real harmonic function on $\mathbf{R}^n$, bounded either from above or below. Then $u$ must be constant.*

When the dimension $n=2$, one can even consider superharmonic functions (e.g., satisfying the inequality $\Delta u \le 0$):

Let $u$ be a real superharmonic function on $\mathbf{R}^2$, bounded from below. Then $u$ is constant.

Proofs can be found for example in [21, pp. 111 and 130]. More recently, the Liouville theorem was further generalized to solutions of quasilinear elliptic equations (Serrin [25]):

Let $u$ be an entire solution of the equation

$$
\Delta u + f(u, \nabla u) = 0 \quad \text{in } \mathbf{R}^n.
$$

Suppose that $\partial f/\partial u \le 0$ and that both $u$ and $\nabla u$ are bounded. Then $u$ must be constant.

Under further assumptions, it can be shown [20], [26] that $\nabla u$ is necessarily bounded on all $\mathbf{R}^n$. Using this fact, one gets a standard Liouville theorem for bounded solutions. See also Caffarelli, Garofalo and Segala [6] and references therein.

Still other Liouville theorems have been obtained for non-negative solutions of the Lane-Emden equation

$$
\Delta u + u^{p-1} = 0, \quad p > 1 \qquad (1.1)
$$

(note that the previous result does not cover (1.1), since $u^{p-1}$ is increasing for $u>0$). We first state a beautiful and deep result of Gidas and Spruck.

THEOREM 1 (Gidas and Spruck [12]). Assume $n>2$. Let $u$ be a non-negative solution of (1.1) in $\mathbf{R}^n$ with $2 \le p < 2n/(n-2)$ (Sobolev number for $\mathbf{R}^n$). Then $u \equiv 0$.

A striking fact about this result is that it fails for any $p \ge 2n/(n-2)$. For example, when $p=2n/(n-2)$, we have the Emden solution

$$
u(x) = \left( C \frac{\kappa}{\kappa^2 + |x|^2} \right)^{(n-2)/2} \qquad (1.2)
$$

where $\kappa > 0$ is a parameter and $C = C(n) = \sqrt{n(n-2)}$. This solution also shows that when $n>2$ there are non-constant bounded superharmonic functions.

A second marvelous result concerning equation (1.1) is due to Bidaut-Veron.

THEOREM 2 (Bidaut-Veron [3]). Let $n \ge 2$ and let $u$ be a non-negative solution of (1.1) on an exterior domain. Suppose $2 < p < 2(n-1)/(n-2)$ ($=\infty$ if $n=2$). Then $u \equiv 0$. (1)

Again this result fails for any $p > 2(n-1)/(n-2)$. For example, for $p$ in this range we have the singular solution

$$
u(x) = C|x|^{-2/(p-2)}, \quad C = (p-2)^{-2/(p-2)} \left[ 2(n-2) \left( p - \frac{2(n-1)}{n-2} \right) \right]^{1/(p-2)}, \qquad (1.3)
$$

(1) In [3] this result was actually given for the more general equation $\Delta_m u + u^{p-1} = 0$, under related restrictions on the parameters $m, p$; see also Theorem I below of Bidaut-Veron and Pohozaev.

The first author to observe the importance of the exponent $p=2(n-1)/(n-2)$ is R. H. Fowler, this exponent being equivalent to the special value $\sigma=-2$ in Fowler's work. Cf. *Quart. J. Pure Appl. Math.*, 45 (1914), 289-350, and *Quart. J. Math. Oxford Ser.*, 2 (1931), 259-288.

defined in the exterior domain $\mathbf{R}^n \setminus \{0\}$.

The purpose of the present paper is to extend the above considerations to non-homogeneous degenerate elliptic equations of the form

$$
\Delta_m u + f(u) = 0, \quad u \ge 0, x \in \Omega, \qquad (1.4)
$$

where $\Omega$ is a domain (connected open set) in $\mathbf{R}^n$, $n \ge 2$, and

$$
\Delta_m u = \operatorname{div}(|\nabla u|^{m-2} \nabla u)
$$

is the well-known $m$-Laplace operator, $m > 1$. Equation (1.4) arises in many nonlinear phenomena, for instance, in the theory of quasi-regular and quasi-conformal mappings, see [17], [22], [29], and in mathematical modeling of non-Newtonian fluids, see [2], [9], [14], [15] for a discussion of the physical background. The equation also has a large and well-known theoretical literature, some of which will be particularly discussed below.

A function $u \in C^1(\Omega)$ is said to be a *weak solution* of (1.4) if

$$
- \int |\nabla u|^{m-2} \nabla u \cdot \nabla \phi + \int f(u) \phi = 0 \quad \text{for all } \phi \in C_0^\infty(\Omega). \qquad (1.5)
$$

We shall assume throughout the paper that $f(u)$ is a non-negative function in $C([0, \infty)) \cap C^1((0, \infty))$. Then a strong maximum principle holds for equation (1.4), in the sense that all non-negative non-trivial solutions must be strictly positive, see Lemma 2.1 below. In what follows we shall always be concerned with weak solutions, without further mention.⁽²⁾

The first main goal of the paper is to consider Liouville-type results for the degenerate equation (1.4), and also for continuously differentiable (or even $W_{\text{loc}}^{1,m}(\Omega) \cap C(\Omega)$) weak solutions of the differential inequalities

$$
-\Delta_m u \ge u^{p-1}, \quad u \ge 0, x \in \Omega, \qquad (1.6)
$$

with $p > 1$, and

$$
-\Delta_m u \ge 0, \quad u \ge 0, x \in \Omega. \qquad (1.6')
$$

Our second principal purpose is to derive universal a priori estimates for solutions of (1.4) and (1.6), including, in particular, the generalized Lane-Emden equation $\Delta_m u + u^{p-1} = 0$, that is, (1.4) with $f(u) = u^{p-1}$. By using the word “universal” here, we mean that our bounds are not only independent of any given solution under consideration but also do not require, or assume, any boundary conditions whatsoever. We are not aware of any previous results of this type for equation (1.4) with $f(u) \ge 0$, with the exception of the a priori estimates obtained by Gidas and Spruck for solutions of (1.1) in the neighborhood of an isolated singularity, and a result of Dancer for the same case.

(²) It is possible to use an even weaker definition for weak solutions. That is, one needs to require only that $u \in W_{\text{loc}}^{1,m}(\Omega) \cap L_{\text{loc}}^{\infty}(\Omega)$. By classical results, however, the two definitions are equivalent (see the references in §8 below).

THEOREM 3 (Dancer [34, Lemma 1]). Assume $n>2$ and $2<p<2n/(n-2)$. Let $u$ be a non-negative solution of the canonical equation (1.1) in a domain $\Omega \neq \mathbf{R}^n$. Then for every $x \in \Omega$ we have

$$
u(x) \le C(n, p)[\mathrm{dist}(x, \partial\Omega)]^{-2/(p-2)}.
$$

In particular, $u$ is bounded on any compact subset $\Omega'$ of $\Omega$, the bound being independent of the solution.

The range $2<p<2n/(n-2)$ and the exponent $2/(p-2)$ are both optimal in view of the special solutions (1.2) and (1.3).

The relevance of a universal boundedness theorem can be immediately illustrated by Theorem 3. Indeed, Theorem 1 is a direct corollary of Theorem 3, since $\mathrm{dist}(x, \partial\Omega)$ can be chosen arbitrarily large when the solution is defined on all $\mathbf{R}^n$. The relation between Theorem 3 and the Liouville Theorem 1 can also be considered in a deeper way. That is, they both provide *upper bounds* for non-negative solutions, with Theorem 1 being the extreme case where the domain is all of $\mathbf{R}^n$ and the upper bound becomes zero, the smallest value it could have. In still other terms, Theorem 3 provides a continuous embedding of the Liouville theorem for (1.1) in a family of results for an expanding sequence of *bounded* domains. Theorem 3 is a special case of Theorem IV below, which in turn is contained in Theorems 4.1 and 4.2.

Returning to the general equation (1.4), when $n>m$ we define

$$
m_* = \frac{m(n-1)}{n-m} > 0,
$$

the *lower critical exponent*, and

$$
m^* = \frac{nm}{n-m} > 0,
$$

the *critical exponent for Sobolev embedding*. We say that $f$ is *subcritical* if $n>m$ and there exists a number $1<\alpha<m^*$ such that

$$
f(u) \ge 0, \quad (\alpha-1)f(u) - uf'(u) \ge 0, \quad \text{for } u > 0. \qquad (1.7)
$$

Note in particular that the function $f(u)=u^{p-1}$ is subcritical when $1<p<m^*$. A domain $\Omega$ is called *exterior* if $\Omega \supset \{|x|>R>0\}$ for some $R>0$. An important recent Liouville-type result is the following

THEOREM I (Bidaut-Veron and Pohozaev [4, Theorems 3.3 (iii) and 3.4 (ii)]). Let $\Omega$ be an exterior domain. Then the differential inequality (1.6) has only the trivial solution $u=0$, provided $p \in (1, m_*]$ when $n>m$, or $p \in (1, \infty)$ when $n=m$.

The result also applies when $n<m$, as follows.

THEOREM I'. Let $\Omega$ be an exterior domain and let $n<m$. Then the differential inequality (1.6) has only the trivial solution $u \equiv 0$, provided $p \in (1, \infty)$.

When the domain $\Omega$ is the entire space $\mathbf{R}^n$, rather than simply an exterior set, Theorem I can be extended to a larger range of exponents. The full result is as follows.

THEOREM II. Let $\Omega=\mathbf{R}^n$. Then the following conclusions hold.

(a) Let $u(x)$ be a non-negative solution of $\Delta_m u=0$ (if $n>m$), or of $\Delta_m u \le 0$ (if $n \le m$). Then $u$ is constant.

(b) Suppose either $n=2$ and $m > \frac{1}{4}(1+\sqrt{17})$, or $n \in [3, 2m)$, $m > \frac{3}{2}$. Assume that $f$ is subcritical. Then every solution of (1.4) is constant.

(c) Assume that $f$ is subcritical and that there exists $p>m$ such that

$$
f(u) \ge u^{p-1} \qquad (1.8)
$$

for sufficiently large $u$. Then (1.4) has only the trivial solution $u \equiv 0$. The same conclusion holds if $p \in (1, m]$, provided $\alpha \le m$ in (1.7).

(d) If $n>m$ and $p \in (1, m_*]$, then the differential inequality (1.6) has only the trivial solution $u \equiv 0$.

Remarks. When $n \le m$ the inequality $-\Delta_m u \ge 0$ has the (bounded) positive non-constant solution $u=1-1/|x|$ on the exterior domain $\{|x|>1\}$, which indicates the necessity of considering (a) on the entire space $\mathbf{R}^n$. Notice also that the result of (b), when it is applicable, is stronger than (c), and that (d) overlaps with (b) and (c), both cases being of independent interest.

Case (d) is of course an immediate consequence of Theorem I; it was first proved by Mitidieri and Pokhozhaev [18].

The special case $m=2$ of Theorem II (Laplace operator) is important enough to be stated as a separate result, especially in order to compare our results with those of Gidas and Spruck. We consider particularly the cases (b), (c), since for the Laplacian case (a) is classical while (d) is a special case of the Mitidieri-Pokhozhaev theorem.

THEOREM 4. Let $m=2$ and $\Omega=\mathbf{R}^n$. Then the following conclusions hold.

(b) Let $n=3$ and assume that $f$ is subcritical. Then every solution of (1.4) is constant.

(c) Suppose $n \ge 4$. Assume that $f$ is subcritical and that (1.8) holds with $p>2$. Then (1.4) has only the trivial solution $u \equiv 0$. The same conclusion holds if $p \in (1, 2]$, provided $\alpha \le 2$ in (1.7).

Case (b) is due to Gidas and Spruck [12] under the additional assumption $f(u)>0$ for $u>0$, the conclusion then of course being that $u \equiv 0$. The first statement of case (c) is

similarly due to Gidas and Spruck, see [12, Theorem 6.1]. The second statement of case (c) is new.

Gidas and Spruck have conjectured (in view of case (b)) that the extra condition (1.8) in case (c) may be unnecessary. We are inclined to doubt this, since even in the more general case of Theorem II, case (b), the required condition is $n<2m$, that is, $n<4$ when $m=2$. If, however, one treats solutions which are also bounded above, then their conjecture is essentially true.

THEOREM III. Let $\Omega=\mathbf{R}^n$ with $n>m$. Assume that $f$ is subcritical and that $f(u)>0$ for all $u>0$. Then every bounded solution of (1.4) is trivial.

Theorems I-III are sharp, in the sense of the following corollaries.⁽³⁾

COROLLARY I. Let $\Omega$ be an exterior domain. Then the differential inequality (1.6) has a non-trivial solution if and only if $m \in (1, n)$ and $p > m_*$.

The "only if" part follows from Theorem I. On the other hand, for $\Omega=\mathbf{R}^n \setminus \{0\}$, one readily verifies when $p > m_*$ that (1.6) has a positive singular solution $C'|x|^{-m/(p-m)}$, where

$$
C' = \left( \frac{m}{p-m} \right)^{m/(p-m)} \left[ \frac{n-m}{m} (p-m_*) \right]^{1/(p-m)},
$$

this being the exact analogue of the solution (1.3) when $m=2$.

COROLLARY II. Let $\Omega$ be the entire space $\mathbf{R}^n$. Then:

(i) The inequality $-\Delta_m u \ge 0$ has a non-constant positive solution in $\mathbf{R}^n$ if and only if $n > m$.

(ii) Assume $n > m$. Then the generalized Lane-Emden equation $\Delta_m u + u^{p-1} = 0$ has a positive solution in $\mathbf{R}^n$ if and only if $p \ge m^*$.

(iii) Assume $n > m$. Then the differential inequality $-\Delta_m u \ge u^{p-1}$ has a positive solution in $\mathbf{R}^n$ if and only if $p > m_*$.

The "only if" part of (i) and of (iii) are an immediate consequence of Theorem II (a) and II (d), respectively. Similarly, (b), (c) of Theorem II imply that when $n > m$ and $p < m^*$ all solutions of the generalized Lane-Emden equation in $\mathbf{R}^n$ must be constant, and hence zero, which is the "only if" part of (ii).

(³) Some of the above Liouville theorems have previously been established in [19] for radially symmetric solutions. If one knew a priori that solutions of (1.4) when $\Omega=\mathbf{R}^n$ were necessarily radially symmetric, then of course Theorem II would follow at once. Such an approach, however, seems an unlikely possibility in any kind of generality; moreover when $p \ge m^*$ it is not even true that all solutions are radially symmetric (see [32]).

On the other hand, direct calculation shows that the inequality $-\Delta_m u \ge 0$ has a (bounded) positive non-constant solution in $\mathbf{R}^n$ of the form

$$
C(1+|x|^{m/(m-1)})^{-(n-m)/m},
$$

which gives the "if" part for (i). For (ii), existence is a special case of Theorem 6.4 of [19].

Finally, by direct calculation, the differential inequality (1.6) has a (bounded) positive solution in $\mathbf{R}^n$ of the form (see Remark 4 in Mitidieri and Pokhozhaev [18])

$$
u(x) = C'(\varkappa + |x|^{m/(m-1)})^{-(m-1)/(p-m)},
$$

where $C'$ is the coefficient given in the proof of Corollary I. (In fact, one finds explicitly that $-\Delta_m u = u^{p-1} + \varkappa c u^{(mp-2m+1)/(m-1)}$ for an appropriate constant $c=c(n, m, p)>0$.) This yields existence for (iii), and the proof is complete.

COROLLARY III. Let $\Omega=\mathbf{R}^n$. Assume $n>m$. Then the generalized Lane-Emden equation has a bounded positive solution on $\Omega$ if and only if $p \ge m^*$, and (1.6) has a bounded positive solution if and only if $p > m_*$.

This is a special case of Corollary II. Two model nonlinearities may be noticed here,

$$
f(u) = u^{p-1} + u^{s-1}, \quad f(u) = \frac{u^{p-1}}{1+u^t},
$$

where $1<s \le p < m^*$ and $t>0$. Both nonlinearities are subcritical as one easily checks. For the first, Theorem II shows that the only solution of (1.4) on $\mathbf{R}^n$ is $u \equiv 0$. For the second, Theorem II (b) applies, but not Theorem II (c). Nevertheless, since $f(u)>0$ for $u>0$, by Theorem III the only bounded solution of (1.4) for this nonlinearity on $\mathbf{R}^n$ is again $u \equiv 0$.

Turning to the second principal goal of the paper, we have the following universal *a priori* estimate (see §5 for other related results).

THEOREM IV. Let $\Omega \subset \mathbf{R}^n$ and assume $n>m$. Then the following conclusions hold.

(a) Let $u$ be a non-negative weak solution of the two-sided differential inequality

$$
u^{p-1} - u^{m-1} \le -\Delta_m u \le \Lambda(u^{p-1} + 1), \quad x \in \Omega, \quad (1.9)
$$

where $\Lambda>1$ and $m<p<m_*$. Then there exists a constant $C=C(n, m, p, \Lambda)>0$ such that for all $x \in \Omega$

$$
u(x) \le CR^{-m/(p-m)}, \quad (1.10)
$$

where $R=\min(1, \text{dist}(x, \partial\Omega))$. If the additive terms $u^{m-1}$ and $1$ are dropped from (1.9), then (1.10) is satisfied with $R=\text{dist}(x, \partial\Omega)$.

(b) Let $u$ be a solution of (1.4). Suppose that $f$ is subcritical and that, for some $\Lambda>1$ and $p>m$, it satisfies the power-like condition

$$
u^{p-1} \le f(u) \le \Lambda(u^{p-1}+1). \qquad (1.11)
$$

Then (1.10) holds with $C=C(n, m, p, \alpha, \Lambda)>0$ and $R=\min(1, \text{dist}(x, \partial\Omega))$. If, instead of (1.11),

$$
u^{p-1} \le f(u) \le \Lambda u^{p-1}, \qquad (1.12)
$$

then (1.10) holds with $R=\text{dist}(x, \partial\Omega)$.

The inequality (1.10) yields absolute bounds for non-negative solutions on any compact subdomain of their domain $\Omega$ of definition, the constant $C$ being independent of any particular solution under consideration. We note also that the range $m<p<m_*$ for case (a) and $m<p<m^*$ for case (b), and the exponent $m/(p-m)$ in (1.10), are each optimal; see the discussion in §5.

It is interesting to ask about the size of the singular set of a solution $u$ which is defined over some domain $\Omega$. Certainly it cannot consist of the entire boundary of $\Omega$, since $u$ is superharmonic. On the other hand, can one estimate in some way the Hausdorff dimension or the Hausdorff measure of this set? Here, a tentative conjecture is that the Hausdorff dimension of a singular set on $\partial\Omega$ must be less than or equal to $n-m(p-1)/(p-m)$; see Mazzeo and Pacard [16] for the case $m=2$, and also Veron [31, pp. 242-254].

*Remark.* In (1.9), one might wish to study the apparently more general left-hand side, $\lambda u^{p-1} - \mu u^{m-1}$. The constants $\lambda$ and $\mu$ can however be reduced to 1 by simple rescaling; thus the special form of the left-hand side of (1.9) involves no loss of generality. The same remark obviously applies to later formulations of the principal conditions on $f$.

Theorem IV has useful implications for the asymptotic behavior of solutions near isolated singularities, see the corollary below.

COROLLARY IV. Let $u$ be a solution of (1.4), where $f$ is subcritical. Then:

(i) Suppose that (1.11) holds, and let $\Omega=B_1(0)\setminus\{0\}$. Then there exists a constant $C=C(n, m, p, \Lambda)>0$ such that

$$
u(x) \le C|x|^{-m/(p-m)} \qquad (1.13)
$$

for all $x \in \Omega$.

(ii) Suppose that (1.12) is satisfied, and let $\Omega$ be an exterior domain. Then (1.13) holds for all sufficiently large $|x|$. (Note that if $p \le m_*$ then Theorem I gives a stronger result.)

The asymptotic behavior (1.13) near an isolated singularity (and further extensions of this) were established for the Laplace operator ($m=2$) by Gidas and Spruck [12] and by Bidaut-Veron and Veron [5].

Theorem IV also implies the following non-existence theorem.

COROLLARY IV'. Let the hypotheses of Theorem IV (a), or (b), hold. Then the Dirichlet problem for (1.9), or (1.4), with data $u \ge M$ on $\partial\Omega$ has no solution if $M$ is sufficiently large.

*Proof.* The result follows at once from (1.10) together with the fact that solutions are $m$-superharmonic and so satisfy $u \ge M$ in $\Omega$.

The a priori estimates given in Theorem IV are obtained from the following Harnack-type theorem, itself of independent interest, which will be proved in §4; see Theorems 4.1 and 4.2.

THEOREM V. Let $R$ and $x_0$ be such that $B_R \equiv B_R(x_0) \subset B_{2R}(x_0) \subset \Omega$, and assume $n>m$. Then we have the following conclusions.

(a) Let $u$ be a non-negative weak solution of the differential inequality (1.9). Then for every $R_0>0$ there exists $C=C(n, m, p, \Lambda, R_0)>0$ such that

$$
\sup_{B_R} u \le C \inf_{B_R} u \quad (1.14)
$$

provided $R \le R_0$.

If the terms $u^{m-1}$ and $1$ are dropped in (1.9), then (1.14) holds with $C=C(n, m, p, \Lambda)$ and with no further restriction on $R$.

(b) Let $u$ be a solution of (1.4), where $f$ is subcritical. Suppose either $n=2$ and $m > \frac{1}{4}(1+\sqrt{17})$, or $n \in [3, 2m)$, $m > \frac{3}{2}$. Then (1.14) holds with $C=C(n, m, \alpha)>0$.

(c) Let $u$ be a solution of (1.4), where $f$ is subcritical, and suppose that (1.12) is satisfied for some $p>m$. Then (1.14) holds with $C=C(n, m, p, \alpha, \Lambda)$.

The case $n \le m$ can also be treated, see Theorem 4.3.

Some remarks on the proof methods are worthwhile. First, Theorems I', II (a) and IV (a) are relatively elementary, with the exception that the last two cases require an application of the classical Harnack inequality for quasilinear equations (Serrin [23]).

The proofs for Theorem II (b), (c), Theorem IV (b) and Theorem V (b), (c) additionally rely on an important integral inequality for solutions of equation (1.4), see Proposition 6.1. For the Laplace case $m=2$ this result is (essentially) due to Gidas and Spruck [12]. When $m \ge 2$, Proposition 6.1 is proved by direct calculation, using as a key element an unusual nonlinear vector field $\omega$, see (6.10), and also, at one point, a delicate interchange of order of differentiation. (For $m=2$ the interchange is elementary because

of the smoothness of solutions of (1.4) in this case; the loss of $C^2$ regularity is at the heart of the difficulty otherwise.)

When $1<m<2$ the proof of the inequality is still more technical, the difficulty again being due to the degeneracy of the $m$-Laplace operator and the loss of smoothness of solutions. As part of the derivation, we have been led to an improved regularity result for solutions of (1.4), extending the “classical” theory of [10], etc. This result is of independent interest and is, to the best of the authors’ knowledge, new. It is worth remarking as well that, when $1<m<2$, it appears to be impossible to obtain a strict analogue of the Gidas-Spruck identity for the case $m=2$. Rather, we employ related integral inequalities, which, fortunately, seem at least as useful as the identity itself.

The paper is organized as follows. Chapter I contains the proofs of Theorems I–V and of several further results of a more special nature; see the Table of Contents for the specific content of these sections. Chapter II is devoted to the proof of Proposition 6.1, that is, the general integral inequality (6.1). In particular, in §§ 6 and 7 we prove the inequality respectively for the case $m \ge 2$ and for the more delicate range $1<m<2$. Finally § 8 contains our regularity results for solutions of (1.4); see the main Proposition 8.1.

It may seem paradoxical that so much effort must be devoted to the integral inequality for (1.4), in view of the fact that it is applied only at one point in Chapter I. On the other hand, on this application alone stands or falls the entire structure for functions $f(u)$ whose growth rate in the variable $u$ exceeds the power $m_*-1$ ($=n(m-1)/(n-m)$); for the case of the Laplace operator, in particular, a growth rate exceeding the “classical” power $n/(n-2)$. This being the case, the further effort seems more than worthwhile, even if it is lengthy and difficult. Moreover, this aspect of the theory makes abundantly clear the great difference between the ranges $(1, m_*)$ and $(m_*, m^*)$ of the variable $p$ in the equation $\Delta_m u + u^{p-1} = 0$.

It almost goes without saying that much of the work in the paper can be expected to carry over to more general operators and to nonlinearities $f$ depending on $x$ and $\nabla u$ as well as on $u$.

The second author wishes to thank E. DiBenedetto and D. Andreucci for useful discussions at the beginning of this work. The authors also wish to thank the referee for carefully reading the manuscript and, in particular, for pointing out to us the importance of reference [16].

Chapter I

2. Liouville theorems I

In this section, we prove the Liouville Theorem I', and also, for completeness, Theorem I. Our proof of the latter result was obtained independently of the work of Bidaut-Veron and Pohozaev, and in some respects depends on different ideas.

The letter $C$ will be used throughout to denote a generic positive constant, which may vary from line to line and only depends on arguments inside the parentheses or which are otherwise clear from the context.

We begin with a series of lemmas. The first is the well-known strong maximum principle.

LEMMA 2.1. Let $u$ be a weak solution of (1.6'). Then either $u \equiv 0$ or $u > 0$ on $\Omega$.

Lemma 2.1 is a consequence of the weak Harnack inequality (see Lemma 3.2 below).

LEMMA 2.2. Let $u$ and $v$ be continuous functions in the Sobolev space $W_{\text{loc}}^{1,m}(\Omega)$ which satisfy the distribution inequality

$$
\Delta_m u - \Delta_m v \le 0 \qquad (2.1)
$$

in a domain $\Omega$ of $\mathbf{R}^n$. Suppose that $u \ge v$ on $\partial\Omega$, in the sense that the set $\{u-v+\varepsilon \le 0\}$ has compact support in $\Omega$ for every $\varepsilon > 0$. Then $u \ge v$ in $\Omega$.

Lemma 2.2 is a well-known comparison lemma; its proof can be omitted.

LEMMA 2.3. Suppose $\{|x|>R>0\} \subset \Omega$. Let $u$ be a positive weak solution of the inequality

$$
\Delta_m u \le 0, \quad x \in \Omega. \qquad (2.2)
$$

Then there exists a constant $C=C(m, n, u, R) > 0$ such that

$$
u(x) \ge C|x|^{-(n-m)/(m-1)} \qquad (2.3)
$$

provided $n > m$, while

$$
\liminf_{x \to \infty} u(x) > 0 \qquad (2.4)
$$

if $n \le m$.

Proof. First assume $n > m$. Define

$$
K = R^{(n-m)/(m-1)} \min_{|x|=2R} u(x) > 0
$$

and

$$
v(x) = K|x|^{-(n-m)/(m-1)}.
$$

Then $v$ is a fundamental solution of $-\Delta_m v=0$, so by applying Lemma 2.2 in the domain $|x|>2R$ we get (2.3).

To prove (2.4), let $S>R$ and define

$$
v(x) = \frac{\ln(4S/|x|)}{\ln(2S/R)}
$$

for $x$ in $\Omega$. Observe that

$$
-\operatorname{div}(|\nabla v|^{m-2}\nabla v) \le 0, \quad x \in \Omega,
$$

while also $v=1$ when $|x|=2R$; $v=\frac{1}{2}$ when $|x|=2(2RS)^{1/2}$; and $|v|=0$ when $|x|=4S$.

Since $u>0$ in $\Omega$, we have $\varepsilon \equiv \inf_{|x|=2R} u>0$. Hence by the weak comparison principle, we get $u \ge \varepsilon v$ for $2R<|x|<4S$. But then $u(x) \ge \frac{1}{2}\varepsilon$ for $|x| \le 2(2RS)^{1/2}$. Letting $S$ tend to infinity now yields $\liminf_{x \to \infty} u(x) \ge \frac{1}{2}\varepsilon > 0$, as required.

We next give an integral estimate for solutions of (1.6) in a domain $\Omega$ of $\mathbf{R}^n$. Here and in the sequel, by $B_R=B_R(x_0)$ we shall mean a ball of radius $R$ and center $x_0$, such that the corresponding ball $B_{2R}(x_0)$ of radius $2R$ is contained in the domain $\Omega$.

LEMMA 2.4. Let $u$ be a weak solution of (1.6) in $\Omega$ for some $p>m$ and let $R>0$. Then for all $\gamma \in (0, p-1)$ there exists a constant $C=C(n, m, p, \gamma)>0$ such that

$$
\int_{B_R} u^\gamma \le CR^{n-m\gamma/r}, \qquad (2.5)
$$

where $r=p-m>0$. Similarly, for all $\mu \in (0, m(p-1)/p)$ there exists $C(n, m, p, \mu)>0$ such that

$$
\int_{B_R} |\nabla u|^\mu \le CR^{n-p\mu/r}. \qquad (2.6)
$$

Remark. The inequality (2.5) is due (in a slightly different form) to Bidaut-Veron and Pohozaev [4, Lemma 2.5]; see also Mitidieri and Pokhozhaev [18]. We include the proof for completeness and also for later reference.

Proof. It can be assumed without loss of generality that $u>0$ in $\Omega$, since otherwise $u \equiv 0$ by the strong maximum principle, and (2.5) and (2.6) are trivially satisfied.

Now let $\xi$ be a radially symmetric $C^2$ cut-off function on the double unit ball $B_2(0)$, namely,

(1) $\xi \equiv 1$ for $|x|<1$; $0 \le \xi \le 1$ for $|x| \ge 1$,

(2) $\xi$ has compact support in $B_2(0)$,

and, without loss of generality,

(3) $|\nabla\xi| \le 2$, $|\nabla^2\xi| \le c$, where $c$ is a suitable constant, e.g., $c=4\sqrt{n}$ suffices.

For $k>m$ to be determined later and $d=p-1-\gamma>0$, take $\phi=[\xi(|x-x_0|/R)]^k u^{-d}>0$ as a test function in the weak form of (1.6). (Test functions involving negative powers of the solution have been classically used at least since the work of Moser in the 1950's.) This gives at once

$$
d \int \xi^k u^{\gamma-p} |\nabla u|^m + \int \xi^k u^{\gamma} \le \int u^{-d} \mathbf{u} \cdot \nabla \xi^k, \quad (2.7)
$$

where $\mathbf{u}=|\nabla u|^{m-2}\nabla u$. Write

$$
|\nabla \xi^k| = k \xi^{k-1} |\nabla \xi| \le \xi^k (1 \cdot 2k/R\xi)
$$

and $1=u^{-(m-1)/m} \cdot u^{(m-1)/m}$. Then by Young's inequality with the exponent pair $m/(m-1)$, $m$ (and the usual trick$^{(4)}$) one finds

$$
\left| \int u^{-d} \mathbf{u} \cdot \nabla \xi^k \right| \le \frac{d}{2} \int \xi^k u^{\gamma-p} |\nabla u|^m + CR^{-m} \int \xi^{k-m} u^{\gamma-r},
$$

where $r=p-m>0$. In turn, by (2.7),

$$
\frac{d}{2} \int \xi^k u^{\gamma-p} |\nabla u|^m + \int \xi^k u^{\gamma} \le CR^{-m} \int \xi^{k-m} u^{\gamma-r}, \quad (2.8)
$$

the constant $C$ depending on $m, k, p, \gamma$.

We can now prove (2.5). First suppose $\gamma>r$. Letting

$$
k = m \frac{\gamma}{r} > m
$$

and applying the Young inequality to the right side of (2.8), using the exponent pair

$$
\frac{\gamma}{\gamma-r}, \quad \frac{\gamma}{r},
$$

we obtain (again with the usual trick)

$$
CR^{-m} \int \xi^{k-m} u^{\gamma-r} \le \frac{1}{2} \int \xi^k u^{\gamma} + C(m, p, \gamma) R^{-m\gamma/r} \int \xi^0.
$$

(4) Namely, to use a small coefficient multiplying one of the terms of the inequality at the expense of a larger coefficient for the other, that is,

$$
ab \le \varepsilon a^q + \frac{1}{\varepsilon^{1/(q-1)}} b^{q/(q-1)}
$$

for any $a, b>0$ and exponents $q, q/(q-1)>1$.

Consequently, (2.8) yields

$$
\frac{d}{2} \int \xi^k u^{\gamma-p} |\nabla u|^m + \frac{1}{2} \int \xi^k u^\gamma \le C(n, m, p, \gamma) R^{n-m\gamma/r}. \quad (2.9)
$$

Condition (2.5) now follows at once. The special case $\gamma=r$, on the other hand, is immediately obvious from (2.8).

Finally, if $\gamma<r$ we apply Hölder's inequality with exponents $r/\gamma$ and $r/(r-\gamma)$ to obtain

$$
\int_{B_R} u^\gamma \le C \left( \int_{B_R} u^r \right)^{\gamma/r} R^{n(1-\gamma/r)}.
$$

Since (2.5) is already known to hold for the exponent $\gamma=r$, this gives the required conclusion for all $\gamma$.

To get (2.6), note that $\mu<m$, and write

$$
\int |\nabla u|^\mu \le \left( \int u^{\gamma-p} |\nabla u|^m \right)^{\mu/m} \left( \int u^{\bar{\gamma}} \right)^{1-\mu/m},
$$

where $\gamma \in (0, p-1)$ and $\bar{\gamma}=(p-\gamma)\mu/(m-\mu)$. Since $\mu \in (0, m(p-1)/p)$, we have $\bar{\gamma} \in (0, p-1)$ provided $\gamma$ is suitably near $p-1$. Hence one can apply (2.5) to the second integral on the right. On the other hand, by (2.9) the first integral is bounded by $CR^{n-m\gamma/r}$. Combining these estimates and simplifying then gives (2.6). This completes the proof of the lemma.

*Remark.* For $1<p<m_*$ one can give an improved version of (2.5), see Lemma 4.1.

Now we are ready to prove the first Liouville theorem.

*Proof of Theorem I.* Let $u$ be a positive weak solution of (1.6), where $\Omega$ is an exterior domain containing $\{|x|>R\}$. Take a sequence of points $\{x^j\} \subset \mathbf{R}^n$ such that $|x^j|>3R$ and $x^j \to \infty$.

Consider first the case $n \le m, p > m$. In (2.5), take $\gamma=r=p-m<p-1$ to obtain

$$
\int_B u^r \le C |x^j|^{n-m}, \quad j=1, 2, \dots,
$$

where $B=B_{|x^j|/4}(x^j)$ (note that $B_{|x^j|/2}(x^j) \subset \Omega$) and $C=C(n, m, p)$. Then

$$
\min_B u^r \le \frac{1}{|B|} \int_B u^r \le C |x^j|^{-m}. \quad (2.10)
$$

But this contradicts (2.4) as $x^j \to \infty$. Hence there are no everywhere positive solutions $u$, so from the strong maximum principle we get $u \equiv 0$, as required.

Next suppose $n>m$ and $p \in (m, m_*)$. Let $u$ be a positive weak solution of (1.6). As in the previous case the inequality (2.10) is valid. Consequently there exists $y^j \in B$ such that

$$
u^r(y^j) = \min_B u^r \le C|x^j|^{-m} \le (\frac{5}{4})^m C|y^j|^{-m}
$$

(since $\frac{3}{4}|x^j| < |y^j| < \frac{5}{4}|x^j|$). On the other hand, recalling that $n>m$ and using (2.3), we have

$$
u(y^j) \ge C|y^j|^{-(n-m)/(m-1)}
$$

for some $C>0$. This yields an immediate contradiction, since $y^j \to \infty$ and

$$
\frac{m}{r} > \frac{n-m}{m-1} \quad \text{when } p < m_*.
$$

It now follows as before that $u \equiv 0$, as required.

For the case $n>m$, $p=m_*$, we need an auxiliary lemma.

LEMMA 2.5. Let $u$ be a weak solution of (1.6) on $\Omega \supset \{|x| > R_0 > 0\}$, with $p > m$. Also let $\mu \in (0, m(p-1)/p)$. Then there exist a constant $C = C(m, n, p, \mu) > 0$ and an increasing sequence $\{R_j\} \to \infty$ as $j \to \infty$, such that

$$
\int_{S^{n-1}} |\nabla u(R_j, \theta)|^{\mu} d\theta \le CR_j^{-p\mu/r}, \quad j = 1, 2, \dots, \qquad (2.11)
$$

where $d\theta$ is the surface area differential on $S^{n-1}$ and $r=p-m$.

Proof. We first show that for $R > R_0$

$$
\int_{B_{3R}(0) \setminus B_{2R}(0)} |\nabla u|^{\mu} \le CR^{n-p\mu/r}. \qquad (2.12)
$$

To see this, notice that one can cover the set $B_{3R}(0) \setminus B_{2R}(0)$ by a finite number of balls $B_{2R}(y_j)$ with $|y_j| = 3R$. Thus (2.12) follows immediately from (2.6) by a covering argument.

Now take a sequence of positive integers $\{K_j\} \to \infty$ such that $2K_{j+1} > 3K_j$. Then (2.12) implies

$$
\int_{2K_j}^{3K_j} t^{n-1} \int_{S^{n-1}} |\nabla u(t, \theta)|^{\mu} d\theta dt = \int_{B_{3K_j}(0) \setminus B_{2K_j}(0)} |\nabla u|^{\mu} \le CK_j^{n-p\mu/r}.
$$

Hence by the mean-value theorem for integrals, there exists $R_j \in (2K_j, 3K_j) \to \infty$ such that

$$
K_j R_j^{n-1} \int_{S^{n-1}} |\nabla u(R_j, \theta)|^{\mu} d\theta \le CK_j^{n-p\mu/r},
$$

and (2.11) follows immediately.

We can now finish the proof for the case $p=m_*$. Integrate (1.6) over $B_{R_j} \setminus B_{R_0}$ to obtain

$$
\int_{B_{R_j} \setminus B_{R_0}} u^{m_* - 1} dx \le - \int_{\partial B_{R_j}} \mathbf{u} \cdot \nu_1 d\theta - \int_{\partial B_{R_0}} \mathbf{u} \cdot \nu_2 d\theta, \quad (2.13)
$$

where $\nu_1$ and $\nu_2$ are the unit outer normal vectors (this is easily justified for the weak form of (1.6)). The left-hand side of (2.13) tends logarithmically to infinity as $j \to \infty$ since

$$
u^{m_* - 1} \ge C |x|^{-(n-m)(m_* - 1)/(m-1)} = C |x|^{-n},
$$

by (2.3). Clearly

$$
\left| \int_{\partial B_{R_0}} \mathbf{u} \cdot \nu_2 d\theta \right| \le C
$$

for some $C>0$. Using (2.11) with $\mu=m-1$ and $p=m_*>m$, one can also bound the first term on the right-hand side of (2.13) as follows:

$$
\begin{aligned} \left| \int_{\partial B_{R_j}} \mathbf{u} \cdot \nu_1 d\theta \right| &\le C(n) R_j^{n-1} \int_{S^{n-1}} |\nabla u(R_j, \theta)|^{m-1} d\theta \\ &\le C R_j^{n-1} R_j^{-(m-1)m_*/(m_*-m)} = C \end{aligned}
$$

for some $C>0$ independent of $j$ as $j \to \infty$. This contradicts (2.13), and the proof is complete.

It remains to take up the case $1<p \le m$. This will be done with the help of three lemmas.

LEMMA 2.6. Let $n>1, m>1$. There exists $R_m>0$ such that the equation

$$
\Delta_m v + v^{m-1} = 0 \quad (2.14)
$$

has a positive radial solution $v_m(|x|)$ in the ball $|x|<R_m$, with $v_m=0$ on $|x|=R_m$ and $v_m(0)=1$.

Lemma 2.6 is well-known. A proof can for example be given by the shooting method and use of Theorem 6.2 (i) of Ni and Serrin [19].

The function $v_m$ plays the role of an "eigenfunction" for equation (2.14). Since (2.14) is homogeneous in $v$, clearly any multiple of $v_m$ is also a solution in $|x|<R_m$ with zero boundary data, while moreover any translation of $v_m$ is equally a solution.

LEMMA 2.7. Let $g(s)$, $s>0$, be a positive function, with $\inf_{s>s_0} g(s)>0$ for any $s_0>0$. Suppose that $u$ is a non-negative solution of the inequality

$$
-\Delta_m u \ge g(u) \qquad (2.15)
$$

in an exterior domain $\Omega$. Then $\liminf_{x \to \infty} u(x)=0$.

Proof. An easy calculation shows that the function

$$
w(x) = \frac{1}{n^{1/(m-1)}} \frac{m-1}{m} |x|^{m/(m-1)}
$$

satisfies $\Delta_m w=1$.

Now suppose for contradiction that $\liminf_{x \to \infty} u(x)=\varepsilon>0$, and let $y^j$ be a sequence in $\Omega$ tending to $\infty$ as $j \to \infty$, such that $\lim_{j \to \infty} u(y^j)=\varepsilon$. Define $\gamma=\inf_{s>\varepsilon/2} g(s)$, so by (2.15) and the conditions on $g$,

$$
-\Delta_m u(x) \ge g(u(x)) > \gamma
$$

whenever $|x|$ is suitably large. The function

$$
w_{\varepsilon}(x) = 2\varepsilon - \gamma w(x - y^j)
$$

is positive and satisfies $-\Delta_m w_{\varepsilon}=\gamma$ when $x \in B_{R_{\varepsilon}}(y^j)$, with $w_{\varepsilon}=0$ when $|x-y^j|=R_{\varepsilon}$ for some appropriate constant $R_{\varepsilon}$. Clearly $B_{R_{\varepsilon}}(y^j) \subset \Omega$ if $|y^j|$ is large enough. Hence by the weak comparison principle we get $u \ge w_{\varepsilon}$ in $B_{R_{\varepsilon}}(y^j)$ for all suitably large $j$. In turn $u(y^j) \ge w_{\varepsilon}(y^j)=2\varepsilon$, an obvious contradiction if $|y^j|$ is sufficiently large. The lemma is proved.

Remark. An immediate consequence of Lemma 2.3 and Lemma 2.7 is that if $n \le m$, then the only possible solution of (2.15) in an exterior domain is $u=0$.

LEMMA 2.8. If $1<p \le m$, then the only solution of (1.6) in an exterior domain $\Omega$ is $u=0$.

Proof. Suppose for contradiction that $u \ne 0$ is a solution of (1.6) in $\Omega$. Then $u>0$ in $\Omega$ by Lemma 2.1. Let $y \in \Omega$ be such that the ball $B_{R_m}(y)$ is contained in $\Omega$ and $u(y) \le 1$. (The second condition is possible because of Lemma 2.7.)

Clearly there is some constant $c \in (0, 1]$ such that $u \ge cv_m > 0$ in $B_{R_m}(y)$ while also $u = cv_m$ at some point in $B_{R_m}(y)$. In turn it is not hard to see that, for any sufficiently small constant $\varepsilon > 0$, there exists a (non-empty) domain $D_{\varepsilon}$ strictly contained in $B_{R_m}(y)$, such that

$$
cv_m > u - \varepsilon \quad \text{in } D_{\varepsilon}
$$

and

$$
cv_m \le u - \varepsilon \quad \text{in } B_{R_m}(y) \setminus D_\varepsilon.
$$

Obviously for $x \in D_\varepsilon$,

$$
\begin{aligned} \Delta_m(cv_m) - \Delta_m(u - \varepsilon) &= \Delta_m(cv_m) - \Delta_m u \\ &\ge -(cv_m)^{m-1} + u^{p-1} \ge -(cv_m)^{p-1} + u^{p-1} \ge 0, \end{aligned} \quad (2.16)
$$

since $1<p \le m$, $cv_m \le v_m \le 1$ and $cv_m \le u$. By the weak comparison principle Lemma 2.2 we then find $cv_m \le u - \varepsilon$ in $D_\varepsilon$, a contradiction.

This proves Lemma 2.8, and so completes the proof of Theorem I.

*Remark.* Lemma 2.8 applies also to the more general inequality

$$
-\Delta_m u = \min(u^{p-1}, u^{m-1}),
$$

the proof being essentially the same, up to a simple and easily seen modification of the second line of (2.16).

The argument used to prove Theorem I no longer works when $p > m_*$, In fact, when $p \in (m_*, \infty)$, $n > m$, it is easy to verify directly that the equation

$$
\Delta_m u + u^{p-1} = 0
$$

(and accordingly also (1.6)) has solutions of the form $C|x-x_0|^{-m/(p-m)}$ in exterior domains.

### 3. Liouville theorems II

In this section we shall prove the (more difficult) results of Theorem II. To this end, it will be critically important to use the generalized Gidas-Spruck inequality (Theorem 6.1 below) together with the assumption that $f$ is "subcritical", in the sense that (1.7) holds for some $\alpha \in (1, m^*)$. The following lemma, extending the range of Lemma 2.4, is the key to the discussion.

LEMMA 3.1. Let $u$ be a positive weak solution of (1.4) with $n > m$, and let

$$
R > 0, \quad d \in (0, 1), \quad k > 2m.
$$

Suppose also that $f$ is subcritical, with

$$
1 < \alpha < m^* - \frac{m^* - 1}{m_*} d. \quad (3.1)
$$

Then there exists a positive constant $C=C(n, m, \alpha, d, k)$ such that

$$
\int \xi^k f^2(u) u^{2-d-m_*} \le CR^{-2m} \int \xi^{k-2m} u^{\sigma-d}, \quad (3.2)
$$

where $\sigma=2m-m_*$ and $\xi=\xi(|x-x_0|/R)$ is a scaled cut-off function on the ball $B_{2R}$, as in the proof of Lemma 2.4.

Proof. Let $A, \hat{A}, B, D, \hat{D}$ be the coefficients in (6.2). By our assumptions on $d$ and $\alpha$ we have $B>0$ and

$$
\delta = \frac{n-1}{n} \left( m^* - \alpha - \frac{m^*-1}{m_*} d \right) > 0.
$$

In turn, by (1.7),

$$
Af(u) + \hat{A}uf'(u) = \delta f(u) + \frac{n-1}{n} [(\alpha-1)f(u) - uf'(u)] \geqslant \delta f(u).
$$

Taking $\phi=[\xi(|x-x_0|/R)]^k$, one readily sees from (6.1) that

$$
\begin{aligned} \delta \int \xi^k f(u) u^{1-d-m_*} |\nabla u|^m + B \int \xi^k u^{-d-m_*} |\nabla u|^{2m} \\ \leqslant \int u^{2-d-m_*} \{\mathbf{u} \nabla^2 (\xi^k) \mathbf{u}\} + \int u^{1-d-m_*} \{D u f(u) + \hat{D} |\nabla u|^m\} \mathbf{u} \cdot \nabla (\xi^k). \end{aligned} \quad (3.3)
$$

Using Young's inequality with the respective exponent pairs

$$
\left(m, \frac{m}{m-1}\right), \quad \left(2m, \frac{2m}{2m-1}\right), \quad \left(m, \frac{m}{m-1}\right),
$$

we may bound the terms on the right side of (3.3) as follows:

$$
\begin{aligned} \left| \int u^{2-d-m_*} \{\mathbf{u} \nabla^2 (\xi^k) \mathbf{u}\} \right| &\leqslant \frac{B}{2} \int \xi^k u^{-d-m_*} |\nabla u|^{2m} + C \int u^{\sigma-d} \xi^{(1-m)k} |\nabla^2 \xi^k|^m, \\ \left| \int \hat{D} u^{1-d-m_*} |\nabla u|^m \mathbf{u} \cdot \nabla (\xi^k) \right| &\leqslant \frac{B}{2} \int \xi^k u^{-d-m_*} |\nabla u|^{2m} + C \int u^{\sigma-d} \xi^{(1-2m)k} |\nabla \xi^k|^{2m}, \\ \left| \int D f(u) u^{2-d-m_*} \mathbf{u} \cdot \nabla (\xi^k) \right| &\leqslant \frac{\delta}{2} \int \xi^k f(u) u^{1-d-m_*} |\nabla u|^m \\ &\quad + C \int f(u) u^{1-d+m-m_*} \xi^{(1-m)k} |\nabla \xi^k|^m, \end{aligned}
$$

where $B=(1-d)(m-1)d/m$ and $C=C(n, m, d, \delta)$. Hence, with the help of the estimates $|\xi|\leqslant 1$, $|\nabla\xi|\leqslant 2/R$ and $|\nabla^2\xi|\leqslant c/R^2$, we get from (3.3)

$$
\int \xi^k f(u) u^{1-d-m_*} |\nabla u|^m \leqslant a \left( R^{-2m} \int \xi^{k-2m} u^{\sigma-d} + R^{-m} \int \xi^{k-m} f(u) u^{1+m-d-m_*} \right), \quad (3.4)
$$

where the coefficient $a$ depends only on $n, m, d, \delta, k$.

Note that the condition $k>2m$ is used here to make the integrals in (3.4) well-defined.

With the crucial estimate (3.4) in hand, we can now turn to the main conclusion (3.2). The first step in its derivation is to take $\phi=\xi^k f(u) u^{2-d-m_*}$ as a test function

in the weak form of (1.4); this is allowable since $u$ is assumed to be positive. One thereby obtains

$$
\int \xi^k f^2(u) u^{2-d-m_*} = \int \xi^k (f(u) u^{2-d-m_*})' |\nabla u|^m + k \int \xi^{k-1} f(u) u^{2-d-m_*} \mathbf{u} \cdot \nabla \xi. \quad (3.5)
$$

The Young inequality with exponents $m/(m-1)$ and $m$ yields the following estimate for the second integral on the right of (3.5):

$$
\left| \int \xi^{k-1} f(u) u^{2-d-m_*} \mathbf{u} \cdot \nabla \xi \right| \le \int \xi^k f(u) u^{1-d-m_*} \{ |\nabla u|^m + (2u/[R\xi])^m \}.
$$

Moreover, the first integral can be controlled with the help of (1.7), namely

$$
\begin{aligned} (f(u) u^{2-d-m_*})' &= u^{1-d-m_*} [(2-d-m_*)f(u) + uf'(u)] \\ &\le u^{1-d-m_*} [\alpha + 1 - d - m_*] f(u) \le \frac{n}{n-m} f(u) u^{1-d-m_*} \end{aligned}
$$

since $\alpha < m_*$. Thus (3.5) gives

$$
\begin{aligned} \int \xi^k f^2(u) u^{2-d-m_*} &\le \left( \frac{n}{n-m} + k \right) \int \xi^k f(u) u^{1-d-m_*} |\nabla u|^m \\ &\quad + 2^m k R^{-m} \int \xi^{k-m} f(u) u^{1+m-d-m_*}. \end{aligned}
$$

Eliminating the first integral on the right by using (3.4) now gives

$$
\int \xi^k f^2(u) u^{2-d-m_*} \le a_1 R^{-2m} \int \xi^{k-2m} u^{\sigma-d} + a_2 R^{-m} \int \xi^{k-m} f(u) u^{1+m-d-m_*}, \quad (3.6)
$$

where $a_1 = (k+n/(n-m))a$, $a_2 = a_1 + 2^m k$.

On the other hand, by the Cauchy inequality,

$$
a_2 R^{-m} \int \xi^{k-m} f(u) u^{1+m-d-m_*} \le \frac{1}{2} \int \xi^k f^2(u) u^{2-d-m_*} + \frac{1}{2} a_2^2 R^{-2m} \int \xi^{k-2m} u^{\sigma-d}.
$$

Using this to eliminate the second integral on the right in (3.6) then yields (3.2), with the constant $C=2a_1+a_2^2$.

We also need the following weak Harnack inequality, due to Trudinger [28].

LEMMA 3.2. Let $-\Delta_m u \ge 0$ and $u \ge 0$ in $\Omega$. Then for all $\gamma \in (0, m_* - 1)$ and $R > 0$, there exists a constant $C = C(n, m, \gamma) > 0$ such that

$$
\min_{x \in B_R} u(x) \ge CR^{-n/\gamma} \|u\|_{L^\gamma(B_{2R})}. \quad (3.7)
$$

*Proof.* The function $u$ satisfies the hypotheses of Theorem 1.2 of [27], with

$$
a_0 = 1, \quad b_0 = 0; \quad a_i(x) = b_i(x) \equiv 0, \quad i \ge 1,
$$

and (3.7) then follows immediately from Theorem 1.2 of [28].$^{(5)}$

The following estimate is a consequence of Lemmas 3.1 and 3.2.

LEMMA 3.3. Let $u$ be a positive weak solution of (1.4) in $\Omega$. Assume that $f$ is subcritical and $n \in (m, 2m^2-m)$. Let

$$
\varrho = \min \left( 2, \frac{2n(m-1)}{2m^2-m-n} \right).
$$

Then for all $q \in (0, \varrho)$ there exists $C=C(n, m, \alpha, q) > 0$ such that

$$
\|fu^{1-m}\|_{L^q(B_R)} \le CR^{n/q-m}, \quad (3.8)
$$

where $B_R = B_R(x) \subset B_{4R} \subset \Omega$.

*Proof.* Choose $d$ so small that (3.1) is valid. Then using Hölder's inequality with exponents $2/q$ and $2/(2-q)$, together with (3.2), we bound

$$
\begin{align*} \int_{B_R} (fu^{1-m})^q &= \int_{B_R} u^{\sigma-d} (fu^{1-m})^q u^{d-\sigma} \\ &\le \left( \int_{B_R} f^2(u) u^{2-d-m_*} \right)^{q/2} \left( \int_{B_R} u^{q(d-\sigma)/(2-q)} \right)^{(2-q)/2} \tag{3.9} \\ &\le \left( CR^{-2m} \int_{B_{2R}} u^{\sigma-d} \right)^{q/2} \left( \int_{B_R} u^{q(d-\sigma)/(2-q)} \right)^{(2-q)/2}. \end{align*}
$$

There are now two cases.

(i) $n \in (m, 2m-1]$. Because $n \le 2m-1$ one sees at once that

$$
\sigma \le 0 \quad \text{and} \quad \varrho = \frac{2n(m-1)}{2m^2-m-n}.
$$

$^{(5)}$ The weak Harnack inequality is also a direct consequence of earlier arguments in [23]. In particular, one may apply the proof given in §3 of [23], restricting however to the case $\beta < 0$ because $u$ obeys only the super-solution inequality $-\operatorname{div}(|\nabla u|^{m-2}\nabla u) \ge 0$. This means that Case I (p. 265 of [23]) can be omitted, and the iteration of (35) in Case II must be terminated at the first point $p_\nu$ where $p_\nu = m + \beta_\nu - 1 \ge m - 1$. But then $p_{\nu-1} < m - 1$, while $p_\nu = \kappa p_{\nu-1}$, where $\kappa = m^*/m = n/(n-m)$.

In turn, by adjusting $p'_0$ appropriately (see [23, top of p. 268]), we can take $p_{\nu-1}$ arbitrarily near $m-1$. Thus the relation (40), p. 268, holds with $\max u$ replaced by $\Phi(\gamma, 2)$, where $\gamma$ is any exponent less than $(m-1)\kappa = m_* - 1$. The remainder of the argument on p. 268 of [23] (that is, Case III with $\beta < 1 - m < 0$) continues to apply, and accordingly we reach the display line immediately after (41), with $\max u$ replaced by $\Phi(\gamma, 2)$, exactly the conclusion (3.7) of Lemma 3.2.

Then, using the fact that $q<\varrho\le 2$, we obtain by direct calculation

$$
-\frac{\sigma q}{2-q} \in [0, m_* - 1).
$$

Choose $d>0$ so small that

$$
\gamma = \frac{q(d-\sigma)}{2-q} \in (0, m_* - 1).
$$

Since $\sigma-d<0$, by Lemma 3.2 we have

$$
\begin{aligned} \int_{B_{2R}} u^{\sigma-d} &\le \int_{B_{2R}} \left[ C R^{-n/\gamma} \left( \int_{B_{4R}} u^{\gamma} \right)^{1/\gamma} \right]^{\sigma-d} \\ &= C R^{2n/q} \left( \int_{B_{4R}} u^{q(d-\sigma)/(2-q)} \right)^{-(2-q)/q}. \end{aligned} \quad (3.10)
$$

Combining (3.9) and (3.10) yields (3.8).

(ii) $n \in (2m-1, 2m^2-m)$. For this case one checks in a straightforward way that $\sigma \in (0, m_* - 1)$. Choose $d>0$ so small that

$$
\gamma = \sigma - d \in (0, m_* - 1).
$$

Since $q(d-\sigma)/(2-q) < 0$, we may now (symmetrically) apply the argument of (3.10) to the second integral in (3.9), and the conclusion follows as before.

Now we are ready to prove our second Liouville theorem.

*Proof of Theorem II.* (a) First part. Let $u$ be a non-negative solution of $\Delta_m u=0$ in $\mathbf{R}^n$. By subtracting an appropriate constant, we can assume without loss of generality that $\inf_{\mathbf{R}^n} u=0$. We must show that $u\equiv 0$.

By the Harnack inequality, Theorem 5 of [23],$^{(6)}$ we have

$$
\max_{B_R(x_0)} u \le C(n, m) \min_{B_R(x_0)} u.
$$

Letting $R \to \infty$ we get

$$
\sup_{\mathbf{R}^n} u \le C(n, m) \inf_{\mathbf{R}^n} u = 0,
$$

which is the required conclusion.

Second part. As before, we can assume that $\inf_{\mathbf{R}^n} u=0$, and must show $u\equiv 0$. But if $u\not\equiv 0$, then by the strong maximum principle $u$ is everywhere positive in $\mathbf{R}^n$. Hence (2.4) gives $\inf_{x \to \infty} u(x) > 0$, so $u$ must have a zero minimum at some finite point $y$, an immediate contradiction. Case (a) is proved.

$^{(6)}$ See also Lemma 4.2 below, in the special case $\hat{c}=\hat{d}=\hat{f}=0$.

Remark. The Liouville theorem of the first part of case (a) is probably known, but we do not have a direct reference.

(b) By the second part of case (a), we can assume without loss of generality that $n>m$. Also, as previously, it is enough to consider positive solutions $u$. It is not hard to check that the hypothesis $n<2m^2-m$ of Lemma 3.3 holds in the present case, hence (3.8) is valid for any $q \in (0, \varrho)$. A short calculation verifies that $n/m < \varrho$ (recall that $1 < n/m < 2$ by assumption). Thus there exists an exponent $q \in (n/m, \varrho)$. With such a choice of $q$, by letting $R \to \infty$ in (3.8) we get

$$
\|fu^{1-m}\|_{L^q(\mathbf{R}^n)} = 0.
$$

It follows that $f(s)=0$ for all values $s$ in the range of the solution $u(x)$. Thus in turn $\Delta_m u \equiv 0$ in $\mathbf{R}^n$, whence by the Liouville theorem for the $m$-Laplacian (first part of case (a)) we get $u(x) \equiv \text{Const.}$, as required.

Before proving case (c) it is convenient to give a simple lemma. (Recall that $\sigma = 2m - m_*$.)

LEMMA 3.4. If either

$$
n=2, \ 1 < m < \frac{4}{3} \quad \text{or} \quad n \ge 3, \ n \ge 2m - \frac{1}{2}, \qquad (3.11)
$$

then

(i) $\sigma > m/n$,

(ii) $(\alpha - m)n < (2\alpha - m_* - m/n)m$ for all $\alpha \in [m, m^*]$.

Proof. It is easy to check that (i) is equivalent to $(n-m)^2 > m^2 - m$, which is satisfied in either case of (3.11). Similarly, (ii) is equivalent to

$$
n(n-m)(n-2m)\alpha < m(n^3 - 2mn^2 + m^2). \qquad (3.12)
$$

If $n \ge 2m$ it is enough to verify (3.12) when $\alpha = m^* = mn/(n-m)$, as is easily done. On the other hand, if $n=2$ or $n < 2m$ then the worst case of (3.12) occurs when $\alpha = m$, that is, we must verify

$$
nm(n-m)(n-2m) < m(n^3 - 2mn^2 + m^2).
$$

This reduces to $(n-m)^2 > m^2 - m$, and as before is satisfied in either case of (3.11). This completes the proof.

We can now return to the proof of the theorem.

(c) If either $n=2$, $m \ge \frac{4}{3}$ or $n \in [3, 2m - \frac{1}{2})$, then the result of case (b) applies, so we are done. Thus without loss of generality we can assume that either

$$
n=2, \ m < \frac{4}{3} \quad \text{or} \quad n \ge 3, \ n \ge 2m - \frac{1}{2}.
$$

Now suppose for contradiction that $u$ is a positive solution of (1.4) on $\mathbf{R}^n$, with $f$ being subcritical. By (1.8) there is some $u_0>0$ such that $f(u)\ge u^{p-1}$ for $u\ge u_0$. By integrating (1.7) we get, for $u\ge u_0$,

$$
f(u) \le \frac{f(u_0)}{u_0^{\alpha-1}} u^{\alpha-1}.
$$

Comparing the last lines it follows that $p\le\alpha$. Again by integrating (1.7), we find for $u\le u_0$

$$
f(u) \ge \frac{f(u_0)}{u_0^{\alpha-1}} u^{\alpha-1} \equiv \lambda u^{\alpha-1}, \quad (3.13)
$$

where $\lambda\ge u_0^{p-\alpha}>0$.

Consider first the case when $p>m$, so that $m<p\le\alpha<m^*$. Define

$$
\sigma = 2m - m_*, \quad \tau = 2p - m_*, \quad \nu = 2\alpha - m_*.
$$

Then clearly

$$
\tau - \sigma = 2(p - m) > 0, \quad \nu - \sigma = 2(\alpha - m) \ge 2(p - m) > 0.
$$

Also by Lemma 3.4 (i),

$$
\sigma - d > 0, \quad \tau - d > 0 \quad (3.14)
$$

provided $d$ is fixed less than $m/n$.

Let $k>2m$. From (3.2), with the positive constant $C$ rewritten as $C_1$, we have

$$
\int \xi^k f^2(u) u^{2-m_*-d} \le C_1 R^{-2m} \int \xi^{k-2m} u^{\sigma-d}
$$

(since $\alpha<m^*$, the hypothesis (3.1) of Lemma 3.1 is satisfied if $d$ is made even smaller, if necessary).

Now, for $u\ge u_0$, by Young's inequality with the exponent pair

$$
\frac{\tau - d}{\sigma - d}, \quad \frac{\tau - d}{\tau - \sigma},
$$

we get (since $f(u)\ge u^{p-1}$)

$$
(\xi R)^{-2m} u^{\sigma-d} \le \frac{1}{2C_1} f^2(u) u^{2-m_*-d} + C_2 (\xi R)^{-m(\tau-d)/(p-m)}; \quad (3.15)
$$

while for $u\le u_0$, similarly (since $f(u)\ge\lambda u^{\alpha-1}$)

$$
(\xi R)^{-2m} u^{\sigma-d} \le \frac{1}{2C_1} f^2(u) u^{2-m_*-d} + C_3 (\xi R)^{-m(\nu-d)/(\alpha-m)} \quad (3.16)
$$

for appropriate constants $C_2$ and $C_3$. Combining the previous lines yields (with the constant $C=2C_1 \max(C_2, C_3)$)

$$
\int_{B_R} f^2(u) u^{2-m_*-d} \le C \max [R^{n-m(\tau-d)/(p-m)}, R^{n-m(\nu-d)/(\alpha-m)}] \quad (3.17)
$$

provided that $k$ is taken suitably large (greater than both $m(\tau-d)/(p-m)$ and $m(\nu-d)/(\alpha-m)$; in fact $k=2mp/(p-m)$ suffices for all purposes.⁽⁷⁾)

We assert that

$$
n-m \frac{\tau-d}{p-m} \le n-m \frac{\nu-d}{\alpha-m} < 0. \quad (3.18)
$$

Indeed the first inequality can be rewritten in the form $(\alpha-p)(\sigma-d) \ge 0$, which is clearly satisfied in view of (3.14). The second (strict) inequality, on the other hand, follows at once from Lemma 3.4 (ii), since $d<m/n$.

Let $R \to \infty$ in the inequality (3.17). In view of (3.18) there results

$$
\int_{\mathbb{R}^n} f^2(u) u^{2-m_*-d} = 0.
$$

But this is impossible because, as we have seen, $f(u)>0$ for all $u>0$.

There remains the case $p \le m$. Here by assumption also $\alpha \le m$. Now by hypothesis $f(u) \ge u^{p-1}$ for $u \ge u_0$. Also (3.13) gives $f(u) \ge \lambda u^{\alpha-1}$ for $u \le u_0$. Hence

$$
-\Delta_m u \ge \min(\lambda u^{\alpha-1}, u^{p-1}) \ge l \min(u^{m-1}, u^{p-1}),
$$

where $l=\min(\lambda, 1)$. After a trivial change of scale, it now follows from the remark after the proof of Lemma 2.8 that $u \equiv 0$.

(d) This is an immediate consequence of Theorem I.

*Remark.* The proof of parts (b), (c) give upper bounds for various norms of $u$ in terms of the radius of the ball $B_R$, see (3.8) and (3.17); these can be considered as another type of universal a priori estimate.

*Proof of Theorem III.* Let $M$ be the upper bound for the solution $u$, that is, $0 < u(x) \le M$ in $\mathbb{R}^n$. As in (3.13), there holds

$$
f(u) \ge \frac{f(M)}{M^{\alpha-1}} u^{\alpha-1} \equiv \hat{\lambda} u^{\alpha-1}
$$

⁽⁷⁾ For its interest, one may note that

$$
C_2 = (2C_1)^{(\sigma-d)/(\tau-d)}, \quad C_3 = (2C_1/\lambda^2)^{(\sigma-d)/(\nu-d)}.
$$

for $u \le M$. Here it should be noted that $\hat{\lambda}>0$, since by assumption $f(u)>0$ for all $u>0$.

Arguing as in the proof of case (c), but without the necessity for introducing the constant $\tau$ or deriving the inequality (3.15), we obtain (3.16), this now being valid for all $x$ in $\mathbf{R}^n$. Inequality (3.17) is therefore replaced simply by

$$
\int_{B_R} f^2(u) u^{2-m_*-d} \le 2C_1C_3R^{n-m(\nu-d)/(\alpha-m)},
$$

and the proof is completed with the help of (3.18) exactly as before.

## 4. The Harnack inequality

Here we establish Harnack inequalities for weak solutions of the equation (1.4) and the inequality (1.6), see Theorems 4.1-4.3.

As previously, $B_R=B_R(x_0)$ denotes a ball centered at $x_0$ with radius $R$, such that the corresponding ball $B_{2R}(x_0)$ of radius $2R$ is contained in $\Omega$. Our arguments will be restricted throughout to such "admissible" balls $B_R$. Moreover, the letter $C$ denotes a generic positive constant, which may vary from line to line and only depends on the arguments inside the parenthesis.

The following result is an extension and generalization of Lemma 2.4.

LEMMA 4.1. (i) Assume that $m<p<m_*$ in Lemma 2.4. Then (2.5) holds for all $\gamma \in (0, m_*-1)$, and (2.6) for all $\mu \in (0, n(m-1)/(n-1))$.

(ii) Assume $p>m$, and let $u$ be a non-negative weak solution of the differential inequality

$$
-\Delta_m u \ge u^{p-1} - u^{m-1} - |\nabla u|^{m-1} \quad \text{in } \Omega.
$$

Then there exists a constant $C=C(n, m, p, \gamma)>0$ such that

$$
\int_{B_R} u^{\gamma} \le CR^{n-m\gamma/r} + CR^n, \quad (4.1)
$$

for all $\gamma \in (0, m_*-1)$ provided $m<p<m_*$, and for all $\gamma \in (0, p-1)$ provided $m_* \le p < m^*$.

Proof. (i) We proceed as in the proof of Lemma 2.4. To begin with, for $k>m$ we have

$$
\nabla(\xi^{k/m} u^{(\gamma-r)/m}) = \xi^{k/m} \frac{\gamma-r}{m} u^{(\gamma-p)/m} \nabla u + \frac{k}{m} \xi^{k/m-1} u^{(\gamma-r)/m} \nabla \xi.
$$

With the help of the elementary inequality $|x+y|^m \le 2^{m-1}(|x|^m + |y|^m)$, an easy calcula-

tion then leads to (recall $|\nabla\xi| \le 2/R$)

$$
\begin{align*}
& d \int |\nabla(\xi^{k/m} u^{(\gamma-r)/m})| + \left(\frac{2(\gamma-r)}{m}\right)^m \int \xi^k u^\gamma \\
& \le \left(\frac{2(\gamma-r)}{m}\right)^m \left[ \frac{d}{2} \int \xi^k u^{\gamma-p} |\nabla u|^m + \int \xi^k u^\gamma \right] + \left(\frac{4k}{m}\right)^m \frac{d}{2} R^{-m} \int \xi^{k-m} u^{\gamma-r} \\
& \le C(m, k, p, \gamma) R^{-m} \int \xi^{k-m} u^{\gamma-r}
\end{align*}
$$

by virtue of (2.8). Then exactly as in the derivation of (2.9) from (2.8), we find that

$$
\int |\nabla(\xi^{k/m} u^{(\gamma-r)/m})|^m \le CR^{n-m\gamma/r}
$$

for $\gamma \in (r, p-1)$. Then by the Sobolev inequality,

$$
\int [\xi^{k/m} u^{(\gamma-r)/m}]^{m^*} \le CR^{(n-m\gamma/r)m^*/m}.
$$

Rewriting this by setting $\bar{\gamma}=m^*(\gamma-r)/m$, we obtain exactly (2.5) with $\gamma$ replaced by $\bar{\gamma}$. But from the condition $\gamma \in (r, p-1)$ then follows $\bar{\gamma} \in (0, m_*-1)$, which is the first result.

The second is then obtained by following the derivation of (2.6), but using at the final step the result just shown.

*Remark.* We have not in fact used the condition $p < m_*$ in this argument. However, if $p \ge m_*$ then the original restriction $\gamma < p-1$ is weaker than or equivalent to $\gamma < m_*-1$. This can be restated alternately, that (2.5) holds for any $\gamma \in (0, \max(p-1, m_*-1))$.

(ii) The proof of Lemma 2.4 carries over without difficulty, once one notes that the inequality (2.7) continues to hold, but with the addition of two further terms

$$
\int \xi^k u^{\gamma-r} + \int \xi^k u^{-d} |\nabla u|^{m-1}
$$

on the right side. In turn, we derive (2.8) essentially as before, but now with an added term

$$
C \int \xi^k u^{\gamma-r}
$$

on the right-hand side. Finally, again essentially as before, by Young's inequality one gets (2.9) with an additional term $CR^n$ on the right side. The rest of the proof then follows exactly as in Lemma 2.4 and the previous case (i).

LEMMA 4.2. Assume $\Omega \subset \mathbf{R}^n$ and $n>m$. Let $u$ be a non-negative weak solution (in $W_{\text{loc}}^{1,m} \cap C$) of the two-sided inequality

$$
|\Delta_m u| \le \hat{d}u^{m-1} + \hat{f}, \quad (4.2)
$$

where $\hat{d}$ and $\hat{f}$ are non-negative measurable functions on $\Omega$. Let $q \in (n/m, n/(m-1))$. Then for every $R>0$ for which $B_R$ is admissible, there exists a constant $C$, depending only on the parameters

$$
n, m, q, R^{m-n/q} \|\hat{d}\|_{L^q(B_{2R})},
$$

such that

$$
\sup_{B_R} u \le C \left( \inf_{B_R} u + R^{m-n/q} \|\hat{f}\|_{L^q(B_{2R})} \right). \quad (4.3)
$$

With slight change of notation, this is exactly the special case $c=0$ of Theorem 5 of [23], after restriction to the operator $\mathcal{A}(p)=|p|^{m-2}p$, see §1 of [23]. The factor $R^{m-n/q}$ is just that required to rescale to the unit ball $B_1$ in the proof of Theorem 5; see p. 263 of [23].

Remark. Lemma 4.2 also holds when $n=m$, and even when $n<m$ provided $q=1$; see §1, relation (8), and §6 of [23].

We can now prove our first Harnack inequality. It will be assumed unless otherwise stated that $n>m$. All balls $B_R$ are assumed to be admissible, in the sense noted at the beginning of the section.

THEOREM 4.1. (a) Suppose $n>m$ and $p \in (m, m_*)$. Let $u$ be a non-negative weak solution of the differential inequality

$$
u^{p-1} \le -\Delta_m u \le \Lambda u^{p-1} \quad \text{in } \Omega, \quad (4.4)
$$

for some constant $\Lambda>1$. Then there is a constant $C=C(n, m, p, \Lambda)>0$ such that

$$
\sup_{x \in B_R} u(x) \le C \inf_{x \in B_R} u(x). \quad (4.5)
$$

(b) If $m<p \le s < m_*$ and (4.4) is replaced by

$$
u^{p-1} - u^{m-1} - |\nabla u|^{m-1} \le -\Delta_m u \le \Lambda (u^{s-1} + u^{m-1} + |\nabla u|^{m-1}) \quad \text{in } \Omega, \quad (4.6)
$$

then (4.5) holds with $C=C(n, m, p, s, \Lambda, R)>0$. The constant $C$ may become arbitrarily large if $R \to 0$ (when $p<s$) or if $R \to \infty$.

Proof. (a) First assume $B_{4R} \subset \Omega$. We shall apply the Harnack inequality, Lemma 4.2. In the present case, in view of (4.2) and (4.4) we can take $\hat{c}=\hat{f}=0$ and

$$
\hat{d} = \hat{d}(x) = \Lambda u^{p-m}.
$$

We require an estimate of the norm $I \equiv \|\hat{d}(x)\|_{L^q(B_{2R})}$ for some $q \in (n/m, n/(m-1))$.

By the left side of (4.4) and by (2.5) with $B_R$ replaced by $B_{2R}$, we get

$$
I^q \le \Lambda^q \int_{B_{2R}} u^{(p-m)q} \le C \Lambda^q R^{n-mq(p-m)/(p-m)} = C R^{n-mq}
$$

provided $q$ satisfies the principal condition $\gamma=(p-m)q<p-1$. Since $p<m_*$, however, it is easy to see that one can choose (and fix) a value $q \in (n/m, n/(m-1))$ so that this condition holds. Hence $I \le C \Lambda R^{n/q-m}$ and in turn $R^{m-n/q}I \le C \Lambda$.

Lemma 4.2 now gives the conclusion (4.5), but under the additional assumption $B_{4R} \subset \Omega$. By a chaining argument, increasing $C$ appropriately, but still dependent only on $n, m, p, \Lambda$, one can replace $B_{4R}$ by $B_{2R}$. This finishes the proof for case (a).

(b) Again it will be assumed to begin with that $B_{4R} \subset \Omega$. From (4.2) and (4.6) we have $\hat{f}=0$ and

$$
\hat{c} = \Lambda, \quad \hat{d} = \Lambda(u^{s-m} + 1).
$$

Therefore, besides an estimate for the norm $I$ we shall also need to bound the norm $J = \|\hat{c}\|_{L^{q'}(B_{2R})}$ for some $q' \in (n, \infty)$. First,

$$
I^q \le \Lambda^q \int_{B_{2R}} (u^{s-m} + 1)^q \le 2^{q-1} \Lambda^q \int_{B_{2R}} (u^{(s-m)q} + 1) = 2^{q-1} \Lambda^q \int_{B_{2R}} (u^\gamma + 1), \quad (4.7)
$$

where $\gamma \equiv (s-m)q$. By choosing $q$ near enough to $n/m$, and recalling that $s < m_*$, we have $\gamma < s-1 < m_*-1$. Hence, with the help of Lemma 4.1 (ii) and the left-hand inequality of (4.6), it follows that

$$
I^q \le C \Lambda^q (R^{n-m\gamma/(p-m)} + R^n) = C \Lambda^q (R^{n-mq(s-m)/(p-m)} + R^n),
$$

where $C=C(n, m, p, s)$. Moreover, $J = \Lambda(\int_{B_{2R}})^{1/q'} = C \Lambda R^{n/q'}$. In turn (with the appropriate rescaling factors)

$$
R^{m-n/q}I \le C \Lambda (R^{-(s-p)/(p-m)} + R)^m, \quad R^{1-n/q}J = C \Lambda R. \quad (4.8)
$$

Lemma 4.2 now yields the required conclusion, since the ball $B_{4R}$ can always be replaced by $B_{2R}$. The proof is complete.

Remark. When $s=p$ the first estimate of (4.8) reduces to $R^{m-n/q}I \le C \Lambda (1+R)^m$. In turn the coefficient $C=C(n, m, p, s, \Lambda, R)$ in (4.5) becomes $C=C(n, m, p, \Lambda, R)$, of course remaining bounded as $R \to 0$.

THEOREM 4.2. Let $u$ be a solution of (1.4), with $n>m$. Then:

(a) If $f$ is subcritical and either $n=2$ and $m > (1+\frac{1}{4}\sqrt{17})$ or $n \in [3, 2m)$, $m > \frac{3}{2}$, then

$$
\sup_{B_R} u \le C \inf_{B_R} u \quad (4.9)
$$

for some constant $C=C(n, m, \alpha)$.

(b) Suppose that $f$ is subcritical, and that for some $p>m$

$$
u^{p-1} \le f(u) \le \Lambda u^{p-1} \quad \text{for all } u > 0. \quad (4.10)
$$

Then (4.9) holds with $C=C(n, m, p, \alpha, \Lambda)$.

(c) Let the conditions of case (b) hold, but with (4.10) replaced by

$$
u^{p-1} \le f(u) \le \Lambda(u^{p-1} + u^{m-1}) \quad \text{for all } u > 0. \quad (4.11)
$$

Then (4.9) is satisfied with $C=C(n, m, p, \alpha, \Lambda, R)$. The constant $C$ remains bounded as $R \to 0$.

Proof. (a) As in the proof of Theorem 4.1 we shall apply Lemma 4.2. By (1.4) and (4.2) one can take $\hat{c}=\hat{f}=0$ and

$$
\hat{d} = \hat{d}(x) = u^{1-m} f(u).
$$

We must estimate the norm $I \equiv \|\hat{d}(x)\|_{L^q(B_{2R})}$ for some $q \in (n/m, n/(m-1))$.

As in the proof of Theorem II (b) we can choose $q$ so that $q \in (n/m, \varrho)$, and even more so that $q \in (n/m, n/(m-1))$. Then by Lemma 3.3, we find

$$
I \le CR^{n/q-m},
$$

and the Harnack inequality follows exactly as in Theorem 4.1 (a).

(b) Before proceeding with the main proof, we note that necessarily $p \le \alpha$, as follows by integration of (1.7); see (3.13).

Now utilizing the left side of (4.10) in (3.2) gives

$$
\int \xi^k u^{\tau-d} \le CR^{-2m} \int \xi^{k-2m} u^{\sigma-d}, \quad (4.12)
$$

where $\tau=2p-m_*$, $\sigma=2m-m_*$ and $d$ is chosen so that (3.1) is satisfied.

If $n=2$ and $m \ge \frac{4}{3}$, or if $n \ge 3$ and $n \le 2m - \frac{1}{2}$, the previous case (a) applies and we are done. It is therefore enough to consider the ranges $n=2$, $m < \frac{4}{3}$ and $n \ge 3$, $n > 2m - \frac{1}{2}$.

Lemma 3.4 shows that $\sigma > m/n$ in both. We may of course suppose that $d < m/2n$, so that $\sigma - d > m/2n$. Clearly $\tau - d > \sigma - d$ since $p > m$. Then from the Young inequality with exponents

$$
\frac{\tau - d}{\sigma - d}, \quad \frac{\tau - d}{\tau - \sigma},
$$

we find (with the usual trick)

$$
CR^{-2m} \int \xi^{k-2m} u^{\sigma-d} \le \frac{1}{2} \int \xi^k u^{\tau-d} + CR^{n-(\tau-d)m/(p-m)},
$$

since $\tau - \sigma = 2(p - m)$. Note also that we must take $k$ suitably large, say $k = 2pm/(p - m)$; see the analogous derivation of (3.17) in the previous section. In turn, with the aid of (4.12),

$$
\int_{B_{2R}} u^{\tau-d} \le CR^{n-(\tau-d)m/(p-m)}, \quad (4.13)
$$

where we have replaced $B_R$ by $B_{2R}$ and used the fact that $B_{4R} \subset \Omega$.

We assert that

$$
(p-m) \frac{n}{m} < \tau - \frac{m}{n}. \quad (4.14)
$$

In fact, since $m < p \le \alpha$, therefore also $p \in (m, m^*)$. Hence (4.14) is exactly the result of Lemma 3.4 (ii) with $\alpha$ replaced by $p$.

We are now able to estimate the norm $I$. First, by the right side of (4.10) there results

$$
I^q \le \Lambda^q \int_{B_{2R}} u^{(p-m)q}.
$$

By (4.14) and the fact that $d < m/2n$, one can choose $q \in (n/m, n/(m-1))$ so that $(p-m)q < \tau - d$. Then by Hölder's inequality,

$$
I^q \le C \Lambda^q R^{n(1-(p-m)q/(\tau-d))} \left( \int_{B_{2R}} u^{\tau-d} \right)^{(p-m)q/(\tau-d)} \le C \Lambda^q R^{n-mq}
$$

by (4.13). The rest of the proof is as before.

(c) The inequality (4.13) follows exactly as in case (b). On the other hand, by the right side of (4.11),

$$
I^q \le \Lambda^q \int_{B_{2R}} (u^{p-m} + 1)^q \le 2^{q-1} \Lambda^q \int_{B_{2R}} (u^{(p-m)q} + 1).
$$

Hence, exactly as in case (b), one gets $I \le C \Lambda (R^{n/q-m} + R^{n/q})$. With the rescaling factor of Lemma 4.2, we then find

$$
R^{m-n/q} I \le C \Lambda (1 + R^m).
$$

The Harnack inequality (4.9) now follows as previously, except of course the coefficient $C$ now depends on $R$.

Harnack inequalities can also be given when $n \le m$, the case earlier left aside.

THEOREM 4.3. Let $n \le m$. Then:

(a) Assume the hypotheses of Theorem 4.1 (a), except that the condition $p \in (m, m_*)$ is replaced by $p \in (1, \infty)$, that is, $m_* = \infty$. Then (4.5) is valid with $C=C(n, m, p, \Lambda)$.

(b) Assume the hypotheses of Theorem 4.1 (b), with $m < p \le s < \infty$. Then (4.5) holds with $C=C(n, m, p, s, \Lambda, R)$.

*Proof.* Everything is the same as in the proof of Theorem 4.1, with the exception that the exponents $q, q'$ must be chosen as in the remark after the proof of Lemma 4.2. Such a choice is obviously possible, and the proof is complete.

*Remark.* Since $q$ is here subject to a weaker condition than in the previous case $n > m$, it is no longer necessary to have the upper bound $p < m_*$ or $\alpha < m^*$.

*Comment on the form of the coefficient $C$ in (4.9).* This constant arises in a complicated way, depending on Lemmas 3.1, 3.2, 3.3, 4.2, as well as on the coefficient on the right side of (4.13). By following the proof, however, it is not hard to see that the corresponding coefficients $C$ can become unbounded only when one or another of the following limits occur:

$$
d \to 0; \quad m \to n; \quad q \to \varrho; \quad q \to n/m; \quad 2m^2 - m \to n; \quad p \to m
$$

(omitting the trivial limits $m, n \to 1$, $m, n \to \infty$ and $\Lambda \to \infty$). Moreover, $d \to 0$ only when $\alpha \to m^*$; $q \to \varrho$ or $q \to n/m$ only when $m \to n$ or $m \to \frac{1}{2}n$ (in the proof of Theorem 4.2 (a)); and $2m^2 - m \to n$ only when $n=2$ and $m \to \frac{1}{4}(1+\sqrt{17})$.

In turn, the coefficient $C=C(n, m, \alpha)$ in case (a) can become unbounded only if $\alpha \to m^*$, or $n=2$ and $m \to \frac{1}{4}(1+\sqrt{17})$, or $n \ge 3$ and $m$ approaches either $n$ or $\frac{1}{2}n$.

Similarly, the coefficient $C=C(n, m, p, \alpha, \Lambda)$ in case (b) can become unbounded only if $\alpha \to m^*$, or $p \to m$, or $m \to n$ (and of course $\Lambda \to \infty$).

## 5. Universal a priori estimates

In this section, we shall establish the universal a priori estimate Theorem IV, as well as several other related conclusions. The notation will be adapted from the previous section, in particular, $B_R = B_R(x_0) \subset B_{2R} = B_{2R}(x_0) \subset \Omega$.

*Proof of Theorem IV.* (a) By (1.9), Lemma 4.1 (ii) implies that there exists a constant $C=C(m, n, p) > 0$ such that

$$
\int_{B_R} u^r \le C(R^{n-m} + R^n)
$$

where $r=p-m$. Therefore

$$
\inf_{B_R} u^r \le \frac{1}{|B_R(x)|} \int_{B_R} u^r \le C(1+R^{-m}).
$$

In turn,

$$
\inf_{B_R} u \le C(1+R^{-m/r}). \quad (5.1)
$$

On the other hand, again by (1.9), a simple modification of Theorem V (a) implies that, for $R \le 1$, there exists a constant $C=C(m, n, p, \Lambda) > 0$ such that for $x \in B_R$,

$$
u(x) \le \sup_{B_R} u \le C(\inf_{B_R} u + 1). \quad (5.2)
$$

The conclusion (1.10) now follows at once from (5.1) and (5.2).

To prove the second part of Theorem IV (a), note first that in this case (5.1) is now valid without the additional term $R^{-m/r}$ and also without the restriction $R \le 1$. Similarly, in view of the second part of Theorem V (a), the inequality (5.2) holds with no restriction on $R$ and without the additive term 1. The required conclusion then follows as before.

*Remark.* A similar result can also be given for the differential inequality (4.6).

(b) We first prove (1.10) under the assumption (1.11). This being the case, we need to apply Lemma 4.2 with

$$
\hat{c} \equiv 0, \quad \hat{d} = \Lambda u^{p-m}, \quad \hat{f} \equiv \Lambda.
$$

Proceeding exactly as in Theorem 4.2 (b), we deduce that there exists $C=C(n, m, p) > 0$ such that

$$
\|\hat{d}\|_{L^q(B_{2R})} \le C \Lambda R^{n/q-m}
$$

for some $q \in (n/m, n/(m-1))$. Therefore, by (4.3), since $\|\hat{f}\|_{L^q(B_{2R})} = C \Lambda R^{n/q}$ we get

$$
\sup_{B_R} u \le C(\inf_{B_R} u + R^m) \quad (5.3)
$$

for some $C=C(n, m, p, \Lambda) > 0$.

On the other hand, by (1.11) and Lemma 2.4, we have

$$
\inf_{B_R} u^{p-m} \le \frac{1}{|B_R(x)|} \int_{B_R} u^{p-m} \le C R^{-m}
$$

for some $C=C(n, m, p) > 0$, that is,

$$
\inf_{B_R} u \le C R^{-m/(p-m)}. \quad (5.4)
$$

Now (1.10) follows immediately from (5.3) and (5.4).

Next suppose that (1.12) holds in place of (1.11). Then (5.3) is valid without the additional term $\Lambda R^m$ since $\hat{f}=0$. Therefore in (1.10) one has $R=\min(x, \partial\Omega)$, and the proof is complete.

We say that the exponent $m/(p-m)$ in (1.10) is optimum, if for any $\delta>0$ there exist a domain $\Omega$ and a solution $u$ of (1.4) in $\Omega$ such that

$$
u(x) \geq C\delta^{-m/(p-m)} \quad (5.5)
$$

for some $x \in \Omega$ satisfying $\text{dist}(x, \partial\Omega) = \delta$, where the constant $C=C(n, m, p)$ is independent of the solution as well as the domain $\Omega$.

When $f=u^{p-1}$ and $p \in (m_*, m^*)$, the singular solution of (1.4) defined in the proof of Corollary I (see the Introduction) immediately reveals that $m/(p-m)$ is optimum, by placing the singularity $x=0$ on the boundary. In fact, we have the following more complete result.

**PROPOSITION 5.1.** Assume that $n>m$, $p \in (m, m^*)$ and $f=u^{p-1}$. Then the exponent $m/(p-m)$ is optimum for (1.10).

*Proof.* Let $m>1$ and $p>m$. Consider the initial value problem

$$
\begin{cases} (|u'|^{m-2}u')' + u^{p-1} = 0, & u > 0, t > 0, \\ u(0) = u_0 > 0, \\ u'(0) = 0. \end{cases} \quad (\text{IVP})
$$

Local existence and uniqueness are well known, with $u'<0$ for $t>0$. Furthermore, since $(|u'|^{m-2}u')'<0$, it is easy to see that the solution can be continued, still with $u'<0$, as long as $u>0$; see for example the Appendix of [19]. Define

$$
T_0 = \sup\{T > 0 \mid u(t) > 0 \text{ for } t \in [0, T)\}.
$$

Then since $p<m^*$ we get from [16, Theorem 6.2]

$$
T_0 < \infty, \quad u(T_0) = 0.
$$

Therefore

$$
((-u')^{m-1}(t))' = u^{p-1}(t), \quad t \in (0, T_0]. \quad (5.6)
$$

Multiply (5.6) by $u'$ and integrate from 0 to $t \in (0, T_0]$ to obtain

$$
-\frac{m-1}{m}(-u')^m = \frac{1}{p}(u^p(t) - u_0^p).
$$

It follows that

$$
-C \frac{u'}{u_0} \left(1 - \frac{u^p(t)}{u_0^p}\right)^{-1/m} = u_0^{(p-m)/m}, \quad (5.7)
$$

where

$$
C = \left( \frac{p(m-1)}{m} \right)^{1/m}.
$$

Integrating (5.7) once more from 0 to $t$, we get

$$
tu_0^{(p-m)/m} = \int_{u(t)/u_0}^{1} (1-s^p)^{-1/m} ds,
$$

that is,

$$
u_0 = \left( C \int_{u(t)/u_0}^{1} (1-s^p)^{-1/m} ds \right)^{m/(p-m)} \cdot t^{-m/(p-m)}.
$$

In particular,

$$
u_0 = KT_0^{-m/(p-m)}, \quad (5.8)
$$

where

$$
K = K(m, p) = \left( C \int_{0}^{1} (1-s^p)^{-1/m} ds \right)^{m/(p-m)} > 0.
$$

For $\delta>0$, let $B=B_\delta$ be the ball centered at 0 with radius $\delta$, and let $u=u(t)$ be the unique solution of (IVP) with $u_0=K\delta^{-m/(p-m)} >0$. By (5.8), for this solution we have $T_0=\delta$. It follows that

$$
v(x) = v(x_1, x_2, \dots, x_n) = u(x_1)
$$

is a solution of (1.4) which is defined and positive in $B$, and of course depends only on the variable $x=x_1$. Clearly $\text{dist}(0, \partial B)=\delta$, while $u(0)=u_0=K\delta^{-m/(p-m)} >0$. This is just (5.5), and the proof is complete.

It is also interesting to know for what values of $p$ the estimate (1.10) holds at all. Again, we consider the pure power $f=u^{p-1}$ for simplicity.

**PROPOSITION 5.2.** Let $n>m$. Then (1.10) fails to hold for (1.4) if $p=m$ or $p \ge m^*$. Similarly (1.10) fails for (1.6) if $p=m$ or $p > m^*$.

*Proof.* For $p=m$, the equation (1.4) is homogeneous. Clearly a multiple of a non-trivial non-negative solution is still a solution, which can have an arbitrarily large maximum value, whence (1.10) cannot hold. On the other hand, when $p \ge m^*$, it is well-known (e.g., Theorem 6.4 of [19]) that (1.4) has positive entire solutions on the entire space $\mathbf{R}^n$, whose maximum value can be arbitrarily large. Again, (1.10) cannot hold.

For (1.6), we observe that when $p>m_*$ the solution given in the proof of Corollary II (iii) takes arbitrarily large values $C'\kappa^{-(m-1)/(p-m)}$ when $x=0$, so again (1.10) fails. The proof is complete.

Remarks for the supercritical range $p \ge mn/(m-n)$. Proposition 5.2 indicates that the optimum range of $p$ for the global estimate (1.10) to hold for (1.1) is $(m, m^*)$. Yet a corresponding local version (1.13) near an isolated singularity may continue to hold outside this range. Indeed, for $m=2$ and $p=2n/(n-2)$, the estimate (1.13) was established for solutions of (1.1) by Caffarelli, Gidas and Spruck, see [6, Theorem 1.1, p. 272], though there the constant $C$ might depend on the solution itself.

For a non-removable singularity at the origin, the estimate can be strengthened to show that $C$ is independent of the solution for sufficiently small $|x|$ (see [6, Theorem 1.2, p. 273]). Of course, similar estimates hold on exterior domains via the Kelvin transform (always assuming $m=2$).

On the other hand, when $n>m+1$ and $p \ge m(n-1)/(n-m-1)$, (1.13) need not hold for an exterior domain, in contrast to case (ii) of Corollary IV. To see this, we observe that $u^{p-1}$ is supercritical for the dimension $n-1$ if $n>m+1$ and $p \ge (n-1)m/(n-m-1)$. Thus (1.1) has a positive radial solution $u_0(r)$ on $\mathbf{R}^{n-1}$ (e.g., Theorem 6.4 of [19]). Put

$$
u(x) = u(x', x_n) = u_0(|x'|).
$$

Obviously $u$ is also a solution of (1.1) on $\mathbf{R}^n$, but (1.13) does not hold in an exterior domain since $u$ is constant ($>0$) along the direction $x_n$.

Whether the local estimate (1.13) holds for (1.4) in $B_1(0)\setminus\{0\}$ remains open even for the pure power $f=u^{p-1}$ when $p \in [m^*, (n-1)m/(n-m-1)]$, except $m=2$ and $p=2n/(n-2)$.

Finally, it is interesting to note that, for a positive solution $u$ of (1.4) on $\mathbf{R}^n$, the estimate (1.13) for large $|x|$ is equivalent to the radial symmetry of $u$, provided $m=2$ and $p \in (2n/(n-2), 2(n-1)/(n-3))$. In fact, (1.13) plainly holds if $u$ is radially symmetric. On the other hand, (1.13) for large $|x|$ implies that $u$ must be radially symmetric with respect to some point $x_0 \in \mathbf{R}^n$ by Theorem 1.1, p. 48, of [33], provided $p \in (2n/(n-2), 2(n-1)/(n-3))$.

## Chapter II

### 6. A general integral inequality I

In this section we shall establish an important integral inequality for solutions $u$ of (1.4), generalizing the Gidas-Spruck identity for solutions of (1.4) in the case $m=2$. The

following agreements will be used throughout. Boldface lower and upper case letters respectively denote vector and matrix quantities; when $\mathbf{x}$ is a vector and $\mathbf{A}$ a matrix, by $\{\mathbf{x}\mathbf{A}\mathbf{x}\}$ we mean the quadratic form $\mathbf{x} \cdot (\mathbf{A}\mathbf{x})$, where standard matrix multiplication is always understood and $\mathbf{x} \cdot \mathbf{y}$ means the inner product of the vectors $\mathbf{x}$ and $\mathbf{y}$.

For a weak solution $u \in C^1(\Omega)$ of (1.4), we introduce the *centrally important vector field*

$$
\mathbf{u} = |\nabla u|^{m-2} \nabla u, \qquad (6.1)
$$

where in the usual way it is understood that $\mathbf{u}=0$ when $\nabla u=0$ (recall $m>1$). (The simple notation $\mathbf{u}$ in (6.1) may not carry a clear indication of the meaning of this vector; alternative notations suggest themselves but all seem cumbersome in view of the many appearances of this vector in later places. Consequently we retain the indicated notation, and simply remind the reader again of the central importance of the vector $\mathbf{u}$.) Recall that

$$
m_* = \frac{m(n-1)}{n-m}, \quad m^* = \frac{mn}{n-m}.
$$

Then we have the following principal result.

PROPOSITION 6.1. Suppose $m \in (1, n)$. Let $u$ be a positive weak solution of (1.4) and $\phi \in C_0^\infty(\Omega)$ a non-negative test function.

Then for any $d \in \mathbf{R}$ we have

$$
\int u^{1-m_*-d}\{Af(u)+\hat{A}uf'(u)\}|\nabla u|^m\phi + B \int u^{-m_*-d}|\nabla u|^{2m}\phi \le \int u^{1-m_*-d}\{Duf(u)+\hat{D}|\nabla u|^m\}\mathbf{u} \cdot \nabla\phi + \int u^{2-m_*-d}\{\mathbf{u}\nabla^2\phi\mathbf{u}\}, \qquad (6.2)
$$

where $\nabla^2\phi$ is the Hessian of $\phi$ and

$$
\begin{aligned} A &= \frac{n-1}{n} \left(1 - \frac{d}{m_*}\right) (m^* - 1), \quad \hat{A} = -\frac{n-1}{n}, \quad B = \frac{m-1}{m} d(1-d), \\ D &= -\frac{n+1}{n}, \quad \hat{D} = \left(2 - \frac{m_*}{m}\right) - \left(2 - \frac{1}{m}\right) d. \end{aligned} \qquad (6.3)
$$

The vector $\mathbf{u}$ is nonlinear in $\nabla u$ when $m \ne 2$; this makes the proof of Proposition 6.1 more delicate than that for the linear case treated by Gidas and Spruck. In addition, the proofs when $m \ge 2$ and $1 < m < 2$ are distinctly different, with the latter requiring extreme care.

Before turning to the main proof, it is convenient to introduce some further notation. Let

$$
\Omega_{\text{cr}} = \{x \in \Omega \mid \nabla u(x) = 0\}
$$

be the *critical* set of the solution $u$ in $\Omega$. Moreover, by $\hat{\Omega}^c$ we mean the complement of the set $\hat{\Omega}$ in $\Omega$, that is, $\hat{\Omega}^c=\Omega\setminus\hat{\Omega}$. In particular, $\nabla u\neq 0$ on $\Omega_{cr}^c$.

Now by the standard regularity theory for quasilinear elliptic operators, one has $u\in C^2(\Omega_{cr}^c)$ for all $m>1$. For $x\in\Omega_{cr}^c$ we can thus introduce the important Jacobian matrix

$$
\mathbf{U} = \nabla \mathbf{u}, \quad (\nabla \mathbf{u})_i^j = \partial \mathbf{u}^j / \partial x_i = \partial (|\nabla \mathbf{u}|^{m-2} u_j) / \partial x_i. \quad (6.4)
$$

It is easy to see that, for $x\in\Omega_{cr}^c$,

$$
\mathbf{U} = |\nabla \mathbf{u}|^{m-2} [\mathbf{I} + (m-2)\mathbf{w} \otimes \mathbf{w}] \mathbf{H}, \quad (6.5)
$$

where $\mathbf{w}=\nabla u/|\nabla u|$, $\mathbf{H}=\nabla^2 u$ is the Hessian of $u$, and (notation) $\mathbf{a} \otimes \mathbf{b}$ denotes the dyadic matrix with components $a_i b^j$.

By virtue of Theorem 8.1 we have $u\in W_{\text{loc}}^{2,2}(\Omega)$, and so also $\mathbf{H}\in L_{\text{loc}}^2(\Omega)$. Thus when $m\ge 2$ the three factors on the right side of (6.5) are respectively in $C^0$, $L^\infty$ and $L^2$, locally on $\Omega$ (when $m>2$ the definition of $\mathbf{w}$ on $\Omega_{cr}$ is unessential since the first factor vanishes there!); hence in this case $\mathbf{U}=\nabla \mathbf{u}$ is in fact well defined on all $\Omega$, with $\mathbf{u}\in W_{\text{loc}}^{1,2}(\Omega)$ and $\mathbf{U}\in L_{\text{loc}}^2(\Omega)$. When $m>2$ it is clear that $\mathbf{U}=0$ on $\Omega_{cr}$, but in fact also $\mathbf{U}=0$ a.e. on $\Omega_{cr}$ even when $m=2$ since $\Omega_{cr}$ is a *level* set of $\mathbf{u}$).

The derivation of Proposition 6.1 involves, at the beginning, several easy lemmas. We first have the following simple result.

LEMMA 6.1. For all $m>1$ and all $x\in\Omega_{cr}^c$,

$$
\min(1, m-1) |\nabla \mathbf{u}|^{m-2} |\nabla^2 \mathbf{u}| \le |\mathbf{U}| \le \max(1, m-1) |\nabla \mathbf{u}|^{m-2} |\nabla^2 \mathbf{u}|, \quad x \in \Omega_{cr}^c.
$$

Proof. For $x\in\Omega_{cr}^c$ we have by (6.5)

$$
\mathbf{U} = |\nabla \mathbf{u}|^{m-2} \mathbf{A} \mathbf{H}, \quad (6.6)
$$

where

$$
\mathbf{A} = \mathbf{I} + (m-2)\mathbf{w} \otimes \mathbf{w}. \quad (6.7)
$$

Clearly $\mathbf{A}$ is symmetric with eigenvalues $\lambda_1=m-1$, $\lambda_2=\dots=\lambda_n=1$.

Now using the fact that $\mathbf{H}$ is also symmetric, and that $\text{trace}(\mathbf{MN})=\text{trace}(\mathbf{NM})$ for any pair of square matrices, we get

$$
|\mathbf{U}|^2 \equiv \text{trace}(\mathbf{U}\mathbf{U}^T) = |\nabla \mathbf{u}|^{2m-4} \text{trace}(\mathbf{A}^2 \mathbf{H}^2).
$$

Diagonalizing $\mathbf{A}$ and recalling the form of its eigenvalues, we easily obtain

$$
\min(1, (m-1)^2) |\mathbf{H}|^2 \le \text{trace}(\mathbf{A}^2 \mathbf{H}^2) \le \max(1, (m-1)^2) |\mathbf{H}|^2,
$$

and Lemma 6.1 follows at once.

The following elementary result in linear algebra is preparatory for the crucial Lemma 6.3 below.

LEMMA 6.2. Let $\mathbf{S}$ be a real symmetric $(n \times n)$-matrix. Then

$$
\operatorname{trace} \mathbf{S}^2 \ge \frac{1}{n} (\operatorname{trace} \mathbf{S})^2.
$$

Proof. Let $\sigma_1, \dots, \sigma_n$ be the eigenvalues of $\mathbf{S}$. Then by diagonalization of $\mathbf{S}$ we have

$$
\operatorname{trace} \mathbf{S}^2 = \sum_{i=1}^{n} \sigma_i^2 \ge \frac{1}{n} \left( \sum_{i=1}^{n} \sigma_i \right)^2 = \frac{1}{n} (\operatorname{trace} \mathbf{S})^2
$$

by the Cauchy-Schwarz inequality.

LEMMA 6.3. For $m>1$ and $x \in \Omega_{\text{cr}}^c$ we have

$$
\operatorname{trace}(\mathbf{U}^2) - \frac{1}{n} (\operatorname{trace} \mathbf{U})^2 \ge 0. \qquad (6.8)
$$

Proof. Recall from (6.6) that $\mathbf{U}=|\nabla u|^{m-2}\mathbf{A}\mathbf{H}$, where $\mathbf{A}$ is given by (6.7). Since $\mathbf{A}$ is symmetric and positive definite (all eigenvalues positive), we can write $\mathbf{B}=\sqrt{\mathbf{A}}$. But then

$$
\operatorname{trace}[(\mathbf{A}\mathbf{H})^2] = \operatorname{trace}[\mathbf{B}(\mathbf{B}\mathbf{H}^2\mathbf{H})] = \operatorname{trace}[(\mathbf{B}\mathbf{H}^2\mathbf{H})\mathbf{B}] = \operatorname{trace}[(\mathbf{B}\mathbf{H}\mathbf{H})^2].
$$

Moreover $\mathbf{B}$ and $\mathbf{H}$ are symmetric, so that also $\mathbf{B}\mathbf{H}\mathbf{B}$ is. Hence by Lemma 6.2 we find

$$
\operatorname{trace}[(\mathbf{B}\mathbf{H}\mathbf{B})^2] \ge \frac{1}{n} [\operatorname{trace}(\mathbf{B}\mathbf{H}\mathbf{B})]^2 = \frac{1}{n} [\operatorname{trace}(\mathbf{B}^2\mathbf{H})]^2 = \frac{1}{n} [\operatorname{trace}(\mathbf{A}\mathbf{H})]^2.
$$

Combining the above relations we get

$$
\operatorname{trace}(\mathbf{U}^2) = |\nabla u|^{2m-4} \operatorname{trace}[(\mathbf{A}\mathbf{H})^2] \ge \frac{1}{n} |\nabla u|^{2m-4} [\operatorname{trace}(\mathbf{A}\mathbf{H})]^2 = \frac{1}{n} (\operatorname{trace} \mathbf{U})^2,
$$

completing the proof.

Remark. When $m \ge 2$ we have $\mathbf{U}=\nabla \mathbf{u}$, so that $\operatorname{trace} \mathbf{U}=\operatorname{div} \mathbf{u}=-f(\mathbf{u})$ (a.e.) by (1.4). But $\mathbf{U}=0$ a.e. on $\Omega_{\text{cr}}$, which thus implies

$$
f(\mathbf{u}) = 0 \quad \text{a.e. on } \Omega_{\text{cr}}.
$$

If $\mathbf{u} \ne 0$, then $\mathbf{u}$ is positive by the strong maximum principle. This gives the following regularity result.

COROLLARY. Suppose that $f(\mathbf{u})>0$ for $\mathbf{u}>0$. Then $|\Omega_{\text{cr}}|=0$ when $m \ge 2$.

That this corollary may not hold when $1<m<2$ makes many of our later proofs more difficult for this case, see §§ 7 and 8.

The following standard result in the calculus of weak derivatives will be used repeatedly in what follows, frequently without explicit mention.

LEMMA 6.4. Suppose that $a, b \in W_{\text{loc}}^{1,2}(\Omega)$, where $a$ is scalar and $b$ is either scalar or vector. Then

$$
\int ab\nabla\phi = - \int (a\nabla b + (\nabla a)b)\phi
$$

for any test function $\phi \in C_0^\infty(\Omega)$.

For the remainder of the section we shall assume that $u$ is a positive solution of (1.4), with $m \ge 2$. (The case $1 < m < 2$ will be deferred until the next section.)

Put

$$
\mathbf{v} = u^a \mathbf{u}, \qquad (6.9)
$$

where $a \in \mathbf{R}$ is a constant to be determined later, and $\mathbf{u}$ is the principal vector (6.1). By the assumption $m \ge 2$ we have $\mathbf{u} \in W_{\text{loc}}^{1,2}(\Omega)$, as already noticed. Hence also $\mathbf{v} \in W_{\text{loc}}^{1,2}(\Omega)$.

LEMMA 6.5. Suppose $m \ge 2$, and let $u$ be a positive weak solution of (1.4). Then

$$
\mathbf{u} \cdot \nabla u = |\nabla u|^m, \quad \mathbf{v} \cdot \nabla u = u^a |\nabla u|^m, \quad \operatorname{div} \mathbf{u} = -f(u). \qquad (6.10)
$$

Moreover $\mathbf{v} \in W_{\text{loc}}^{1,2}(\Omega)$ and

$$
\nabla \mathbf{v} = a u^{a-1} |\nabla u|^{m-2} \nabla u \otimes \nabla u + u^a \nabla \mathbf{u}, \quad \operatorname{div} \mathbf{v} = u^{a-1} (a |\nabla u|^m - u f(u)), \qquad (6.11)
$$

where $\mathbf{U} = \nabla \mathbf{u}$, $\mathbf{V} = \nabla \mathbf{v}$ are the Jacobian matrices of $\mathbf{u}$, $\mathbf{v}$. Finally, with standard matrix multiplication notation,

$$
\mathbf{U} \nabla u = (\nabla \mathbf{u}) \nabla u = \frac{m-1}{m} \nabla (|\nabla u|^m). \qquad (6.12)
$$

Proof. The identities (6.10), (6.11) follow by direct verification with the aid of the fundamental equation (1.4) and Lemma 6.4. For the final relation (6.12) we use the calculation

$$
\begin{aligned} (\nabla \mathbf{u}) \nabla u &= |\nabla u|^{2-m} (\nabla \mathbf{u}) \mathbf{u} = \frac{1}{2} |\nabla u|^{2-m} \nabla (|\mathbf{u}|^2) \\ &= \frac{1}{2} |\nabla u|^{2-m} \nabla (|\nabla u|^{2m-2}) = \frac{m-1}{m} \nabla (|\nabla u|^m). \end{aligned}
$$

Now define

$$
I(x) = \operatorname{trace}(\mathbf{V}^2) - \frac{1}{n} (\operatorname{div} \mathbf{v})^2.
$$

Note that $I(x) \in L_{\text{loc}}^1(\Omega)$ (for $m \ge 2$) since $\mathbf{V} \in L_{\text{loc}}^2(\Omega)$.

LEMMA 6.6. Suppose $m \ge 2$. Then $I(x) \ge 0$ a.e.

Proof. Observe that

$$
\mathbf{v} = u^a \mathbf{u} = s^{-2} |\nabla(u^s)|^{m-2} \nabla(u^s) \equiv \hat{\mathbf{u}},
$$

where $s=1+a/(m-1)$, $a \ne 1-m$, while

$$
\mathbf{v} = u^a \mathbf{u} = |\nabla(\ln u)|^{m-2} \nabla(\ln u)
$$

if $a=1-m$. For points $x \in \Omega_{\text{cr}}^c$ the conclusion now follows directly from Lemma 6.3 applied to $\hat{\mathbf{u}}$ and $\hat{\mathbf{U}} = \nabla \hat{\mathbf{u}}$ rather than to $\mathbf{u}$ and $\mathbf{U}$, with the obvious changes if $a=1-m$. (Note here that $\operatorname{div} \hat{\mathbf{u}} = \operatorname{trace} \hat{\mathbf{U}}$ a.e. on $\Omega_{\text{cr}}^c$.) When $x \in \Omega_{\text{cr}}$, then $\mathbf{U} = \mathbf{V} = 0$ a.e., and again the conclusion holds.

Let $b \in \mathbf{R}$. Consider the vector field

$$
\boldsymbol{\omega} = \omega(x) = \left( \mathbf{v} \cdot \nabla \mathbf{v} - \frac{1}{n} \mathbf{v} \operatorname{div} \mathbf{v} \right) u^b \quad (6.13)
$$

(the expression $\mathbf{v} \cdot \nabla \mathbf{v}$ is interpreted as the vector $(\mathbf{v} \cdot \nabla)\mathbf{v}$ or equally as the matrix product $\mathbf{v}\mathbf{V}$). Also put

$$
\psi = u^{b+2a-1} \{ A f(u) + \hat{A} u f'(u) \} |\nabla u|^m + B u^{b+2a-2} |\nabla u|^{2m} + C \operatorname{div} (u^{b+2a-1} |\nabla u|^m \mathbf{u}) \quad (6.14)
$$

where

$$
\begin{aligned} A &= \left(1 - \frac{1}{m^*}\right) b, & \hat{A} &= -\frac{n-1}{n}, & B &= -\frac{m-1}{m}(b+2a-1)b - \frac{n-1}{n}a^2, \\ C &= \frac{n-1}{n}a + \frac{m-1}{m}b. \end{aligned} \quad (6.15)
$$

Clearly $\boldsymbol{\omega}$ and $\psi$ are in $L_{\text{loc}}^2$ (in fact, the first three terms in $\psi$ are continuous). The coefficients $A, \hat{A}, B$ in (6.15) are the same as in (6.3) provided $b$ and $a$ are chosen appropriately, see (6.26) below.

The next result is the key to Proposition 6.1 in the case $m \ge 2$.

PROPOSITION 6.2. Suppose $m \ge 2$ and let $\boldsymbol{\omega}$ and $\psi$ be given as above. Then $\operatorname{div} \boldsymbol{\omega} = u^b I(x) + \psi$ in the sense of distributions, that is,

$$
- \int \boldsymbol{\omega} \cdot \nabla \phi = \int (u^b I(x) + \psi) \phi \quad \text{for all } \phi \in C_0^\infty(\mathbf{R}^n). \quad (6.16)
$$

*Proof.* By virtue of the identities (6.10) and (6.11), and Lemma 6.4, we have

$$
\begin{align*}
I_0 &\equiv \int u^b (\operatorname{div} \mathbf{v}) \mathbf{v} \cdot \nabla \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v})^2 \phi - b \int u^{b-1} (\operatorname{div} \mathbf{v}) \mathbf{v} \cdot \nabla u \phi - \int u^b \mathbf{v} \cdot \nabla [\operatorname{div} \mathbf{v}] \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v})^2 \phi - b \int u^{b+2a-2} [a|\nabla u|^m - uf(u)] |\nabla u|^m \phi \\
&\quad - \int u^{b+a} \mathbf{u} \cdot \nabla [u^{a-1} (a|\nabla u|^m - uf(u))] \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v})^2 \phi + \int u^{b+2a-1} (A_0 f(u) + uf'(u)) |\nabla u|^m \phi \\
&\quad + B_0 \int u^{b+2a-2} |\nabla u|^{2m} \phi + C_0 \int u^{b+a} \mathbf{u} \cdot \nabla (u^{a-1} |\nabla u|^m) \phi,
\end{align*}
\tag{6.17}
$$

where

$$
A_0 = a+b, \quad B_0 = -ab, \quad C_0 = -a. \tag{6.18}
$$

We have next, by (6.10) and (6.11),

$$
\begin{align*}
- \int u^b (\mathbf{v} \cdot \nabla \mathbf{v}) \cdot \nabla \phi &= -a \int u^{b+a-1} (\mathbf{v} \cdot \nabla u) (\mathbf{u} \cdot \nabla \phi) - \int u^{b+a} (\mathbf{v} \cdot \nabla \mathbf{u}) \cdot \nabla \phi \\
&\equiv I_1 + I_2.
\end{align*}
$$

With the help of (6.10) one finds that

$$
\begin{align*}
\operatorname{div}(u^{b+a-1}(\mathbf{v} \cdot \nabla u) \mathbf{u}) &= \operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}) \\
&= u^{b+2a-1} \mathbf{u} \cdot \nabla (|\nabla u|^m) - u^{b+2a-1} f(u) |\nabla u|^m \\
&\quad + (b+2a-1) u^{b+2a-2} |\nabla u|^{2m}.
\end{align*}
$$

This gives the evaluation

$$
I_1 = A_1 \int u^{b+2a-1} f(u) |\nabla u|^m + B_1 \int u^{b+2a-2} |\nabla u|^{2m} + C_1 \int u^{b+2a-1} \mathbf{u} \cdot \nabla (|\nabla u|^m) \quad (6.19)
$$

where

$$
A_1 = -a, \quad B_1 = (b+2a-1)a, \quad C_1 = a. \tag{6.20}
$$

The integral $I_2$ is more difficult, involving a delicate interchange of order of differentiation. That is, in rewriting $I_2$ we should like to use the relation (in an obvious subscript notation)

$$
\nabla_i \nabla_j u^i = \nabla_j \nabla_i u^i = f'(u) \nabla_j u.
$$

This is only a formal calculation, however, except in the regular case $m=2$, and consequently it is necessary to follow a somewhat roundabout procedure. For $h>0$ and $h^i=h\mathbf{e}_i$, $i=1, \dots, n$, let $\mathbf{U}_h$ be the matrix with components

$$
\{\mathbf{U}_h\}_i^j = h^{-1}\{|\nabla u(x+h^i)|^{m-2}\nabla_j u(x+h^i) - |\nabla u(x)|^{m-2}\nabla_j u(x)\}. \quad (6.21)
$$

Since $\mathbf{u} \in W_{\text{loc}}^{1,2}(\Omega)$, as noted just after (6.5), it is standard that $\mathbf{U}_h \to \nabla \mathbf{u}$ in $L_{\text{loc}}^2$ as $h \to 0$, see (6.1). Hence we can write

$$
I_2 = - \lim_{h \to 0} \int u^{b+a} (\mathbf{v}\mathbf{U}_h) \cdot \nabla \phi.
$$

In turn, by Lemma 6.4,

$$
I_2 = \lim_{h \to 0} \left\{ \int (\mathbf{v}\mathbf{U}_h) \cdot \nabla (u^{b+a}) \phi + \int u^{b+a} \operatorname{trace}(\mathbf{V}\mathbf{U}_h) \phi + \int u^{b+a} \mathbf{v} \cdot (\operatorname{div} \mathbf{U}_h^T) \phi \right\},
$$

the last term understood in the distribution sense. Now by (6.10)–(6.12), with convergence in the sense of $L_{\text{loc}}^2(\Omega)$,

$$
(\mathbf{v}\mathbf{U}_h) \cdot \nabla (u^{b+a}) \to (b+a)u^{b+a-1}\mathbf{v} \cdot ((\nabla \mathbf{u})\nabla u) = \frac{m-1}{m}(b+a)u^{b+2a-1}\mathbf{u} \cdot \nabla (|\nabla u|^m)
$$

and

$$
\begin{aligned} \operatorname{trace}(\mathbf{V}\mathbf{U}_h) &\to \operatorname{trace}(\mathbf{V}\nabla \mathbf{u}) = u^{-a} \operatorname{trace}(\mathbf{V}^2) - au^{-1} \mathbf{u} \cdot (\mathbf{V}\nabla \mathbf{u}) \\ &= u^{-a} \operatorname{trace}(\mathbf{V}^2) - a^2 u^{a-2} |\nabla u|^{2m} - \frac{m-1}{m} au^{a-1} \mathbf{u} \cdot \nabla (|\nabla u|^m). \end{aligned}
$$

Finally, for the third term in the limit, we assert that (uniformly on compact subsets of $\Omega$)

$$
\operatorname{div} \mathbf{U}_h^T \to -f'(u)\nabla u. \quad (6.22)
$$

Assuming (6.22) for the moment and then combining the previous four lines, we get

$$
\begin{aligned} I_2 = \int u^{-a} \operatorname{trace}(\mathbf{V}^2) - \int u^{b+2a} f'(u) |\nabla u|^m \phi & \\ + B_2 \int u^{b+2a-2} |\nabla u|^{2m} \phi + C_2 \int u^{b+2a-1} \mathbf{u} \cdot \nabla (|\nabla u|^m) \phi, \end{aligned} \quad (6.23)
$$

where

$$
B_2 = -a^2, \quad C_2 = \frac{m-1}{m} b. \quad (6.24)
$$

It is clear that the left side of (6.16) has the form

$$
\frac{I_0}{n} + I_1 + I_2,
$$

where $I_0, I_1, I_2$ have been calculated above, see (6.17), (6.19), (6.23). The terms in $I_0, I_1, I_2$ with coefficients $C_0, C_1, C_2$ can be put in pure divergence form, as required for the function $\psi$. In particular, making use of (6.10) we have the following identity for rewriting the indicated term in $I_0$:

$$
\operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}) = u^{b+a} \mathbf{u} \cdot \nabla (u^{a-1} |\nabla u|^m) - u^{b+2a-1} f(u) |\nabla u|^m \\ + (b+a) u^{b+2a-1} |\nabla u|^{2m},
$$

while, for the corresponding terms in $I_1, I_2$,

$$
\operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}) = u^{b+2a-1} \mathbf{u} \cdot \nabla (|\nabla u|^m) - u^{b+2a-1} f(u) |\nabla u|^m \\ + (b+2a-1) u^{b+2a-2} |\nabla u|^{2m}.
$$

With the help of these identities and the previous calculations for $I_0, I_1, I_2$ we are lead to the main formula for $\psi$, with coefficients

$$
\begin{aligned} A &= \frac{A_0}{n} + A_1 + \frac{C_0}{n} + C_1 + C_2, & \hat{A} &= -1 + \frac{1}{n}, \\ B &= \frac{B_0}{n} + B_1 + B_2 - (b+a) \frac{C_0}{n} - (b+2a-1)(C_1 + C_2), \\ C &= \frac{C_0}{n} + C_1 + C_2, \end{aligned}
$$

or equivalently, for $A$ and $B$,

$$
\begin{aligned} A &= \frac{A_0}{n} + A_1 + C, \\ B &= \frac{B_0}{n} + B_1 + B_2 + (a-1) \frac{C_0}{n} - (b+2a-1)C. \end{aligned}
$$

Using (6.18), (6.20) and (6.24) together with a little arithmetic, we then obtain the claimed values (6.15) for the coefficients $A, \hat{A}, B, C$. This completes the proof of Proposition 6.2, once we have shown (6.22).

*Proof of (6.22).* Apply finite differences to (1.5) to obtain

$$
\operatorname{div} \mathbf{U}_h^T = \mathbf{y}, \qquad (6.25)
$$

where $\mathbf{y}$ is the vector with components

$$
y^j = c^j(x) \frac{u(x+h^j) - u(x)}{h}, \quad j = 1, 2, \dots, n,
$$

and

$$
c^j(x) = - \int_0^1 f'(u(x) + t(u(x+h^j) - u(x))) dt.
$$

The result now follows at once since $h^{-1}(u(x+h^j) - u(x)) \to \nabla u$ and $c^j \to -f'(u)$ as $h \to 0$, uniformly on compact subsets of $\Omega$.

We now determine the parameters $a$ and $b$. To motivate our choice, let us first seek the maximum value of $b$, and hence $A$, subject to the condition $B=0$. Writing $b=b(a)$ and differentiating the relation

$$
B(a, b) = 0
$$

with respect to $a$, we obtain, when $b'(a)=0$,

$$
2a \frac{n-1}{n} + 2b \frac{m-1}{m} = 0.
$$

Solving the last two equations for $a$ and $b$ gives

$$
a = -\frac{m-1}{m} m^*, \quad b = \frac{n-1}{n} m^*,
$$

where the critical exponent $m^*$ was defined at the beginning of the section. In fact, these values for $a$ and $b$ are not optimal, since in §3 we need to have $B>0$. Thus we make the modified choice

$$
a = -\frac{m-1}{m} m^*, \quad b = \frac{n-1}{n} m^* - d, \qquad (6.26)
$$

where $d$ is a given parameter which will eventually be chosen small and positive. With these values for $a$ and $b$, the constants $A, \hat{A}, B$ in (6.15) take the final form given in (6.3), while

$$
C = \frac{C_0}{n} + C_1 + C_2 = \frac{n-1}{n} a + \frac{m-1}{m} b
$$

by (6.18), (6.20), (6.24).

We can now complete the proof of Proposition 6.1 for the case $m \ge 2$. First, from (6.13) and (6.11),

$$
\omega = u^{b+2a} \mathbf{u} \cdot \nabla \mathbf{u} + a \frac{n-1}{n} u^{b+2a-1} |\nabla u|^m \mathbf{u} + \frac{1}{n} u^{b+2a} f(u) \mathbf{u}.
$$

By means of (reverse) integration by parts and (6.10), one gets

$$
\begin{aligned} - \int u^{b+2a} (\mathbf{u} \cdot \nabla \mathbf{u}) \cdot \nabla \phi &= \int (\mathbf{u} \cdot \nabla (u^{b+2a})) \mathbf{u} \cdot \nabla \phi + \int u^{b+2a} \operatorname{div} \mathbf{u} \, \mathbf{u} \cdot \nabla \phi + \int u^{b+2a} \mathbf{u} \nabla^2 \phi \, \mathbf{u} \\ &= (b+2a) \int u^{b+2a-1} |\nabla u|^m \mathbf{u} \cdot \nabla \phi \qquad (6.27) \\ &\quad - \int u^{b+2a} f(u) \mathbf{u} \cdot \nabla \phi + \int u^{b+2a} \{\mathbf{u} \nabla^2 \phi \, \mathbf{u}\} \end{aligned}
$$

(in a corresponding calculation at this stage of the proof Gidas and Spruck use a different partial integration). In turn

$$
- \int \omega \cdot \nabla \phi = \left( \frac{n+1}{n} a + b \right) \int u^{b+2a-1} |\nabla u|^m \mathbf{u} \cdot \nabla \phi \\ - \frac{n+1}{n} \int u^{b+2a} f(u) \mathbf{u} \cdot \nabla \phi + \int u^{b+2a} \{ \mathbf{u} \nabla^2 \phi \mathbf{u} \}.
$$

By Proposition 6.2 and Lemma 6.6 the left side of the previous relation is greater than or equal to $\int \psi \phi$ for all non-negative test functions $\phi$. Moreover the integral of the last term in the expression (6.14) for $\psi$ can be rewritten using integration by parts, namely

$$
C \int \operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}) \phi = -C \int u^{b+2a-1} |\nabla u|^m \mathbf{u} \cdot \nabla \phi. \quad (6.28)
$$

The required conclusion (6.2), (6.3) now follows, with

$$
\hat{D} = C + \left( \frac{n+1}{n} a + b \right) = 2a + \frac{2m-1}{m} b = \left( 2 - \frac{m_*}{m} \right) - \left( 2 - \frac{1}{m} \right) d
$$

and $b+2a=2-m_*-d$.

*Remarks.* It is obviously possible to state Proposition 6.1 in a slightly more general form, without specifying $a$ and $b$.

In the present case $m \ge 2$, equality can be attained in (6.2) by adding the term $\int u^l I(x) \phi$ to the left-hand side. Whether equality can hold in (6.2) itself is an open question.

## 7. A general integral inequality II

The proof for Proposition 6.1 given in §6 for the case $m \ge 2$ fails when $1 < m < 2$, since the Jacobian matrices $\nabla \mathbf{u}$ and $\nabla \mathbf{v}$ are singular on the critical set

$$
\Omega_{\text{cr}} = \{ x \in \Omega \mid \nabla u(x) = 0 \}.
$$

Because we cannot be assured that this set is empty when $1 < m < 2$, or even of measure zero, the previous proof becomes only formal. Moreover when $1 < m < 2$ the function $I(x)$ in Lemma 6.6 cannot be defined on the critical set $\Omega_{\text{cr}}$, creating a further complication. All this forces us, when $1 < m < 2$, to modify the previous argument in essential ways.

As in §6, definitions (6.1) and (6.9), we continue to write

$$
\mathbf{u} = |\nabla u|^{m-2} \nabla u, \quad \mathbf{v} = u^a \mathbf{u}.
$$

The matrices $\nabla \mathbf{u}$, $\nabla \mathbf{v}$, though now having no meaning on $\Omega_{\text{cr}}$, are of course well defined and continuous on $\Omega_{\text{cr}}^c$. It is then convenient to redefine $\mathbf{U}$ and $\mathbf{V}$, for $1<m<2$, as

$$
\mathbf{U} = \begin{cases} \nabla \mathbf{u}, & x \in \Omega_{\text{cr}}^c, \\ 0, & x \in \Omega_{\text{cr}}, \end{cases} \quad \mathbf{V} = \begin{cases} \nabla \mathbf{v}, & x \in \Omega_{\text{cr}}^c, \\ 0, & x \in \Omega_{\text{cr}}. \end{cases} \quad (7.1)
$$

With these redefinitions, Lemma 6.5 continues to hold, with the first relation of (6.11) and also (6.12) in the slightly modified form

$$
\mathbf{V} = au^{a-1} |\nabla u|^{m-2} \nabla u \otimes \nabla u + u^a \mathbf{U}, \quad \mathbf{U} \nabla u = \frac{m-1}{m} \nabla (|\nabla u|^m); \quad (7.2)
$$

the second relation of (6.11), however, remains unchanged in view of the calculation

$$
\begin{aligned} \int \mathbf{v} \cdot \nabla \phi &= \int u^a \mathbf{u} \cdot \nabla \phi = \int \mathbf{u} \cdot [\nabla (u^a \phi) - au^{a-1} (\nabla u) \phi] \\ &= \int (u^a f(u) - au^{a-1} |\nabla u|^m) \phi. \end{aligned}
$$

For fixed $0<\varepsilon<1$ we put

$$
\mathbf{u}_{\varepsilon} = |\nabla u|_{\varepsilon}^{m-2} \nabla u, \quad |\nabla u|_{\varepsilon} = \max\{|\nabla u|, \varepsilon\}.
$$

Clearly $\mathbf{u}_{\varepsilon}$ is in $C(\Omega)$ and $\nabla \mathbf{u}_{\varepsilon}$ in $L_{\text{loc}}^2(\Omega)$ by Proposition 8.1. The following technical lemma will be important in the sequel. Its proof will be deferred until §8, Lemma 8.4.

LEMMA 7.1. Let $\mathbf{U}_h$ be the (matrix) difference quotient introduced in the previous section, see (6.21). Then as $h \to 0$,

$$
\begin{aligned} \mathbf{u}_{\varepsilon} \mathbf{U}_h &\to \mathbf{u}_{\varepsilon} \mathbf{U} && \text{weakly in } L_{\text{loc}}^2(\Omega), \\ \nabla \mathbf{u}_{\varepsilon} \mathbf{U}_h &\to \nabla \mathbf{u}_{\varepsilon} \mathbf{U} && \text{weakly in } L_{\text{loc}}^1(\Omega). \end{aligned}
$$

Remark. These relations are obvious when $m \ge 2$, since $\mathbf{U}_h \to \nabla \mathbf{u}$ in $L_{\text{loc}}^2$ and $\nabla \mathbf{u} = \mathbf{U}$. They are far from trivial when $m<2$.

Now proceeding in analogy with the demonstration in §6, we set

$$
\mathbf{v}_{\varepsilon} = u^a \mathbf{u}_{\varepsilon}, \quad \mathbf{V}_{\varepsilon} = \nabla \mathbf{v}_{\varepsilon}
$$

and

$$
I_{\varepsilon}(x) = \operatorname{trace}(\mathbf{V}_{\varepsilon} \mathbf{V}) - \frac{1}{n} \operatorname{div} \mathbf{v}_{\varepsilon} \operatorname{div} \mathbf{v}. \quad (7.3)
$$

From Proposition 8.1 it is evident that $\mathbf{V}$, $\mathbf{V}_{\varepsilon}$ and $\operatorname{div} \mathbf{v}_{\varepsilon}$ are in $L_{\text{loc}}^2(\Omega)$. Hence $I_{\varepsilon}(x) \in L_{\text{loc}}^1(\Omega)$. The proof of the next result will be deferred until the end of the section.

LEMMA 7.2. Let $\Omega_\varepsilon=\{x\in\Omega\mid 0<|\nabla u|<\varepsilon\}$. Then, for all suitably small $\varepsilon>0$,

$$
I_{\varepsilon}(x) \ge \begin{cases} -u^{2a-2}(1+uf(u))^2/8(m-1), & x \in \Omega_{\varepsilon}, \\ 0, & x \in \Omega_{\varepsilon}^{c}. \end{cases}
$$

Now let $b\in\mathbf{R}$, and consider the vector and scalar fields $\boldsymbol{\omega}_\varepsilon=\boldsymbol{\omega}_\varepsilon(x)$ and $\psi_\varepsilon=\psi_\varepsilon(x)$ given by

$$
\boldsymbol{\omega}_\varepsilon = \left( \mathbf{v}_\varepsilon \mathbf{V} - \frac{1}{n} \mathbf{v}_\varepsilon \operatorname{div} \mathbf{v} \right) u^b \quad (7.4)
$$

and

$$
\psi_\varepsilon = u^{b+2a-1} \{ \bar{A}f(u) + \hat{A}uf'(u) \} \Gamma_\varepsilon + \tilde{A}u^{b+2a-1} |\nabla u|^m \operatorname{div} \mathbf{u}_\varepsilon + B u^{b+2a-2} |\nabla u|^m \Gamma_\varepsilon + C \operatorname{div} (u^{b+2a-1} |\nabla u|^m \mathbf{u}_\varepsilon), \quad (7.5)
$$

where $\Gamma_\varepsilon=\mathbf{u}_\varepsilon \cdot \nabla u=|\nabla u|_\varepsilon^{m-2} |\nabla u|^2$,

$$
\bar{A} = A - \tilde{A}, \quad \tilde{A} = \frac{a}{n} - \frac{m-1}{m} b \quad (7.6)
$$

and $A, \hat{A}, B, C$ are given by (6.15).

PROPOSITION 7.1. Let $\boldsymbol{\omega}_\varepsilon$ be defined by (7.4). Then

$$
\operatorname{div} \boldsymbol{\omega}_\varepsilon = \psi_\varepsilon + u^b I_\varepsilon(x) + O(\varepsilon^{2(m-1)})
$$

in the sense of distributions, that is,

$$
- \int \boldsymbol{\omega}_\varepsilon \cdot \nabla \phi = \int (\psi_\varepsilon + u^b I_\varepsilon(x)) \phi + O(\varepsilon^{2(m-1)}) \quad \text{for all } \phi \in C_0^\infty(\mathbf{R}^n). \quad (7.7)
$$

Proof. By virtue of (1.4), the identities (7.2) and (6.12), and Lemma 6.5, we have

$$
\begin{align*}
I_0 &= \int u^b (\operatorname{div} \mathbf{v}) \mathbf{v}_\varepsilon \cdot \nabla \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v}_\varepsilon) (\operatorname{div} \mathbf{v}) \phi - b \int u^{b-1} (\operatorname{div} \mathbf{v}) \mathbf{v}_\varepsilon \cdot \nabla u \phi - \int u^b \mathbf{v}_\varepsilon \cdot \nabla [\operatorname{div} \mathbf{v}] \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v}_\varepsilon) (\operatorname{div} \mathbf{v}) \phi - b \int u^{b+2a-2} (a |\nabla u|^m - u f(u)) \Gamma_\varepsilon \phi \\
&\quad - \int u^{b+a} \mathbf{u}_\varepsilon \cdot \nabla [u^{a-1} (a |\nabla u|^m - u f(u))] \phi \\
&= - \int u^b (\operatorname{div} \mathbf{v}_\varepsilon) (\operatorname{div} \mathbf{v}) \phi + \int u^{b+2a-1} (A_0 f(u) + u f'(u)) \Gamma_\varepsilon \phi \\
&\quad + B_0 \int u^{b+2a-2} |\nabla u|^m \Gamma_\varepsilon \phi + C_0 \int u^{b+a} \mathbf{u}_\varepsilon \cdot \nabla (u^{a-1} |\nabla u|^m) \phi, \tag{7.8}
\end{align*}
$$

where

$$
A_0 = a+b, \quad B_0 = -ab, \quad C_0 = -a. \tag{7.9}
$$

Next, by (7.2) again,

$$
\begin{aligned}
- \int u^b (\mathbf{v}_\varepsilon \cdot \mathbf{V}) \cdot \nabla \phi &= -a \int u^{b+a-1} (\mathbf{v}_\varepsilon \cdot \nabla u) (\mathbf{u} \cdot \nabla \phi) - \int u^{b+2a} \mathbf{v}_\varepsilon \mathbf{U} \cdot \nabla \phi \\
&\equiv I_1 + I_2.
\end{aligned}
$$

With the help of (1.4) one finds that

$$
\begin{aligned}
\operatorname{div}(u^{b+a-1}(\mathbf{v}_\varepsilon \cdot \nabla u)\mathbf{u}) &= \operatorname{div}(u^{b+2a-1}\Gamma_\varepsilon \mathbf{u}) \\
&= u^{b+2a-1}\mathbf{u} \cdot \nabla \Gamma_\varepsilon - u^{b+2a-1}f(u)\Gamma_\varepsilon + (b+2a-1)u^{b+2a-2}|\nabla u|^m \Gamma_\varepsilon.
\end{aligned}
$$

This gives the evaluation

$$
I_1 = A_1 \int u^{b+2a-1} f(u) \Gamma_\varepsilon + B_1 \int u^{b+2a-2} |\nabla u|^m \Gamma_\varepsilon + C_1 \int u^{b+2a-1} \mathbf{u} \cdot \nabla \Gamma_\varepsilon, \quad (7.10)
$$

where

$$
A_1 = -a, \quad B_1 = (b+2a-1)a, \quad C_1 = a. \tag{7.11}
$$

The term $I_2$ is more difficult, involving a delicate limit calculation. By Lemma 7.1 (i),

$$
\begin{aligned}
I_2 &= \lim_{h \to 0} \int u^{b+a} \mathbf{v}_\varepsilon \mathbf{U}_h \cdot \nabla \phi \\
&= \lim_{h \to 0} \left\{ \int (\mathbf{v}_\varepsilon \mathbf{U}_h) \cdot \nabla (u^{b+a}) \phi + \int u^{b+a} \operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{U}_h) \phi + \int u^{b+a} \mathbf{v}_\varepsilon \cdot \operatorname{div}(\mathbf{U}_h^T) \phi \right\}.
\end{aligned}
$$

We deal separately with the three terms on the right. By Lemma 7.1 (i) and (7.2) we get

$$
(\mathbf{v}_\varepsilon \mathbf{U}_h) \cdot \nabla (u^{b+a}) = (b+a) u^{b+a-1} \mathbf{v}_\varepsilon \mathbf{U}_h \cdot \nabla u \to \frac{m-1}{m} (b+a) u^{b+2a-1} \mathbf{u}_\varepsilon \cdot \nabla (|\nabla u|^m)
$$

weakly in $L^2$.

Next,

$$
\mathbf{V}_\varepsilon = \nabla \mathbf{v}_\varepsilon = au^{a-1} \nabla u \otimes \mathbf{u}_\varepsilon + u^a \nabla \mathbf{u}_\varepsilon,
$$

where we note that $\mathbf{V}_\varepsilon=0$ a.e. on $\Omega_{cr}$ since $\nabla^2 u=0$ a.e. on this set (that is, $\nabla(\nabla u)=0$ a.e. on the level set $\Omega_{cr}$). Therefore, again using Lemma 7.1 and (7.2), we find as $h \to 0$

$$
\begin{aligned}
\operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{U}_h) &\to \operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{U}) \\
&= u^{-a} \operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{V}) - au^{-1} \mathbf{u} \cdot (\nabla \mathbf{v}_\varepsilon \nabla u) \\
&= u^{-a} \operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{V}) - a^2 u^{a-2} \Gamma_\varepsilon |\nabla u|^m - \frac{m-1}{m} au^{a-1} \mathbf{u}_\varepsilon \cdot \nabla (|\nabla u|^m) \\
&\quad + O(\varepsilon^{2(m-1)} \nabla^2 u)
\end{aligned}
$$

weakly in $L^1$; the last step arises from direct differentiation together with the observation that

$$
\mathbf{u} \cdot \nabla \mathbf{u}_{\varepsilon} \nabla u = \begin{cases} \frac{m-1}{m} au^{a-1} \mathbf{u}_{\varepsilon} \cdot \nabla (|\nabla u|^m), & x \in \Omega_{\varepsilon}^c, \\ O(\varepsilon^{m-2} |\nabla u|^m \nabla^2 u) = O(\varepsilon^{2(m-1)} \nabla^2 u), & x \in \Omega_{\varepsilon}. \end{cases}
$$

Finally, for the third term in the limit we have, exactly as in (6.22),

$$
\operatorname{div} \mathbf{U}_h^T \to -f'(u) \nabla u. \qquad (7.12)
$$

Combining the previous lines yields

$$
I_2 = \int u^b \operatorname{trace}(\mathbf{V}_\varepsilon \mathbf{V}) - \int u^{b+2a} f'(u) \Gamma_\varepsilon \phi + B_2 \int u^{b+2a-2} \Gamma_\varepsilon |\nabla u|^m \phi + C_2 \int u^{b+2a-1} \mathbf{u}_\varepsilon \cdot \nabla (|\nabla u|^m) \phi + O(\varepsilon^{2(m-1)}) \quad (7.13)
$$

(since $\nabla^2 u \in L_{\text{loc}}^2(\Omega)$), where

$$
B_2 = -a^2, \quad C_2 = \frac{m-1}{m} b. \qquad (7.14)
$$

It is clear that the left side of (7.7) has the form

$$
\frac{I_0}{n} + I_1 + I_2,
$$

where $I_0, I_1, I_2$ have been calculated above, see (7.8), (7.10), (7.13). The terms in $I_0, I_1, I_2$ with coefficients $C_0, C_1, C_2$ can be rewritten in pure divergence form, as required for the function $\psi_\varepsilon$. In particular, making use of (1.4) and differentiation, we have the following identity for rewriting the indicated term in $I_0$:

$$
\operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}_\varepsilon) = u^{b+a} \mathbf{u}_\varepsilon \cdot \nabla (u^{a-1} |\nabla u|^m) + u^{b+2a-1} \operatorname{div} \mathbf{u}_\varepsilon |\nabla u|^m \\ + (b+a) u^{b+2a-1} \Gamma_\varepsilon |\nabla u|^m,
$$

while for the corresponding terms in $I_1$ and $I_2$, we have

$$
\operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}_\varepsilon) = \operatorname{div}(u^{b+2a-1} \Gamma_\varepsilon \mathbf{u}) \\ = u^{b+2a-1} \mathbf{u} \cdot \nabla \Gamma_\varepsilon - u^{b+2a-1} f(u) \Gamma_\varepsilon + (b+2a-1) u^{b+2a-2} |\nabla u|^m \Gamma_\varepsilon
$$

and

$$
\operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}_\varepsilon) = u^{b+2a-1} \mathbf{u}_\varepsilon \cdot \nabla (|\nabla u|^m) + u^{b+2a-1} \operatorname{div} \mathbf{u}_\varepsilon |\nabla u|^m \\ + (b+2a-1) u^{b+2a-2} \Gamma_\varepsilon |\nabla u|^m.
$$

With the help of these identities and the previous calculations for $I_0, I_1, I_2$ we are lead (after a little arithmetic) to the main formula for $\psi_\varepsilon$, with coefficients given in (7.6) and (6.15). This completes the proof of Proposition 7.1.

PROPOSITION 7.2. Suppose $m \in (1, 2)$. Let $u$ be a positive weak solution $f$ of (1.4) and $\phi \in C_0^\infty(\Omega)$ a non-negative cut-off function. Then

$$
\begin{aligned}
& \int u^{b+2a-1} \{Af(u) + \hat{A}uf'(u)\} |\nabla u|^m \phi + B \int u^{b+2a-2} |\nabla u|^{2m} \phi \\
& \le \int u^{b+2a-1} \{Duf(u) + \hat{D}|\nabla u|^m\} \mathbf{u} \cdot \nabla \phi + \frac{1}{2} \int u^{b+2a} \{\mathbf{u} \nabla^2 \phi \mathbf{u}\},
\end{aligned} 
\quad (7.15)
$$

where $A$, $\hat{A}$ and $B$ are given in (6.15) and

$$
D = -\frac{n+1}{n}, \quad \hat{D} = 2a + \frac{2m-1}{m} b. \quad (7.16)
$$

Proof. We shall obtain (7.15) by letting $\varepsilon \to 0$ in (7.7). In preparation for this limit process, observe first by (7.2) that

$$
\omega_{\varepsilon} = u^{b+2a} \mathbf{u}_{\varepsilon} \mathbf{U} + a \frac{n-1}{n} u^{b+2a-1} |\nabla u|^m \mathbf{u}_{\varepsilon} + \frac{1}{n} u^{b+2a} f(u) \mathbf{u}_{\varepsilon}. \quad (7.17)
$$

As in §6, equation (6.27), we evaluate the first term on the right in (7.17):

$$
\begin{aligned}
- \int u^{b+2a} \mathbf{u}_{\varepsilon} \mathbf{U} \cdot \nabla \phi &= (b+2a) \int u^{b+2a-1} |\nabla u|^m \mathbf{u}_{\varepsilon} \cdot \nabla \phi \\
&\quad + \int u^{b+2a} \operatorname{div} \mathbf{u}_{\varepsilon} \mathbf{u} \cdot \nabla \phi + \int u^{b+2a} \{\mathbf{u}_{\varepsilon} \nabla^2 \phi \mathbf{u}\}.
\end{aligned} 
\quad (7.18)
$$

This cannot, however, be obtained as in §6 by a direct integration by parts, since the matrix $\mathbf{U}$ is not a true gradient. Nevertheless, by approximating $\mathbf{U}$ by $\mathbf{U}_h$ and using Lemma 7.1 (i) it is clear that (7.18) is valid.

Finally, a transformation of the last term in the formula for $\psi_{\varepsilon}$, see the corresponding relation (6.28), gives

$$
C \int \operatorname{div}(u^{b+2a-1} |\nabla u|^m \mathbf{u}_{\varepsilon}) \phi = -C \int u^{b+2a-1} |\nabla u|^m \mathbf{u}_{\varepsilon} \cdot \nabla \phi. \quad (7.19)
$$

With the help of (7.17)–(7.19) one may now carry out the limit as $\varepsilon$ approaches zero in (7.5), (7.7). Since $\mathbf{u}_{\varepsilon}$ goes to $\mathbf{u}$ pointwise and boundedly, and similarly $\Gamma_{\varepsilon}$ goes to $|\nabla u|^m$, the only difficulty then resides in the limiting value for the quantity $\operatorname{div} \mathbf{u}_{\varepsilon}$, which appears both in (7.5) and (7.18). Corresponding to the term in (7.5), however, we have

$$
|\nabla u|^m \operatorname{div} \mathbf{u}_{\varepsilon} = \begin{cases} -|\nabla u|^m f(u), & x \in \Omega_{\varepsilon}^c, \\ \varepsilon^{m-2} |\nabla u|^m \Delta u, & x \in \Omega_{\varepsilon}, \end{cases} \quad (7.20)
$$

while for the term in (7.18),

$$
\mathbf{u} \operatorname{div} \mathbf{u}_{\varepsilon} = \begin{cases} -\mathbf{u}f(u), & x \in \Omega_{\varepsilon}^{c}, \\ \varepsilon^{m-2} \nabla u |\nabla u|^{m-2} \Delta u, & x \in \Omega_{\varepsilon}. \end{cases} \quad (7.21)
$$

Letting $\varepsilon \to 0$, and using the fact that $\Omega_{\varepsilon}$ then converges to the empty set, we see that the right side of (7.20) converges pointwise in $\Omega$ to $-|\nabla u|^m f(u)$. Moreover, by Proposition 8.1, it is uniformly bounded in $L_{\text{loc}}^2(\Omega)$. Hence the convergence also holds weakly in $L_{\text{loc}}^2(\Omega)$; see the remark after Lemma 8.3.

For the second term on the right side of (7.21) we have the estimate

$$
|\varepsilon^{m-2} \nabla u |\nabla u|^{m-2} \Delta u| \le \varepsilon^{m-1} |\nabla u|^{m-2} |\nabla^2 u| x \in \Omega_{\varepsilon}.
$$

By the second part of Proposition 8.1, it now follows as for (7.20) that the right side of (7.21) converges weakly in $L_{\text{loc}}^2(\Omega)$ to $-\mathbf{u}f(u)$.

In summary, both the quantities $|\nabla u|^m \operatorname{div} \mathbf{u}_\varepsilon$ and $\mathbf{u} \operatorname{div} \mathbf{u}_\varepsilon$ converge weakly in $L_{\text{loc}}^2(\Omega)$, respectively to $-|\nabla u|^m f(u)$ and $-\mathbf{u}f(u)$.

The resulting limit (7.15) is now easily obtained with the help of a little arithmetic, provided that the term $u^b I_\varepsilon$ in (7.7) is *non-negative*, or at least *non-negative in the limit* as $\varepsilon \to 0$. Indeed by Lemma 7.2 we have

$$
\begin{aligned} \liminf_{\varepsilon \to 0} \int u^b I_\varepsilon(x) \phi &\ge \liminf_{\varepsilon \to 0} \int_{\Omega_\varepsilon} u^b I_\varepsilon(x) \phi \\ &\ge -\frac{1}{4(m-1)} \lim_{\varepsilon \to 0} \int_{\Omega_\varepsilon} u^{b+2a-2} (1+\mathbf{u}f(\mathbf{u}))^2 \phi \to 0 \end{aligned} \quad (7.22)
$$

since $|\Omega_\varepsilon \cap (\operatorname{supp} \phi)| \to 0$ and the integrand in (7.22) is bounded. Proposition 7.2 is therefore proved.

Proposition 6.1 for the case $1<m<2$ now follows by setting, as in (6.26),

$$
a = -\frac{m-1}{m} m^*, \quad b = \frac{n-1}{n} m^* - d.
$$

It remains to prove Lemma 7.2.

*Proof of Lemma 7.2.* For $|\nabla u| < \varepsilon$ one has $\mathbf{v}_\varepsilon = \varepsilon^{m-2} u^a \nabla u$ and

$$
\mathbf{V}_\varepsilon = \varepsilon^{m-2} u^{a-1} (a \nabla u \otimes \nabla u + u \mathbf{H}),
$$

with $\mathbf{H} = \nabla^2 u$. Since $\mathbf{H} = \nabla^2 u = 0$ a.e. on $\Omega_{\text{cr}}$, one has as well that $\mathbf{V}_\varepsilon = 0$, $\operatorname{div} \mathbf{v}_\varepsilon = 0$ a.e. on $\Omega_{\text{cr}}$. On the other hand, $\mathbf{v}_\varepsilon = \mathbf{v}$, $\mathbf{V}_\varepsilon \equiv \mathbf{V}$ and $I_\varepsilon = I$ when $|\nabla u| \ge \varepsilon$.

Therefore, as in the proof of Lemma 6.6 we get $I_{\varepsilon}(x) \ge 0$ (a.e.) on $\Omega_{\varepsilon}^c$ (note that $I_{\varepsilon}=0$ a.e. on $\Omega_{cr}$).

Next consider the remaining case $x \in \Omega_{\varepsilon}$. Here one finds by (7.2) and (6.5) that

$$
\mathbf{V} = u^{a-1} |\nabla u|^{m-2} [a \nabla u \otimes \nabla u + u(\mathbf{I} + (m-2)\mathbf{w} \otimes \mathbf{w})\mathbf{H}],
$$

where $\mathbf{w} = \nabla u / |\nabla u|$. Thus, recalling that $1 < m < 2$,

$$
\begin{align*}
\operatorname{trace} \mathbf{V}_{\varepsilon} \mathbf{V} &= \varepsilon^{m-2} u^{2(a-1)} |\nabla u|^{m-2} \\
&\quad \times \{a^2 |\nabla u|^4 + a m u |\nabla u|^2 \{\mathbf{w}\mathbf{H}\mathbf{w}\} + u^2 (|\mathbf{H}|^2 + (m-2) |\mathbf{w}\mathbf{H}|^2)\} \\
&\ge \varepsilon^{m-2} u^{2(a-1)} |\nabla u|^{m-2} \cdot \{a^2 |\nabla u|^4 + a |\nabla u|^2 \cdot m u \{\mathbf{w}\mathbf{H}\mathbf{w}\} + (m-1) u^2 |\mathbf{H}|^2\} \\
&\equiv \varepsilon^{m-2} u^{2(a-1)} |\nabla u|^{m-2} \cdot \{Q + \frac{1}{2} (m-1) u^2 |\mathbf{H}|^2\},
\end{align*}
$$

defining $Q$. By the Cauchy-Schwarz inequality (and the usual trick),

$$
Q \ge \left(1 - \frac{m^2}{2(m-1)}\right) a^2 |\nabla u|^4 \ge -\frac{1}{m-1} a^2 |\nabla u|^4.
$$

Noticing that $|\nabla u|^{m+2} \le \varepsilon^{m+2}$ and $|\nabla u|^{m-2} \ge \varepsilon^{m-2}$ since $1 < m < 2$, we then get by combining the previous lines,

$$
\operatorname{trace} \mathbf{V}_{\varepsilon} \mathbf{V} \ge -\frac{1}{m-1} a^2 \varepsilon^{2m} u^{2(a-1)} + \frac{1}{2} (m-1) \varepsilon^{2(m-2)} u^{2a} |\mathbf{H}|^2. \quad (7.23)
$$

On the other hand,

$$
\frac{1}{n} \operatorname{div} \mathbf{v}_{\varepsilon} \operatorname{div} \mathbf{v} = \frac{1}{n} \operatorname{trace} \mathbf{V}_{\varepsilon} \operatorname{div} \mathbf{v} = \frac{1}{n} \varepsilon^{m-2} u^{2(a-1)} \{a |\nabla u|^2 + u \Delta u\} \cdot \{a |\nabla u|^m - u f(u)\}
$$

using the second equation in (6.11) at the last step. Then, by the Cauchy-Schwarz inequality again,

$$
\begin{align}
\frac{1}{n} \operatorname{div} \mathbf{v}_{\varepsilon} \operatorname{div} \mathbf{v} \le & \frac{1}{2} (m-1) \varepsilon^{2(m-2)} u^{2a} |\Delta u|^2 \nonumber \\
& + u^{2(a-1)} \frac{|a|}{n} \varepsilon^m \{|a| \varepsilon^m + u f(u)\} + \frac{1}{2n^2(m-1)} \{|a| \varepsilon^m + u f(u)\|^2. \tag{7.24}
\end{align}
$$

Hence finally, by (7.23) and (7.24),

$$
\begin{align*}
I_{\varepsilon} &= \operatorname{trace} \mathbf{V}_{\varepsilon} \mathbf{V} - \frac{1}{n} \operatorname{div} \mathbf{v}_{\varepsilon} \operatorname{div} \mathbf{v} \\
&\ge -\frac{1}{2(m-1)} u^{2(a-1)} \left[ a^2 \varepsilon^{2m} + 2(m-1) \frac{|a|}{n} \varepsilon^m (|a| \varepsilon^m + u f(u)) + \frac{1}{n^2} (|a| \varepsilon^m + u f(u))^2 \right] \\
&= -\frac{1}{2(m-1)} u^{2(a-1)} \left[ \left(1 + \frac{1}{n}\right) |a| \varepsilon^m + \frac{1}{n} u f(u) \right]^2.
\end{align*}
$$

The required result now follows from the fact that $n \ge 2$.

## 8. Regularity theory

In this section, we consider the regularity of weak solutions of (1.4). We shall require only that $u \in C^1(\Omega)$ and $f \in C^1(\mathbf{R}^n)$, rather than the more specialized conditions which were assumed for the earlier work.

The following fundamental result is well-known, see [1], [10], [11], [13], [27], [29], [30].

THEOREM 8.1. Let $u$ be a weak solution of (1.4). Then there exists $\beta \in (0, 1)$ such that

$$
u \in W_{\text{loc}}^{2,2}(\Omega). \qquad (8.1)
$$

Moreover,

$$
u \in C_{\text{loc}}^{1,\beta}(\Omega). \qquad (8.2)
$$

The embedding $u \in W_{\text{loc}}^{2,2}(\Omega)$ for $1<m<2$ in particular is due to Acerbi and Fusco [1], though the result is essentially contained in earlier work; we give a separate proof below as a corollary of Lemma 8.2.

Our main regularity theorem improves (8.1) in the case $1<m<2$, by introducing an important weighting factor.

PROPOSITION 8.1. Let $u$ be a weak solution of (1.4), with $1<m<2$. Then

$$
|\nabla u|^{m-2} \nabla^2 u \in L^2(\Omega' \setminus \Omega_{\text{cr}}) \qquad (8.3)
$$

where $\Omega'$ is any compact subset of $\Omega$ and

$$
\Omega_{\text{cr}} = \{x \in \Omega \mid \nabla u = 0\}
$$

is the critical set of the solution $u$.

Condition (8.3) implies that the "natural" Jacobian matrix $\mathbf{U}=\nabla \mathbf{u}$, see (6.5), is in $L_{\text{loc}}^2(\Omega' \setminus \Omega_{\text{cr}})$. This fact is crucial for the proof of Proposition 6.1 in the case $m<2$, see the discussion of (7.21) in §7.

The proof of Proposition 8.1 requires a series of lemmas. The first is elementary.

LEMMA 8.1. Let $\mathbf{a}, \mathbf{b}$ be vectors in $\mathbf{R}^n$ with $|\mathbf{a}| + |\mathbf{b}| > 0$, and suppose $m > 1$. Then

$$
| |\mathbf{a}|^{m-2} \mathbf{a} - |\mathbf{b}|^{m-2} \mathbf{b} | \le C_1 (|\mathbf{a}| + |\mathbf{b}|)^{m-2} |\mathbf{a} - \mathbf{b}| \qquad (8.4)
$$

and

$$
(|\mathbf{a}|^{m-2} \mathbf{a} - |\mathbf{b}|^{m-2} \mathbf{b})(\mathbf{a} - \mathbf{b}) \ge C_2 (|\mathbf{a}| + |\mathbf{b}|)^{m-2} |\mathbf{a} - \mathbf{b}|^2, \qquad (8.5)
$$

where

$$
C_1 = 2, \quad C_2 = 2^{2-m} \min(m-1, 1).
$$

Remarks. The right-hand sides of (8.4) and (8.5) are undefined when $\mathbf{a}=\mathbf{b}=0$ and $m<2$; in this case we understand them to have the value 0. The same agreement will of course apply in later applications of these inequalities.

The actual forms of $C_1$ and $C_2$ are not important, only the simpler fact that they depend only on the exponent $m$.⁽⁸⁾

Let $\{\mathbf{e}_i\}_1^n$ be an orthonormal basis of $\mathbf{R}^n$. For $h>0$ and $h^i=h\mathbf{e}_i$, put

$$
u_{h^i}(x) = h^{-1}(u(x+h^i) - u(x)), \quad i = 1, 2, \dots, n, \qquad (8.6)
$$

and introduce the matrix field $\mathbf{U}_h$ with components

$$
\{\mathbf{U}_h\}_i^j = h^{-1}\{|\nabla u(x+h^i)|^{m-2}\nabla_j u(x+h^i) - |\nabla u(x)|^{m-2}\nabla_j u(x)\} \qquad (8.7)
$$

where $\nabla_j u = \partial u / \partial x_j$. For simplicity we shall also write (8.6) and (8.7) in the abbreviated forms

$$
u_h = h^{-1}(u(x+h) - u(x))
$$

and

$$
\mathbf{U}_h = h^{-1}\{|\nabla u(x+h)|^{m-2}\nabla u(x+h) - |\nabla u(x)|^{m-2}\nabla u(x)\},
$$

with similar simplifications in subsequent formulas. Of course, we shall always suppose that $h$ is so small that these formulas are meaningful for a given $x$ in $\Omega$.

Here and in the sequel, by $B_R=B_R(x_0)$ we shall mean a ball of radius $R$ and center $x_0$, such that the corresponding ball $B_{4R}(x_0)$ of radius $4R$ is in $\Omega$.

LEMMA 8.2. There exists a constant $C=C(x, R, n, m)>0$ such that (when $h<R$)

$$
\int_{B_R} \{|\nabla u(x+h)| + |\nabla u(x)|\}^{m-2} |\nabla u_h|^2 dx \le C, \qquad (8.8)
$$

the integrand being assigned the value 0 when $\nabla u(x+h)=\nabla u(x)=0$.

Proof. Take differences in (1.4), resulting in

$$
\operatorname{div} \mathbf{U}_h^T = \mathbf{y}, \qquad (8.9)
$$

where $\mathbf{y}=f'(\zeta)u_h$ and $\zeta$ is an intermediate value, see (6.25).

⁽⁸⁾ To obtain (8.4) and (8.5) one can proceed as follows. By direct calculus we see that for fixed $|\mathbf{a}|, |\mathbf{b}| \ne 0$ the ratio of the two sides of (8.4) attains its maximum when $\cos \theta=1$ if $m>2$, and when $\cos \theta=-1$ if $m<2$; and conversely for (8.5) the ratio assumes its minimum when $\cos \theta=-1$ if $m>2$, and when $\cos \theta=1$ if $m<2$, where $\theta$ is the angle between the vectors $\mathbf{a}$ and $\mathbf{b}$; in all cases, then, the extremum is reached when $\mathbf{a}$ and $\mathbf{b}$ are parallel. Once this is shown, it is easy (again using elementary calculus) to estimate the maximum and minimum of these ratios as $|\mathbf{a}|$ and $|\mathbf{b}|$ vary. (In fact, $C_2$ can be taken to be 1 when $m=2$ or $m \ge 3$.)

Let $\xi$ be a standard cut-off function on the ball $B_{2R} \subset \Omega$; see Lemma 2.4. Multiply (8.9) by the test function $\xi^2 u_h(x)$ and integrate over $B$ to obtain

$$
\int \xi^2 \mathbf{U}_h \cdot \nabla u_h + \int u_h \mathbf{U}_h \cdot \nabla (\xi^2) = \xi^2 f'(\zeta) |u_h|^2. \quad (8.10)
$$

Observe by (8.5) and (8.7) that (for each fixed direction $\mathbf{e}_i$)

$$
\mathbf{U}_h \cdot \nabla u_h \geqslant C_2 \{|\nabla u(x+h)| + |\nabla u(x)|\}^{m-2} |\nabla u_h|^2. \quad (8.11)
$$

Also when $m \in (1, 2)$, we can bound$^{(9)}$

$$
\begin{align*}
\left| \int u_h \mathbf{U}_h \cdot \nabla (\xi^2) \right| &= \left| \iint_0^1 \nabla_i \{(\nabla u)^{m-2} \nabla_j u(x+sh^i)\} u_{h^i} \nabla_j \xi^2 \, ds \, dx \right| \\
&= \left| \int_0^1 \int [\nabla u^{m-2} \nabla_j u](x+sh^i) \nabla_i [u_{h^i} \nabla_j \xi^2] \, ds \, dx \right| \\
&\leqslant \int_0^1 \int |\nabla u(x+sh)|^{m-1} \{|\nabla u_h| |\nabla \xi^2| + |u_h| |\nabla^2 \xi^2|\} \, ds \, dx \\
&\leqslant 4R^{-1} \int_0^1 \int |\nabla u(x+sh)|^{m-1} |\nabla u_h| \xi \, ds \, dx + CR^{-2} \\
&\leqslant \frac{C_2}{2} \int \{|\nabla u(x+h)| + |\nabla u(x)|\}^{m-2} |\nabla u_h|^2 \xi^2 \, dx \tag{8.12} \\
&\quad + CR^{-2} \int \left( \int_0^1 |\nabla u(x+sh)|^{m-1} \, ds \right)^2 \{|\nabla u(x+h)| + |\nabla u(x)|\}^{2-m} \, dx \\
&\quad + CR^{-2} \\
&\leqslant \frac{C_2}{2} \int \{|\nabla u(x+h)| + |\nabla u(x)|\}^{m-2} |\nabla u_h|^2 \xi^2 \, dx + CR^{-2}.
\end{align*}
$$

The constants $C$ in the above calculation clearly depend only on $n$, $m$ and bounds on $\nabla u$ in the ball $B_{3R}(x_0)$. The estimate (8.8) now follows at once with the help of (8.10)–(8.12).

For $m \geqslant 2$, we have by (8.4),

$$
\begin{align*}
\left| \int u_h \mathbf{U}_h \cdot \nabla (\xi^2) \right| &\leqslant 8R^{-1} \int \{|\nabla u(x+h^i)| + |\nabla u(x)|\}^{m-2} |\nabla u_h| \cdot |u_h| \xi \, dx \\
&\leqslant \frac{C_2}{2} \int \{|\nabla u(x+h)| + |\nabla u(x)|\}^{m-2} |\nabla u_h|^2 \xi^2 \, dx + CR^{-2},
\end{align*}
$$

(9) At the first and second steps of the calculation, we use summed index notation to avoid confusion. At the fourth step take $|\nabla \xi| \leqslant 2R^{-1}$, and at the second to last step use the Cauchy-Schwarz inequality.

and again (8.8) follows immediately.

*Proof of (8.1) when $1<m<2$. By (8.8),*

$$
\int_{B_R} |\nabla u_h|^2 dx \le C
$$

since $u \in C^1(\Omega)$. Because $u_h \to \nabla u$ as $h \to 0$ (uniformly on compact subsets), it is now a standard result of the calculus of distribution derivatives (using the weak sequential compactness of $L_{\text{loc}}^2(\Omega)$) that $u \in W_{\text{loc}}^{2,2}(\Omega)$, as asserted.

The rest of the section is devoted to proving the important embedding (8.3). We first need two technical lemmas. Here it is convenient to define

$$
l = \frac{1}{2}(2-m) = 1 - \frac{1}{2}m;
$$

note particularly that $l>0$ when $1<m<2$.

LEMMA 8.3. *The function*

$$
z = \begin{cases} |\nabla u|^{-l} |\nabla^2 u|, & x \in \Omega_{\text{cr}}^c, \\ 0, & x \in \Omega_{\text{cr}}, \end{cases} \qquad (8.13)
$$

is in $L_{\text{loc}}^2(\Omega)$.

*Proof.* By (8.8) the quantity

$$
K_h = (|\nabla u(x+h^j)| + |\nabla u(x)|)^{-l} |\nabla u_h|
$$

is uniformly in $L_{\text{loc}}^2(\Omega)$ (use the Heine-Borel theorem). Clearly $K_h \to 2^{-l}z$ pointwise in $\Omega$. Hence by the weak sequential compactness of $L_{\text{loc}}^2(\Omega)$, $K_h \to 2^{-l}z$ weakly in $L_{\text{loc}}^2(\Omega)$, which at once yields the required result.

*Remark.* Here (and also below) we use the fact that weak convergence and pointwise convergence are consistent, that is, if $\psi_h \to \psi$ weakly in $L^p$, $p \ge 1$, and $\psi_h \to \zeta$ pointwise (almost everywhere) then $\psi=\zeta$ a.e. This result is apparently well-known but it seems difficult to find a proof in standard texts. An easy demonstration can be given using Egoroff's theorem. Indeed, suppose that $\psi \ne \zeta$ on some set of positive measure, say, e.g.,

$$
\Gamma = \{x \in \Omega \mid \psi(x) > \zeta(x)\}
$$

with $|\Gamma|>0$. By Egoroff's theorem, there exists $\Gamma_1 \subset \Gamma$ such that $|\Gamma_1| = \frac{1}{2}|\Gamma|>0$ and $\psi_h \to \zeta$ uniformly on $\Gamma_1$ (up to a subsequence). Put $\phi = \chi_{\Gamma_1}$. Then by weak convergence,

$$
\int \psi_h \phi \to \int \psi \phi = \int_{\Gamma_1} \phi,
$$

while by uniform convergence,

$$
\int \psi_h \phi = \int_{\Gamma_1} \psi_h \to \int_{\Gamma_1} \zeta,
$$

a contradiction.

LEMMA 8.4. Let $1<m<2$. Let $\mathbf{U}$ be given by (7.1), and $\mathbf{u}_\varepsilon = |\nabla u|_\varepsilon^{m-2} \nabla u$ as in §7. Then as $h \to 0$,

$$
\mathbf{u}_\varepsilon \mathbf{U}_h \to \mathbf{u}_\varepsilon \mathbf{U} \quad \text{weakly in } L_{\text{loc}}^2(\Omega)
$$

and

$$
\nabla \mathbf{u}_\varepsilon \mathbf{U}_h \to \nabla \mathbf{u}_\varepsilon \mathbf{U} \quad \text{weakly in } L_{\text{loc}}^1(\Omega),
$$

where $\mathbf{U}_h$ is the (matrix) difference quotient (8.8).

Remark. This is exactly Lemma 7.1, whose proof was previously deferred.

Proof. (i) For fixed $\varepsilon > 0$, we write

$$
\mathbf{u}_\varepsilon \mathbf{U}_h = |\nabla u|^{-l} \mathbf{u}_\varepsilon \cdot |\nabla u|^l \mathbf{U}_h.
$$

Clearly

$$
|\nabla u|^{-l} \mathbf{u}_\varepsilon \le \begin{cases} \varepsilon^{m/2-2l} & \text{if } m \le \frac{4}{3}, \\ |\nabla u|^{m/2-2l} & \text{if } m > \frac{4}{3}, \end{cases}
$$

so $|\nabla u|^{-l} \mathbf{u}_\varepsilon \in L_{\text{loc}}^\infty(\Omega)$. On the other hand, by (8.4) and (8.7), one verifies since $m<2$ and $l>0$ that

$$
|\nabla u|^l |\mathbf{U}_h| \le 2(|\nabla u(x+h)| + |\nabla u(x)|)^{-l} |\nabla u_h|,
$$

which is uniformly bounded in $L_{\text{loc}}^2(\Omega)$ by (8.8).

Now observe that outside the critical set the expression $\mathbf{u}_\varepsilon \mathbf{U}_h \to \mathbf{u}_\varepsilon \mathbf{U}$ pointwise as $h \to 0$, while on the critical set both sides are zero. The first conclusion now follows as previously, in view of the weak sequential compactness of $L_{\text{loc}}^2(\Omega)$.

(ii) By the definition of $\nabla \mathbf{u}_\varepsilon$, we have

$$
|\nabla \mathbf{u}_\varepsilon| \le \begin{cases} \varepsilon^{m-2} |\nabla^2 u| & \text{if } |\nabla u| < \varepsilon, \\ |\nabla u|^{m-2} |\nabla^2 u| & \text{if } |\nabla u| \ge \varepsilon, \end{cases}
$$

where, for the set $\{|\nabla u| \ge \varepsilon\}$, we have used the equality $\nabla u_\varepsilon = \nabla u = \mathbf{U}$ together with Lemma 6.1 and the fact that $m<2$. Therefore

$$
|\nabla \mathbf{u}_\varepsilon| \le \varepsilon^{m-2} |\nabla^2 u| \quad \text{for } x \in \Omega. \qquad (8.14)
$$

Now write

$$
\mathbf{Y} = \begin{cases} |\nabla u|^{-l} \nabla \mathbf{u}_\varepsilon, & x \in \Omega_{\text{cr}}^c, \\ 0, & x \in \Omega_{\text{cr}}. \end{cases} \qquad (8.15)
$$

Then by (8.13)-(8.15),

$$
|\mathbf{Y}| = |\nabla u|^{-l} |\nabla \mathbf{u}_\varepsilon| \le \varepsilon^{m-2} |\nabla u|^{-l} |\nabla^2 u| = \varepsilon^{m-2} z, \quad x \in \Omega_{\text{cr}}^c.
$$

Thus $\mathbf{Y} \in L_{\text{loc}}^2(\Omega)$ by Lemma 8.3.

As in (i), the quantity $|\nabla u|^l \mathbf{U}_h$ is uniformly bounded in $L_{\text{loc}}^2(\Omega)$. But also $|\nabla u|^l \mathbf{U}_h \to |\nabla u|^l \mathbf{U}$ pointwise as $h \to 0$. Therefore as in earlier arguments, the convergence is also in $L_{\text{loc}}^2(\Omega)$. Consequently, noting that

$$
\nabla \mathbf{u}_{\varepsilon} = |\nabla u|^l \mathbf{Y},
$$

we see that (with weak convergence in $L_{\text{loc}}^1(\Omega)$)

$$
\nabla \mathbf{u}_{\varepsilon} \mathbf{U}_h = \mathbf{Y} |\nabla u|^l \mathbf{U}_h \to \mathbf{Y} |\nabla u|^l \mathbf{U} = \nabla \mathbf{u}_{\varepsilon} \mathbf{U}.
$$

This completes the proof.

Finally, we can prove the embedding (8.3). By (6.25), since $\mathbf{U}_h \in C(\Omega)$, we can write

$$
\int \mathbf{U}_h \cdot \nabla \phi = \int \mathbf{y} \phi,
$$

for any $\phi \in W_0^{1,1}(\Omega)$. We take $\phi$ to be the vector

$$
\phi = \mathbf{u}_{\varepsilon} \xi^2, \quad \varepsilon \in (0, 1),
$$

where $\xi$ is a standard cut-off function in $B_{2R}$, see Lemma 2.3; actually $\phi \in W_0^{1,2}(\Omega)$. Then one obtains easily, after contracting against $\mathbf{u}_{\varepsilon}$,

$$
\int \xi^2 \operatorname{trace}(\nabla \mathbf{u}_{\varepsilon} \mathbf{U}_h) + \int 2\xi(\mathbf{u}_{\varepsilon} \mathbf{U}_h) \cdot \nabla \xi = \int \xi^2 \mathbf{y} \cdot \mathbf{u}_{\varepsilon}.
$$

Let $h \to 0$. Using Lemma 8.4 and the definition of $\mathbf{y}$ (see (6.25)), we get

$$
\int \xi^2 \operatorname{trace}(\nabla \mathbf{u}_{\varepsilon} \mathbf{U}) + \int 2\xi(\mathbf{u}_{\varepsilon} \mathbf{U}) \cdot \nabla \xi = - \int \xi^2 f'(u) \mathbf{u}_{\varepsilon} \cdot \nabla u. \quad (8.16)
$$

Now from Lemma 6.1,

$$
\operatorname{trace}(\nabla \mathbf{u}_{\varepsilon} \mathbf{U}) \ge (m-1)\varepsilon^{m-2} |\nabla u|^{m-2} |\nabla^2 u|^2
$$

when $0 < |\nabla u| < \varepsilon$, and similarly

$$
\operatorname{trace}(\nabla \mathbf{u}_{\varepsilon} \mathbf{U}) = \operatorname{trace}(\mathbf{U}^2) \ge (m-1)^2 |\nabla u|^{2m-4} |\nabla^2 u|^2
$$

if $|\nabla u| \ge \varepsilon$. In turn, one checks without difficulty that

$$
\operatorname{trace}(\nabla \mathbf{u}_{\varepsilon} \mathbf{U}) \ge (m-1)^2 |\nabla u|_{\varepsilon}^{m-2} z^2 \quad \text{for } x \in \Omega.
$$

On the other hand, from (8.13) and another use of Lemma 6.1, we get $|U| \le |\nabla u|^{-l} z$.
Consequently, by the Cauchy-Schwarz inequality and (8.13),

$$
\begin{aligned}
-\xi(\mathbf{u}_\varepsilon \mathbf{U}) \cdot \nabla \xi &\le \xi(|\nabla u|_\varepsilon |\nabla u|)^{-l} |\mathbf{U}| \cdot |\mathbf{u}_\varepsilon| (|\nabla u|_\varepsilon |\nabla u|)^l |\nabla \xi| \\
&\le \frac{1}{2}(m-1)^2 \xi^2 |\nabla u|_\varepsilon^{m-2} z^2 + \frac{1}{2(m-1)^2} |\nabla u|_\varepsilon^{2(m-1)} |\nabla \xi|^2.
\end{aligned}
$$

Thus by (8.16),

$$
\frac{1}{2}(m-1)^2 \int \xi^2 |\nabla u|_\varepsilon^{m-2} z^2 \le \int A(x) |\nabla \xi|^2 + \int B(x) \xi^2,
$$

where

$$
A(x) = \frac{1}{2(m-1)^2} |\nabla u|_\varepsilon^{2(m-1)}, \quad B(x) = |f'(u)| \cdot |\nabla u|^m
$$

are in $L_{\text{loc}}^\infty(\Omega)$. In turn

$$
\int_{B_R} |\nabla u|_\varepsilon^{m-2} z^2 \le \text{Const.},
$$

the constant being *independent* of $\varepsilon$ (since $|\nabla u|_\varepsilon \le 1 + |\nabla u|$ in the expression for $A(x)$).
By the Lebesgue monotone convergence theorem, we now get

$$
\int_{B_R} |\nabla u|^{m-2} z^2 \le \text{Const.},
$$

which by (8.13) is exactly the statement that $|\nabla u|^{m-2} |\nabla^2 u|$ is in $L^2(\hat{\Omega} \setminus \Omega_{\text{cr}})$. This completes the proof of Proposition 8.1.

## 9. Historical note: Cauchy and Liouville, a question of priority

Augustin Cauchy was the first person to publish the result now known as Liouville's theorem (see [8]). The contribution of Joseph Liouville is an interesting and tangled story, worth recounting in some detail. A few weeks before Cauchy's note appeared, Liouville announced to the academy his first results for doubly-periodic functions, for which he is justly famous (C. R. Acad. Sci. Paris, 19 (1844), 1262). This announcement includes, without proof, a weak version of Cauchy's theorem, namely the statement that a doubly-periodic holomorphic function must be constant. Cauchy was entirely aware of the relation of his result to that of Liouville, as he writes (C. R. Acad. Sci. Paris, 19 (1844), 1379), "If one considers separately the case of doubly-periodic functions, one recovers the special theorem regarded with reason, by one of our honorable associates, as particularly applicable to the theory of elliptic functions."

Three years later, Liouville gave a series of informal lectures on his theory for F. Joachimsthal and C. W. Borchardt; these lectures, containing the previously cited weak version of Cauchy's result, but with no reference to Cauchy, were transcribed and edited by Borchardt and (much later) published in *J. Reine Angew. Math.*, 88 (1880), 277-310. Outside of the first announcement and one later note (see below), this is the entire published record of Liouville's work; surprisingly it does not contain Liouville's own proof, but instead an alternate discussion due to Borchardt.

In 1851 Cauchy again wrote explicitly that his work of 1844 "furnished the fundamental principle invoked by M. Liouville for doubly-periodic functions" and went on to restate his result of 1844 (see *C. R. Acad. Sci. Paris*, 32 (1851), 452-454; *Œuvres complètes*, Ire série, tome XI, 373-376). At about the same time, Liouville delivered a carefully written course of lectures at the Collège de France on doubly-periodic functions, containing a relatively simple proof of his doubly-periodic theorem, but again not citing Cauchy's contribution.

Liouville was clearly much concerned with what he considered his priority to the doubly-periodic result, for in 1855 (*J. Math. Pures Appl.*, 20, 201-208) he republished his 1844 remarks together with a later comment of 1851 containing much the same material; indeed he even went on to refer explicitly to his lectures at the Collège de France "in the second semester of the year 1850-1851". This degree of concern almost certainly stems from the remarkable fact that near the end of his mathematical notebook for the year 1844 he had written the following "*Remarque d'analyse*":

*Soit $f(z)$ une fonction bien déterminée de $z$. Si le module de $f(z)$ ne dépasse jamais $M$, on a $f(z)=\text{Constante}$.*

Since it is evident that he understood the function $f(z)$ to be given on the entire complex plane, this is clearly the general result! There follows a one-line proof sketch, which however can only be considered tentative. From internal evidence it seems highly likely that these words were written prior to the announcement of 1844, that Liouville then devoted his effort to finding a proof of the doubly-periodic result, and, upon finding a (difficult) demonstration, then reported this (but only this) result to the academy. He never afterwards referred to the "Remarque".

Liouville saw the utility and centrality of the doubly-periodic theorem for elliptic function theory, but in his preoccupation with this he missed the elegance and beauty of the main result. Cauchy on the other hand immediately understood its importance, as have all subsequent writers. Clearly disappointed at the turn of events, Liouville at no time thereafter ever made reference to Cauchy's theorem. The irony is that nevertheless it is Liouville's name which has become attached to the theorem.

The first modern proof of the main theorem (still found in texts today, based on

the Taylor expansion) is apparently due to Briot and Bouquet in the first edition of their monograph *Théorie des fonctions elliptiques*, Paris, 1859. They refer neither to Cauchy nor to Liouville for the result. Very curiously, the first published attribution of the theorem to Liouville (to our knowledge) occurs in the *second edition*, Paris, 1875, pp. 202-203. In the preface (p. iv) they cite Liouville's lectures of 1851 as the source for their attribution, though as we have noted above, their proof is neither Cauchy's nor Liouville's but essentially the modern one based on Taylor's series.

A few years later, E. Borel, *Leçons sur les fonctions entières*, Paris, 1900, p. 2, gives the result back to Cauchy, though without citing a source. Finally, Whittaker and Watson in *A Course of Modern Analysis*, Cambridge, 1902, explicitly call the result "Liouville's theorem", again without citation; in their second edition, however, Cambridge, 1915, while still naming the result Liouville's theorem, they specifically attribute it to Cauchy and cite the 1844 reference at the beginning of this note. On rare occasions a more modern treatise on complex analysis still refers to Cauchy, e.g., works of Copson, 1935; Dinghas, 1961; Sansone and Gerretson, 1962. But by this time the die has been cast.

For simplicity throughout the present work, we have continued the customary practice of attaching Liouville's name to results in which a non-negative solution of an elliptic equation is shown to be constant.

(We are indebted to Professor Edgar Reich for his aid in locating some of the sources cited above, and for helpful discussions of the various historical issues involved. We also thank Fabienne Queyroux of the Bibliothèque, Institut de France, for her help in locating Liouville's notebooks and manuscripts. We cite also J. Lützen's *Joseph Liouville 1809-1882: Master of Pure and Applied Mathematics*, Springer-Verlag, 1990, where there is an extended and interesting discussion of some of the material above, though the presentation is partly marred by championship of Liouville's priority claims.)