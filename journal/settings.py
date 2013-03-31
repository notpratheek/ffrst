import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.rst'
FLATPAGES_HTML_RENDERER = 'utils:restructuredtext_filter'
