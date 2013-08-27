"""
Defines the base controller that all of the bootstrap controllers inherit from
"""

import oz
from bootstrap import middleware

class BaseHandler(oz.RequestHandler, middleware.BoostrapMiddleware):
    pass
