from neutron_encryption.db import encryption_db
import inspect
from oslo_log import log
_LOG = log.getLogger(__name__)
class EncryptionPlugin(encryption_db.EncryptionPluginDb):
    supported_extension_aliases = ["encryption"]
    path_prefix = "/encryption"


class EncryptionDriverPlugin(EncryptionPlugin):
    def __init__(self):
        super(EncryptionDriverPlugin,self).__init__()
        _LOG.info(f"EncryptionDriverPlugin inheritance tree:\n {inspect.getmro(EncryptionDriverPlugin)}")
    def get_plugin_type(self):
        return 'ENCRYPTION'
    def get_plugin_description(self):
        return 'Encryption service plugin'