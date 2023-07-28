
class Report:
    def __init__(self, title):
        self.title = title
        self.tabs = []

    def add_tab(self, tab):
        self.tabs.append(tab)

    def generate_html(self):
        tabs_html = "\n".join([f'<button class="tablinks" onclick="openTab(event, \'Tab{i+1}\')">Tab {i+1}</button>' for i, tab in enumerate(self.tabs)])
        tab_contents_html = "\n".join([f'<div id="Tab{i+1}" class="tabcontent">\n{tab.generate_html()}\n</div>' for i, tab in enumerate(self.tabs)])
        html = f'''
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
        '''
        return html
