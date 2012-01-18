# -*- coding: utf-8 -*-

from cromlech.io import IRequest
from cromlech.browser.interfaces import ILayout, ITemplate
from cromlech.i18n import ILanguage
from grokcore.component import baseclass, implements
from zope.component import queryMultiAdapter


def query_layout(request, context, interface=ILayout, name=''):
    assert interface.isOrExtends(ILayout)
    assert IRequest.providedBy(request)
    return queryMultiAdapter((request, context), interface, name=name)


def query_layout_template(layout, interface=ITemplate, name=""):
    """Returns a template associated to a view, or None.
    """
    assert ILayout.providedBy(view)
    assert interface.isOrExtends(ITemplate)
    return queryMultiAdapter((layout, layout.request), interface, name=name)


class Layout(object):
    """A layout object.
    """
    baseclass()
    implements(ILayout)

    template = None

    def __init__(self, request, context):
        self.context = context
        self.request = request

    def namespace(self):
        namespace = {}
        namespace['context'] = self.context
        namespace['request'] = self.request
        namespace['layout'] = self
        return namespace

    @property
    def target_language(self):
        return ILanguage(self.request, None)

    def update(self, *args, **kws):
        pass

    def render(self, content='', view=None, *args, **more):
        namespace = {'content': content, 'view': view}
        namespace.update(**more)
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(
            self, target_language=self.target_language, **namespace)
