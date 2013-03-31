from flask import Flask
from flask_flatpages import FlatPages
import settings

app = Flask(__name__)
app.config.from_object(settings)
pages = FlatPages(app)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == '__main__':
    app.run(port=8000)
