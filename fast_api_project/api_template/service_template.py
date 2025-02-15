service_template = '''from common.database import db_manager
from apis.{{ service_name }}.queries.query import *

# Write Service for API in This Section To be Used in Router
class {{ router_name.capitalize() }}Service:
    pass

'''