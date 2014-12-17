import base
import tornado

class HomeHandler(base.BaseHandler):
    def get(self):
        return self.render("index.html")

class NotFoundHandler(base.BaseHandler):
    """
    Handler intended to catch all invalid paths. This way we raise a
    404 exception and show the appropriate not found error page.
    """

    def get(self, path):
        raise tornado.web.HTTPError(404)
