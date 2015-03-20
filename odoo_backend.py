#!/usr/bin/env python2

# Import as private to hide all but env
from openerp import netsvc as _netsvc, api as _api, SUPERUSER_ID as _uid
from openerp.modules.registry import RegistryManager as _RegistryManager

# Name of database to use
_db = 'test'

# Initialize logger
_netsvc.init_logger()

# Get registry / init database
_registry = _RegistryManager.get(_db, update_module=False)

# Assign to variable to avoid garbage collection
_gen_context = _api.Environment.manage().gen
_gen_context.next()

# Get psycopg cursor
_cr = _registry.cursor()

# Get a context from admin
_context = _registry('res.users').context_get(_cr, _uid)

# Get a v8 env
env = _api.Environment(_cr, _uid, _context)
