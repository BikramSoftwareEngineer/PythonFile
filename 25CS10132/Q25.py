import matplotlib.pyplot as plt
import pandas as pd


data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [45000, 52000, 48000, 61000, 58000, 65000, 
              62000, 70000, 68000, 75000, 72000, 80000]
}

df = pd.DataFrame(data)


highest_sale = df.loc[df['Sales'].idxmax()]
lowest_sale = df.loc[df['Sales'].idxmin()]

print(f"--- Sales Analysis Summary ---")
print(f"Highest Sales: {highest_sale['Month']} with ₹{highest_sale['Sales']:,}")
print(f"Lowest Sales:  {lowest_sale['Month']} with ₹{lowest_sale['Sales']:,}\n")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


ax1.bar(df['Month'], df['Sales'], color='skyblue', edgecolor='navy')
ax1.set_title('Monthly Sales Revenue (Bar Chart)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (₹)')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.7)


ax2.plot(df['Month'], df['Sales'], marker='o', color='green', linewidth=2, markersize=6)
ax2.set_title('Monthly Sales Trend (Line Chart)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales (₹)')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, linestyle='--', alpha=0.7)


ax2.annotate(f"Highest: {highest_sale['Month']} (₹{highest_sale['Sales']})", 
             (highest_sale['Month'], highest_sale['Sales']),
             textcoords="offset points", xytext=(0,10), ha='center',
             arrowprops=dict(arrowstyle="->", color='red'))

ax2.annotate(f"Lowest: {lowest_sale['Month']} (₹{lowest_sale['Sales']})", 
             (lowest_sale['Month'], lowest_sale['Sales']),
             textcoords="offset points", xytext=(0,-15), ha='center',
             arrowprops=dict(arrowstyle="->", color='blue'))


plt.tight_layout()


plt.savefig('monthly_sales_analysis.png')
print("Visualizations saved successfully as 'monthly_sales_analysis.png'!")
plt.show()