# Variance and Standard Deviation — Real Time Example

## Employee Salary Example

### Company A Salaries

```python
[49000, 50000, 51000]
```

Mean Salary:

[
\frac{49000 + 50000 + 51000}{3} = 50000
]

Average salary = ₹50,000

---

### Company B Salaries

```python
[10000, 50000, 90000]
```

Mean Salary:

[
\frac{10000 + 50000 + 90000}{3} = 50000
]

Average salary = ₹50,000

---

# Important Observation

Both companies have the SAME mean salary.

But the salary distribution is very different.

---

## Company A

```python
49000
50000
51000
```

* Salaries are close together
* Very stable
* Low spread
* Low variance
* Low standard deviation

---

## Company B

```python
10000
50000
90000
```

* Salaries are far apart
* Highly spread
* Unstable
* High variance
* High standard deviation

---

# Why Variance Exists

Variance measures:

> How far values are from the average.

---

# Company A Variance Intuition

| Salary | Difference From Mean |
| ------ | -------------------- |
| 49000  | -1000                |
| 50000  | 0                    |
| 51000  | 1000                 |

Differences are small.

Variance is LOW.

---

# Company B Variance Intuition

| Salary | Difference From Mean |
| ------ | -------------------- |
| 10000  | -40000               |
| 50000  | 0                    |
| 90000  | 40000                |

Differences are huge.

Variance is HIGH.

---

# Standard Deviation

Standard deviation is:

[
\text{Standard Deviation} = \sqrt{\text{Variance}}
]

It tells:

> On average, how much values deviate from the mean.

---

# Real Interpretation

## Company A

Small standard deviation:

```python
~1000
```

Meaning:

* Most salaries are close to average.
* Very consistent salary structure.

---

## Company B

Large standard deviation:

```python
~40000
```

Meaning:

* Salaries vary a lot.
* Very inconsistent salary structure.

---

# Real World Uses

| Field            | Use                         |
| ---------------- | --------------------------- |
| Finance          | Measure stock market risk   |
| Cricket          | Measure player consistency  |
| Machine Learning | Understand data spread      |
| Manufacturing    | Product quality consistency |
| Education        | Student score consistency   |

---

# Stock Market Example

| Stock | Average Return | Standard Deviation |
| ----- | -------------- | ------------------ |
| A     | 10%            | 2%                 |
| B     | 10%            | 25%                |

Both stocks give the same average return.

But:

* Stock A is stable
* Stock B is risky

Investors use standard deviation to measure risk.

---

# Median

Median means:

> The middle value after sorting the data.

---

# Odd Number of Elements

Example:

```python
[1, 3, 5, 7, 9]
```

Middle value:

```python
5
```

So median = 5.

---

# Even Number of Elements

Example:

```python
[1, 3, 5, 7]
```

Two middle values:

```python
3 and 5
```

Median:

[
rac{3+5}{2}=4
]

So median = 4.

---

# Real-Time Median Example

Suppose company salaries are:

```python
[25000, 27000, 30000, 35000, 900000]
```

Mean becomes very high because of one CEO salary:

[
rac{25000+27000+30000+35000+900000}{5}=203400
]

Average salary looks like ₹203,400.

But most employees are NOT earning that much.

Now sort salaries:

```python
[25000, 27000, 30000, 35000, 900000]
```

Middle value:

```python
30000
```

Median = ₹30,000.

This better represents the typical employee salary.

---

# Why Median Is Important

Median is useful when:

* Outliers exist
* Extreme values distort average
* Data is skewed

Used heavily in:

* Salary analysis
* Real estate prices
* Income statistics
* Population studies

---

# Final Memory Notes

| Concept            | Meaning                    |
| ------------------ | -------------------------- |
| Mean               | Average                    |
| Median             | Middle value after sorting |
| Variance           | Spread of values squared   |
| Standard Deviation | Actual spread distance     |

---

# Most Important Intuition

Mean alone is NOT enough.

Variance and standard deviation tell:

* Stability
* Consistency
* Risk
* Data spread
