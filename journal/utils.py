from docutils.core import publish_parts
from flask import current_app
from jinja2.filters import do_mark_safe

__all__ = ('restructuredtext_filter', )


def restructuredtext_filter(text, mixed=None):
    app = current_app
    docutils_settings = app.config.get('RESTRUCTUREDTEXT_FILTER_SETTINGS', {})
    result = (mixed
                if mixed is not None and isinstance(mixed, basestring)
                else 'fragment')
    writer = app.config.get('RESTRUCTUREDTEXT_WRITER_NAME', 'html4css1')
    parts = publish_parts(source=text, writer_name=writer,
            settings_overrides=docutils_settings)
    return do_mark_safe(parts[result])
