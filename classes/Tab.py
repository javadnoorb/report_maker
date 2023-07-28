
from io import BytesIO
import base64

class Tab:
    def __init__(self, title):
        self.title = title
        self.contents = []

    def add_text(self, text):
        self.contents.append(('text', text))

    def add_figure(self, fig, caption="", dpi=80):
        buf = BytesIO()
        fig.savefig(buf, format='png', dpi=dpi)
        buf.seek(0)
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
        tab_html = f'''
        <div>
            <h2>{self.title}</h2>
            {contents_html}
        </div>
        '''
        return tab_html
