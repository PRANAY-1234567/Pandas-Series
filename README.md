# Pandas Series – Python Practice

## 📌 About the Project

This project covers the fundamentals of **Pandas Series** in Python. It includes practical examples of Series creation, indexing, attributes, statistical methods, data inspection, sorting, and data type conversion.

The goal is to understand how Pandas Series work and learn the commonly used properties and methods for data analysis.

## 🛠️ Technologies Used

- Python
- Pandas
- Jupyter Notebook / VS Code

## 📚 Topics Covered

### 1. Creating a Pandas Series

- Creating a Series from a list.
- Assigning custom index labels.
- Assigning a name to a Series.

### 2. Series Attributes

| Attribute | Description |
|---|---|
| `values` | Returns the values of the Series. |
| `index` | Returns the index labels. |
| `dtype` | Returns the data type of elements. |
| `shape` | Returns the dimensions as a tuple. |
| `size` | Returns the total number of elements. |
| `ndim` | Returns the number of dimensions. |
| `name` | Returns the name of the Series. |
| `empty` | Checks whether the Series is empty. |
| `is_unique` | Checks whether all values are unique. |
| `hasnans` | Checks whether the Series contains NaN values. |
| `nbytes` | Returns the memory used by the values. |

### 3. Data Inspection Methods

| Method | Description |
|---|---|
| `head()` | Displays the first 5 rows by default. |
| `tail()` | Displays the last 5 rows by default. |
| `sample()` | Returns a random sample of elements. |
| `unique()` | Returns unique values. |
| `nunique()` | Returns the count of unique values. |
| `value_counts()` | Returns the frequency of each unique value. |
| `count()` | Returns the number of non-null elements. |

### 4. Sorting Methods

| Method / Attribute | Description |
|---|---|
| `is_monotonic_increasing` | Checks whether values are in increasing order. |
| `is_monotonic_decreasing` | Checks whether values are in decreasing order. |
| `sort_values()` | Sorts values in ascending or descending order. |

### 5. Data Type Conversion

The `astype()` method converts Series elements into different data types.

Examples:

- `astype(int)` – Integer
- `astype(float)` – Float
- `astype(bool)` – Boolean
- `astype(complex)` – Complex
- `astype(str)` – String

### 6. Statistical Methods

| Method | Description |
|---|---|
| `max()` | Returns the maximum value. |
| `min()` | Returns the minimum value. |
| `sum()` | Returns the sum of all values. |
| `mean()` | Calculates the average. |
| `median()` | Returns the middle value. |
| `mode()` | Returns the most frequently occurring value. |

## 💻 Code Example

```python
import pandas as pd

# Creating a Pandas Series
x = pd.Series(
    [34, 34, 56, 78, 99],
    index=["a", "b", "c", "d", "e"],
    name="Data"
)

# Display Series
print(x)

# Series Attributes
print(x.values)
print(x.index)
print(x.dtype)
print(x.shape)
print(x.size)
print(x.ndim)
print(x.name)

# Data Inspection
print(x.head(2))
print(x.tail(2))
print(x.sample())
print(x.unique())
print(x.nunique())
print(x.value_counts())

# Sorting
print(x.sort_values(ascending=True))

# Data Type Conversion
print(x.astype(float))
print(x.astype(str))

# Statistical Methods
print(x.max())
print(x.min())
print(x.sum())
print(x.mean())
print(x.median())
print(x.mode())
```

## 🎯 Learning Objectives

After completing this practice, I can:

- Create and understand Pandas Series.
- Work with custom indexes.
- Access Series attributes.
- Inspect and analyze Series data.
- Find unique values and their frequencies.
- Sort Series values.
- Convert data types using `astype()`.
- Perform basic statistical calculations.

## 📦 Installation

Install Pandas using pip:

```bash
pip install pandas
```

Import Pandas into your Python file:

```python
import pandas as pd
```

## 🚀 Future Learning

I will continue learning Pandas by covering:

- DataFrames
- DataFrame attributes and methods
- Data selection using `loc` and `iloc`
- Filtering data
- Handling missing values
- Data cleaning
- GroupBy operations
- Merging and joining DataFrames
- Applying functions using `apply()` and `map()`

---

**Author:** Pranay Vishwanath Jadhao

**Focus:** Python | Pandas | Data Analysis

