from flask_flatpages import FlatPages

class FlatPages():
    def init(app):
        flatpages = FlatPages(app)
        
        return flatpages