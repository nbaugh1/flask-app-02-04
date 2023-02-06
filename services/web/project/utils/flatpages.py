from flask_flatpages import FlatPages

FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

class FlatPages():
    def init():
        pages = FlatPages()
        
        return pages