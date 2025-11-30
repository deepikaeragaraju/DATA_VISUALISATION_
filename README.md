# **Data Visualization Project – Matplotlib & Seaborn**

This project demonstrates various data visualization techniques using **Matplotlib** and **Seaborn**, two of the most widely used Python libraries for creating visual graphs and statistical plots.

It includes documentation, sample datasets, and Python code to help beginners understand how to visualize data effectively.

---

## **Project Contents**

```
Data_visualisation_project
│
├── Visualization document.pdf
├── Visualization document.docx
├── Code files (optional)
├── Dataset files (optional)
└── README.md
```

---

## **Objective**

The main goal of this project is to explain and demonstrate:

* How to use **Matplotlib** for line, bar, scatter, histogram, and pie charts.
* How to use **Seaborn** for statistical plots like barplot, boxplot, distplot, and regression plots.
* Compare both libraries based on:

  * Ease of use
  * Customization
  * Interactivity
  * Performance

---

## **Libraries Used**

This project uses the following Python libraries:

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

---

**Visualizations Included**

### Matplotlib Plots

* Line Plot
* Bar Chart
* Scatter Plot
* Histogram
* Pie Chart

### Seaborn Plots

* Bar Plot
* Box Plot
* Distribution Plot
* Regression Plot
* Pair Plot

Each plot includes:

* Description
* Use case
* Python code
* Graph output

---

## **Dataset Used**

This project uses a simple dataset containing:

| Month | Sales | Profit |
| ----- | ----- | ------ |
| Jan   | 150   | 20     |
| Feb   | 180   | 25     |
| Mar   | 220   | 30     |
| Apr   | 210   | 28     |
| May   | 260   | 35     |
| Jun   | 300   | 40     |

The dataset is created using:

```python
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [150, 180, 220, 210, 260, 300],
    "profit": [20, 25, 30, 28, 35, 40]
}
df = pd.DataFrame(data)
```

---

**Comparison: Matplotlib vs Seaborn**

| Feature       | Matplotlib         | Seaborn            |
| ------------- | ------------------ | ------------------ |
| Ease of Use   | Requires more code | Easier, high-level |
| Customization | Very flexible      | Good defaults      |
| Interactivity | Basic              | Basic              |
| Performance   | Fast               | Fast               |

---

## 📝 **Conclusion**

This project provides a beginner-friendly explanation of data visualization techniques.
By the end of this project, you will understand:

How to create different types of graphs
When to choose Matplotlib vs Seaborn
How to present data meaningfully
How to use visualizations in data analysis
## 📖 **Resources**

* Matplotlib Docs: [https://matplotlib.org/stable/users/explain/quick_start.html](https://matplotlib.org/stable/users/explain/quick_start.html)
* Seaborn Docs: [https://seaborn.pydata.org/tutorial/introduction.html](https://seaborn.pydata.org/tutorial/introduction.html)
