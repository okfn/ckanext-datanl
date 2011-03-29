This CKAN Extension encapsulates modifications for CKAN required for the DataNL project.

To install this package, from your CKAN virtualenv, run the following from your CKAN base folder (e.g. ``pyenv/``)::

 pip install -e hg+https://okfn@bitbucket.org/okfn/ckanext-datanl

Then activate it by setting ``ckan.plugins = datanl
synchronous_search`` in your main ``ini``-file.
