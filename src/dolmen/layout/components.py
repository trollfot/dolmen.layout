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

    def __init__(self, request, context):
        self.context = context
        self.request = request 
        self.push_in = dict()

    def namespace(self):
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['layout'] = self
        namespace.update(self.push_in)
        return namespace

    def update(self, *args, **extra):
        if extra: self.push_in = extra

    def render(self, content='', *args, **extra):
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(self, **{'content': content})

    def __call__(self, content='', *args, **extra):
        self.update(**extra)
        self.response = self.responseFactory()
        self.response.write(self.render(content) or u'')
        return self.response
