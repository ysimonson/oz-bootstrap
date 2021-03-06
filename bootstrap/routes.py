"""Defines application routes"""

import oz
from bootstrap.handlers import home

oz.routes(
    # Format: (<path>, <handler>, [dict(<request handler kwargs>)])
    # e.g.: (r"^/hello/(\w+)$", handlers.GreetingHandler)
    (r"^/$", home.HomeHandler),
    (r"^(.+)$", home.NotFoundHandler),
)