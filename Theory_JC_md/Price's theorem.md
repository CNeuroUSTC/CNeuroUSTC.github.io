# Price’s theorem </br>

两个联合正态分布的随机变量(x,y)</br>
联合概率密度 $f(x,y)$，方差 $\mu=<x,y>-<x><y>$，给定任意函数 $g(x,y)$</br>
期望:</br>
$$I=E[g(x,y)]=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}g(x,y)f(x,y)\text{d}x\text{d}y$$</br>
上述积分是方差$\mu$和联合概率密度$f(x,y)$中四个参数的函数，若满足$lim_{(x,y)→∞} g(x,y)f(x,y)=0$，则</br>
$$\frac{∂^n I(μ)}{∂μ^n}=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}\frac{∂^{2n} g(x,y)}{∂x^n ∂y^n} f(x,y)\text{d}x\text{d}y)=E[\frac{∂^{2n} g(x,y)}{∂x^n ∂y^n }]$$</br>


</br>
</br>

<center><font face="Times New Roman" size=5><font face="TimeNewRoman"></font>Reference</font></center>

<font face="Times New Roman" size=2>[1] A. Papoulis, Probability, Random Variables, and Stochastic Processes (McGraw-Hill, Inc., New York, 1991), 3rd ed, P219~220.</font></br>
<font face="Times New Roman" size=2>[2] R. Price, "A Useful Theorem for NonHnear Devices Having Gaussian Inputs," IRE. PGIT. VoL IT-4. 1995.</font></br>
<font face="Times New Roman" size=2>[3] See also A. Papoulis. "On an Extension of Price's Theorem," IEEE Transactions on Information Theory, Vol. IT-ll,l965.</font></br>
