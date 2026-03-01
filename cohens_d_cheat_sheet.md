---
title: Cohen's d Cheat Sheet
exports:
  - format: pdf
    template: lapreprint-typst
---


# Cohen's *d* Cheat Sheet

Goal: Estimate the population value for the standardized mean difference:


$$\delta = \frac{\mu_1 - \mu_2}{\sigma}$$

where $\mu_1$ and $\mu_2$ are the population means of the two groups and $\sigma$ is the population standard deviation (which is common between the groups).  

Cohen's *d* is a common sample estimator for this parameter.

## Basic Setup

Given two independent groups:

$$\bar{X}_1, \; s_1, \; n_1 \qquad \text{and} \qquad \bar{X}_2, \; s_2, \; n_2$$

where $\bar{X}$ is the sample mean, $s$ is the sample standard deviation (with Bessel's correction, i.e. dividing by $n-1$), and $n$ is the sample size.

---

## Cohen's *d* (Pooled SD)

The most common version, which assumes equal population variances (homogeneity of variance).

$$d = \frac{\bar{X}_1 - \bar{X}_2}{s_p}$$

where the **pooled standard deviation** is:

$$s_p = \sqrt{\frac{(n_1 - 1)\,s_1^2 + (n_2 - 1)\,s_2^2}{n_1 + n_2 - 2}}$$

> **Note:** The denominator $n_1 + n_2 - 2$ uses degrees of freedom (Bessel's correction). Some implementations use $n_1 + n_2$, which is the maximum likelihood estimator but is biased because it underestimates the SD.  The corrected version is an unbiased estimator.

---
## Variants of Cohen's *d*

There are some variants that are sometimes used instead of the pooled SD version.

### Glass's $\Delta$

Uses only the **control group's** standard deviation as the denominator. Useful when variances are unequal and you want to express the effect relative to the control group's variability.

$$\Delta = \frac{\bar{X}_1 - \bar{X}_2}{s_{\text{control}}}$$

> **Watch out:** You must specify which group is the control group. AI tools often pick arbitrarily.

---

### Cohen's *d* (Average SD)

Uses the simple average of the two variances rather than pooling by degrees of freedom. Sometimes used when sample sizes are very unequal.

$$d_{\text{avg}} = \frac{\bar{X}_1 - \bar{X}_2}{s_{\text{avg}}}$$

where:

$$s_{\text{avg}} = \sqrt{\frac{s_1^2 + s_2^2}{2}}$$

> **Note:** This is *not* the same as the pooled SD. When $n_1 = n_2$, the two formulas give identical results. When sample sizes differ, they diverge.

---

## Hedges' *g* (Small-Sample Correction)

Cohen's *d* is positively biased in small samples. Hedges' *g* applies a correction factor $J$:

$$g = J \cdot d$$

where a commonly used approximation for $J$ is:

$$J = 1 - \frac{3}{4(n_1 + n_2) - 9}$$

The exact correction factor is:

$$J_{\text{exact}} = \frac{\Gamma\!\left(\frac{n_1+n_2-2}{2}\right)}{\sqrt{\frac{n_1+n_2-2}{2}} \;\; \Gamma\!\left(\frac{n_1+n_2-3}{2}\right)}$$

where $\Gamma$ is the gamma function. The approximation is accurate to $O(n^{-3})$, but it's now standard to use the original version since it's easy to compute the gamma function.  This is important for total sample sizes less than 100:

| $n_1 + n_2$ | $J$ (approx) | Bias reduction |
|:-----------:|:------------:|:--------------:|
| 10          | 0.903        | ~10%           |
| 20          | 0.956        | ~4%            |
| 50          | 0.983        | ~2%            |
| 100         | 0.992        | <1%            |

---

## Standard Error of *d*

For constructing confidence intervals:

$$SE_d = \sqrt{\frac{n_1 + n_2}{n_1 \, n_2} + \frac{d^2}{2(n_1 + n_2)}}$$

This is a large-sample approximation. For Hedges' *g*, replace $d$ with $g$:

$$SE_g = \sqrt{\frac{n_1 + n_2}{n_1 \, n_2} + \frac{g^2}{2(n_1 + n_2)}}$$

---

## Confidence Interval (Large-Sample Approximation)

$$d \pm z_{\alpha/2} \cdot SE_d$$

For a 95% CI: $z_{0.025} = 1.96$.

> **More accurate method:** Use the noncentral *t*-distribution. The noncentrality parameter is:
>
> $$\lambda = d \sqrt{\frac{n_1 \, n_2}{n_1 + n_2}}$$
>
> Find $\lambda_L$ and $\lambda_U$ such that the observed $t$ is the $1-\alpha/2$ and $\alpha/2$ quantile of the noncentral $t$ with $df = n_1 + n_2 - 2$, then convert back:
>
> $$d_L = \lambda_L \sqrt{\frac{n_1 + n_2}{n_1 \, n_2}}, \qquad d_U = \lambda_U \sqrt{\frac{n_1 + n_2}{n_1 \, n_2}}$$

---

## Relationship to Other Statistics

**From a $t$-test (equal variances):**

$$d = t \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

**From a $t$-test (equal $n$):**

$$d = \frac{2t}{\sqrt{n_1 + n_2 - 2}} \quad \text{(when } n_1 = n_2 \text{)}$$

**To point-biserial correlation $r$:**

$$r = \frac{d}{\sqrt{d^2 + \frac{(n_1 + n_2)^2}{n_1 \, n_2}}}$$

**From $r$ back to $d$:**

$$d = \frac{r \sqrt{n_1 + n_2}}{\sqrt{(1 - r^2) \cdot \frac{n_1 \, n_2}{n_1 + n_2}}}$$

**To overlap (OVL) — percentage of overlap between two normal distributions:**

$$\text{OVL} = 2\,\Phi\!\left(-\frac{|d|}{2}\right)$$

where $\Phi$ is the standard normal CDF.

---

## Common Implementation Pitfalls

1. **$n$ vs. $n-1$:** The pooled SD should use $n_1 + n_2 - 2$ (degrees of freedom), not $n_1 + n_2$.
2. **Which variant?** Pooled, Glass's, and average SD formulas give different results. Know which one you want.
3. **Sign convention:** $d > 0$ or $d < 0$ depends on the order of subtraction. Be consistent.
4. **Hedges' correction omitted:** For samples under ~20 per group, the bias is non-negligible.
5. **Confidence intervals:** The normal approximation is poor for small samples. Use the noncentral $t$ method.
6. **Zero variance:** If all values in a group are identical ($s = 0$), $d$ is undefined. Handle this explicitly.
