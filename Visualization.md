# Visualization: Visitors by Web Traffic Sources

## 1. Description

The bar chart above displays the number of visitors, in thousands, categorized by web traffic sources (Searches, Direct, Social Media) over a period of five months (from July 2019 to November 2019).

- **Y-axis**: Number of visitors (in thousands)
- **X-axis**: Months
- **Legend**: 
    - Blue = Searches
    - Pink = Direct
    - Orange = Social Media

## 2. Data Table

| Month    | Searches | Direct | Social Media |
|----------|----------|--------|-------------|
| 07/2019  | 50       | 39     | 70          |
| 08/2019  | 53       | 47     | 80          |
| 09/2019  | 59       | 42     | 90          |
| 10/2019  | 56       | 51     | 87          |
| 11/2019  | 62       | 51     | 92          |

## 3. Insights

- Social Media consistently delivers the highest number of visitors, with a steady increase over the months.
- Searches show a moderate increase, while Direct traffic remains relatively stable.
- The highest visitor count from any source is Social Media in November 2019 (92,000 visitors).

## 4. Programmatic Generation (Python Example)

Below is an example Python script using `matplotlib` and `pandas` to generate this visualization:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

df = pd.DataFrame({
    'Searches': searches,
    'Direct': direct,
    'Social Media': social_media
}, index=months)

# Plot
ax = df.plot(kind='bar', figsize=(10,6), color=['#4B9CD3', '#D36E9B', '#F5B942'])
plt.title('Visitors by web traffic sources')
plt.xlabel('months')
plt.ylabel('visitors in thousands')
plt.xticks(rotation=0)
plt.legend(title=None)
plt.tight_layout()
plt.show()
```

## 5. Screenshot

Below is the screenshot of the generated visualization from the program:

![image1](image1)
