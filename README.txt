This CKAN Extension encapsulates modifications for CKAN required for the DataNL project.

To install this package, from your CKAN virtualenv, run the following from your CKAN base folder (e.g. ``pyenv/``)::

 pip install -e hg+https://okfn@bitbucket.org/okfn/ckanext-datanl#egg=ckanext-datanl 

You'll also want the Solr extension::

 pip install -e hg+https://okfn@bitbucket.org/okfn/ckanext-solr#egg=ckanext-solr

Then activate these two extensions by puttin ``ckan.plugins = datanl
synchronous_search`` in your main ``ini``-file.
