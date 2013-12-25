
try:
    from HTMLParser import HTMLParser
except:
    from html.parser import HTMLParser


class Resource(HTMLParser):
    def __init__(self, mobi):
        super(Resource, self).__init__()
        self.mobi = mobi
