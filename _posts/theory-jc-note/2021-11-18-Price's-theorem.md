---
layout: note
author: Rongkang Xiong
title: Price’s theorem
---

两个联合正态分布的随机变量$(x,y)$, 其联合概率密度为 $f(x,y)$，方差 $\mu=\overline{x\cdot y}-\overline{x}\cdot\bar{y}$，给定任意函数 $g(x,y)$，则有期望:

$$
I=E[g(x,y)]=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}g(x,y)f(x,y)\text{d}x\text{d}y
$$

上述积分是方差$\mu$和联合概率密度$f(x,y)$中四个参数的函数，若满足$lim_{(x,y)→∞} g(x,y)f(x,y)=0$，则

$$
\frac{∂^n I(μ)}{∂μ^n}=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}\frac{∂^{2n} g(x,y)}{∂x^n ∂y^n} f(x,y)\text{d}x\text{d}y=E[\frac{∂^{2n} g(x,y)}{∂x^n ∂y^n }]
$$

#### ***Reference***

*[1] A. Papoulis, Probability, Random Variables, and Stochastic Processes (McGraw-Hill, Inc., New York, 1991), 3rd ed, P219~220.*

*[2] R. Price, "A Useful Theorem for NonHnear Devices Having Gaussian Inputs," IRE. PGIT. VoL IT-4. 1995.*

*[3] See also A. Papoulis. "On an Extension of Price's Theorem," IEEE Transactions on Information Theory, Vol. IT-ll,l965.*

