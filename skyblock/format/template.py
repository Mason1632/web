from os import walk
from pathlib import Path

from .._lib import _open
from ..function.file import load_folder
from ..function.io import *
from ..path import join_path


__all__ = ['TEMPLATES', 'get_template']

if not Path(join_path('skyblock', 'data', 'templates')).is_dir():
    raise FileNotFoundError(
        'Required data not found.\n'
        'Restart skyblock to fix it automatically.'
    )

TEMPLATES = {}
for category in [*walk(join_path('skyblock', 'data', 'templates'))][0][1]:
    TEMPLATES[category] = {}
    for subpath, folders, file_names in walk(join_path('skyblock', 'data', 'templates', category)):
        for file_name in file_names:
            if not file_name.endswith('.txt'):
                continue

            with _open(join_path(subpath, file_name)) as file:
                TEMPLATES[category][file_name[:-4]] = file.read()


def get_template(category: str, name: str, /, *, warn=True) -> str | None:
    if category not in TEMPLATES:
        if warn:
            red(f'Template category not found: {category!r}')
    elif name not in TEMPLATES[category]:
        if warn:
            red(f'Template not found: {name!r}')
    else:
        return TEMPLATES[category][name]
