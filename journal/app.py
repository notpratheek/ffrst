from flask import Flask, render_template
from flask_flatpages import FlatPages
import settings

app = Flask(__name__)
app.config.from_object(settings)
pages = FlatPages(app)


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/tag/<string:tag>')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path).html
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.run(port=8000)
