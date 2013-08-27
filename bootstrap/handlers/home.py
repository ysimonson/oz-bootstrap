import base

class HomeHandler(base.BaseHandler):
    def get(self):
        return self.render("index.html")
