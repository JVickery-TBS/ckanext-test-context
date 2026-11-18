from ckan.common import CKANConfig

import ckan.plugins as plugins
from ckan.lib.plugins import DefaultTranslation


class TestContextPlugin(plugins.SingletonPlugin, DefaultTranslation):
    """
    Custom plugin to mask user context via front-end interface.
    """
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITranslation, inherit=True)

    # IConfigurer
    def update_config(self, config: 'CKANConfig'):
        plugins.toolkit.add_template_directory(config, 'templates')
        plugins.toolkit.add_resource('assets', 'ckanext-test-context')

    # DefaultTranslation, ITranslation
    def i18n_domain(self) -> str:
        return 'ckanext-test-context'
