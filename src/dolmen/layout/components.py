# -*- coding: utf-8 -*-

from grokcore.component import baseclass, implements
from cromlech.browser.interfaces import ILayout


class Layout(object):
    """A layout object.
    """
    baseclass()
    implements(ILayout)

    template = None
    responseFactory = None

    def __init__(self, context, request):
        self.context = context
        self.request = request 

    def namespace(self):
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['layout'] = self
        return namespace

    def update(self, **kwargs):
        pass

    def render(self, content):
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self, **{'content': content})

    def __call__(self, content):
        self.update()
        self.response = self.responseFactory()
        self.response.write(self.render(content) or u'')
        return self.response
