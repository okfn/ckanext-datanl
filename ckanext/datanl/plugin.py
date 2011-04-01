import os
from logging import getLogger

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IConfigurer

log = getLogger(__name__)


class DataNLPlugin(SingletonPlugin):
    implements(IConfigurer, inherit=True)

    def update_config(self, config):
        """This IConfigurer implementation causes CKAN to look in the
        ```public``` and ```templates``` directories present in this
        package for any customisations, plus some other settings.
        """
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        our_public_dir = os.path.join(rootdir, 'ckanext',
                                      'datanl', 'theme', 'public')
        template_dir = os.path.join(rootdir, 'ckanext',
                                    'datanl', 'theme',
        'templates')
        # set our local template and resource overrides
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])
        # set the title and other standard bits
        config['ckan.site_title'] = "Overheid.nl"
        config['ckan.site_logo'] = "http://www.overheid.nl/presentatie/images/overheid.nl.png"
        config['ckan.site_id'] = "nl.ckan.net"
        config['lang'] = "nl"
        config['ckan.site_url'] = ""

        # solr config
        config['search_backend'] = "solr"
        #config['solr_url'] = "http://eu4-int.okfn.org:8080/solr/ckan"

        # default permissions
        config['ckan.default_roles.Package'] = \
                 ('{"visitor": ["reader"], '
                  '"logged_in": ["reader"]}')
