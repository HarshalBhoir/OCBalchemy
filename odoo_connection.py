"""
Odoo connection classes which describe how to connect to odoo
"""

from openerp import netsvc, api, SUPERUSER_ID
from openerp.modules.registry import RegistryManager


class Odoo8Context(object):
    """
    A context for connecting to a odoo 8 server with function to export .pot
    """

    def __init__(self, dbname):
        """
        Create context object.
        :param str dbname: database name with odoo installation
        """
        self.dbname = dbname

    def __enter__(self):
        """
        Context enter function.
        Temporarily add odoo 8 server path to system path and pop afterwards.
        Import odoo 8 server from path as library.
        Init logger, registry and environment.
        Add addons path to config.
        :returns Odoo8Context: This instance
        """
        netsvc.init_logger()
        registry = RegistryManager.new(self.dbname)
        self._environment_manage = api.Environment.manage()
        self._environment_manage.__enter__()
        self._cr = registry.cursor()
        self._uid = SUPERUSER_ID
        self._context = registry("res.users").context_get(self._cr, self._uid)
        self.env = api.Environment(self._cr, self._uid, self._context)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context exit function.
        Cleanly close environment manage and cursor.
        """
        self._environment_manage.__exit__(exc_type, exc_val, exc_tb)
        self._cr.close()
