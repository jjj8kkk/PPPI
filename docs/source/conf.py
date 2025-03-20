import os
import sys

project = 'BPMN'
copyright = '2025, Anton'
author = 'Anton'
release = '1.0.0'

sys.path.insert(0, os.path.abspath('../..'))  # Два уровня вверх от docs/source

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': False,
    'inherited-members': False,
    'show-inheritance': True,
}
html_theme = 'sphinx_rtd_theme'
templates_path = ['_templates']
exclude_patterns = []


html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

try:
    import main
    print("✅ Модуль main успешно импортирован")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")