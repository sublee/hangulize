import os
import os.path as p
import re


def get_list():
    """Returns the supported language code list."""
    ext = p.extsep + 'py'
    init = '__init__' + ext
    def _get_list(prefix='', path=None):
        path = path or p.dirname(__file__)
        # helpers
        name = lambda x: prefix + re.sub(re.escape(ext) + '$', '', x)
        def is_lang(x):
            if x.startswith(init):
                return False
            x = p.join(path, x)
            return p.isdir(x) and p.isfile(p.join(x, init)) or \
                   p.isfile(x) and x.endswith(ext)
        # find top-level language modules
        langs = [name(x) for x in os.listdir(path) if is_lang(x)]
        # find sub language modules
        for lang in langs:
            _path = p.join(path, lang)
            if p.isdir(_path):
                langs += _get_list(prefix=lang + '.', path=_path)
        langs.sort()
        return langs
    return _get_list()
