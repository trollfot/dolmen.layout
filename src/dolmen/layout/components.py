# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import ILayout
from cromlech.i18n import ILanguage
from grokcore.component import baseclass, implements


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

    @property
    def target_language(self):
        return ILanguage(self.request, None)

    def update(self, *args, **extra):
        if extra:
            self.push_in = extra

    def render(self, content='', *args, **extra):
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(
            self, target_language=self.target_language, **{'content': content})

    def __call__(self, content='', *args, **extra):
        self.update(**extra)
        self.response = self.responseFactory()
        self.response.write(self.render(content) or u'')
        return self.response
