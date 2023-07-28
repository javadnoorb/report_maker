
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from classes.tab import Tab
from classes.report import Report

# Create some random data for the first tab
data1 = np.random.randn(50)
data2 = np.random.randn(50)

# Create a DataFrame for the first tab
df = pd.DataFrame({
    'data1': data1,
    'data2': data2
})

# Create a matplotlib figure for the first tab
fig, ax = plt.subplots()
ax.plot(df['data1'], label='data1')
ax.plot(df['data2'], label='data2')
ax.legend()

# Get the HTML for the first DataFrame
df_html = df.to_html()

# Create a tab for the first tab
tab1 = Tab("Tab 1")

# Add text, figure, and dataframe to the first tab
tab1.add_text("This is some text.")
tab1.add_figure(fig, caption="This is figure 1.", dpi=80)
tab1.add_dataframe(df_html, caption="This is table 1.")

# Create some more random data for the second tab
data3 = np.random.randn(50)
data4 = np.random.randn(50)

# Create another DataFrame for the second tab
df2 = pd.DataFrame({
    'data3': data3,
    'data4': data4
})

# Create another matplotlib figure for the second tab
fig2, ax2 = plt.subplots()
ax2.plot(df2['data3'], label='data3')
ax2.plot(df2['data4'], label='data4')
ax2.legend()

# Get the HTML for the second DataFrame
df2_html = df2.to_html()

# Create a tab for the second tab
tab2 = Tab("Tab 2")

# Add different text, figure, and dataframe to the second tab
tab2.add_text("This is some different text.")
tab2.add_figure(fig2, caption="This is a different figure.", dpi=80)
tab2.add_dataframe(df2_html, caption="This is a different table.")

# Create a report
report = Report("My Report")

# Add the tabs to the report
report.add_tab(tab1)
report.add_tab(tab2)

# Generate the HTML for the report
report_html = report.generate_html()

# Write the HTML to a file
with open('final_report.html', 'w') as f:
    f.write(report_html)
