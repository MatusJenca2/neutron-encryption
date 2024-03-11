from neutron_encryption.extensions import encryption
from oslo_log import log
_LOG = log.getLogger(__name__)

class EncryptionPluginDb(encryption.EncryptionPluginBase):
    pass


class EncryptionPluginRpcDbMixin(object):
    pass