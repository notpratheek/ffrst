from flask import Flask, render_template
from flask_flatpages import FlatPages
from pygments.formatters import HtmlFormatter

import sourcecode
import settings

app = Flask(__name__)
app.config.from_object(settings)
pages = FlatPages(app)


@app.route('/pygments.css')
def pygments_css():
    formatter = HtmlFormatter(style='tango')
    styles = formatter.get_style_defs('.highlight')
    return styles, 200, {'Content-Type': 'text/css'}


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/tag/<string:tag>')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run(port=8000)
