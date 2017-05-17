from __future__ import unicode_literals

import os
import sys

sys.path.append(os.path.abspath('..'))

extensions = []

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'django-user-messages'
copyright = '2017 Feinheit AG'

version = __import__('user_messages').__version__
release = version

pygments_style = 'sphinx'

html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'djangousermessagesdoc'

latex_documents = [(
    'index',
    'djangousermessages.tex',
    'django-user-messages Documentation',
    'Feinheit AG',
    'manual',
)]

man_pages = [(
    'index',
    'djangouser-messages',
    'django-user-messages Documentation',
    ['Feinheit AG'],
    1,
)]

texinfo_documents = [(
    'index',
    'djangousermessages',
    'django-user-messages Documentation',
    'Feinheit AG',
    'djangousermessages',
    'Offline addon for django.contrib.messages',
    'Miscellaneous',
)]
