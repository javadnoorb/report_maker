import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class Tab:
    def __init__(self, title):
        self.title = title
        self.contents = []

    def add_text(self, text):
        self.contents.append(('text', text))

    def add_figure(self, fig, caption="", dpi=80):
        # Convert the Matplotlib figure to an image in memory
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=dpi)
        buf.seek(0)

        # Convert the image to Base64 and create a data URL
        img_str = base64.b64encode(buf.read()).decode()
        img_data_url = f"data:image/png;base64,{img_str}"

        self.contents.append(('figure', (img_data_url, caption)))

    def add_dataframe(self, df_html, caption=""):
        self.contents.append(('dataframe', (df_html, caption)))

    def generate_html(self):
        contents_html = ""
        for content_type, content in self.contents:
            if content_type == 'text':
                contents_html += f"<p>{content}</p>"
            elif content_type == 'figure':
                img_data_url, caption = content
                contents_html += f'<figure><img src="{img_data_url}" alt="figure"><figcaption>{caption}</figcaption></figure>'
            elif content_type == 'dataframe':
                df_html, caption = content
                contents_html += f'<div style="height: 300px; overflow: auto;">{df_html}</div><p>{caption}</p>'
        tab_html = f"""
        <div>
            <h2>{self.title}</h2>
            {contents_html}
        </div>
        """
        return tab_html

class Report:
    def __init__(self, title):
        self.title = title
        self.tabs = []

    def add_tab(self, tab):
        self.tabs.append(tab)

    def generate_html(self):
        tabs_html = "\n".join([f'<button class="tablinks" onclick="openTab(event, \'Tab{i+1}\')">Tab {i+1}</button>' for i, tab in enumerate(self.tabs)])
        tab_contents_html = "\n".join([f'<div id="Tab{i+1}" class="tabcontent">\n{tab.generate_html()}\n</div>' for i, tab in enumerate(self.tabs)])
        html = f"""
        <html>
        <head>
            <title>{self.title}</title>
            <style>
                .tabcontent {{
                    display: none;
                }}
                .tablinks.active, .tab:hover {{
                    background-color: #ddd;
                }}
            </style>
            <script>
                function openTab(event, tabName) {{
                    var i, tabcontent, tablinks;
                    tabcontent = document.getElementsByClassName("tabcontent");
                    for (i = 0; i < tabcontent.length; i++) {{
                        tabcontent[i].style.display = "none";
                    }}
                    tablinks = document.getElementsByClassName("tablinks");
                    for (i = 0; i < tablinks.length; i++) {{
                        tablinks[i].className = tablinks[i].className.replace(" active", "");
                    }}
                    document.getElementById(tabName).style.display = "block";
                    event.currentTarget.className += " active";
                }}
            </script>
        </head>
        <body>
            <h1>{self.title}</h1>
            {tabs_html}
            {tab_contents_html}
            <script>
                // Get the element with id="defaultOpen" and click on it
                document.getElementsByClassName("tablinks")[0].click();
            </script>
        </body>
        </html>
        """
        return html

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
