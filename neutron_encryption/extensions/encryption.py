
import abc
from neutron_lib.plugins import constants as nconstants
from neutron_lib.services import base as service_base
from neutron_lib.api import extensions as api_extensions
from neutron_lib.plugins import directory
from neutron.api.v2 import base
from neutron.quota import resource_registry
from neutron_lib.db import constants as db_const
from neutron.extensions import standardattrdescription as stdattr_ext
from neutron.api import extensions
from oslo_log import log
_LOG = log.getLogger(__name__)

_LOG.info("TEST: Encryption extension loaded")

RESOURCE_ATTRIBUTE_MAP = {
    'encryptions' : {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_visible': True,
               'is_filter': True,
               'is_sort_key': True,
               'primary_key': True},
        'name': {'allow_post': True, 'allow_put': True,
                 'is_visible': True, 'default': '', 'is_filter': True,
                 'is_sort_key': True,
                 'validate': {
                     'type:name_not_default': db_const.NAME_FIELD_SIZE}},
    }

}

class Encryption(api_extensions.ExtensionDescriptor):
    def get_plugin_interface(self):
        _LOG.info(f"TEST PLUGIN BASE")
        return EncryptionPluginBase

    def get_name(self):
        return "encryption"
    def get_alias(self):
        return "encryption"
    def get_description(self):
        return "The encryption extension."
    def get_updated(self):
        return "2022-03-14T15:00:00-00:00"
    def get_resources(self):
        """Returns Ext Resources."""
        exts = []
        plugin = directory.get_plugin()
        resource_name = 'encryption'
        collection_name = "encryption"
        params = RESOURCE_ATTRIBUTE_MAP.get("encryptions", dict())
        resource_registry.register_resource_by_name(resource_name)
        controller = base.create_resource(collection_name,
                                            resource_name,
                                            plugin, params, allow_bulk=True,
                                            allow_pagination=True,
                                            allow_sorting=True)

        ex = extensions.ResourceExtension(collection_name,
                                            controller,
                                            attr_map=params)
        exts.append(ex)
        _LOG.info("TEST: get API resources ")
        return exts

    def update_attributes_map(self, attributes):
        _LOG.info("TEST3: updating attributes map")
        super(Encryption, self).update_attributes_map(
            attributes, extension_attrs_map=RESOURCE_ATTRIBUTE_MAP)
    def get_extended_resources(self, version):
        return {}
    def get_required_extensions(self):
        return [stdattr_ext.Standardattrdescription.get_alias()]


class EncryptionPluginBase:
    def get_plugin_type(self):
        return 'ENCRYPTION'
    def get_plugin_description(self):
        return 'Encryption service plugin'
