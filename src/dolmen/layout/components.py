# -*- coding: utf-8 -*-

from cromlech.browser import IRequest, ILayout, ITemplate
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
    assert ILayout.providedBy(layout)
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

    def namespace(self, **extra):
        namespace = {
            'context': self.context,
            'request': self.request,
            'layout': self,
            }
        namespace.update(extra)
        return namespace

    @property
    def target_language(self):
        return ILanguage(self.request, None)

    def __call__(self, content, **namespace):
        environ = self.namespace(**namespace)
        environ['content'] = content
        if self.template is None:
            raise NotImplementedError("Template is not defined.")
        return self.template.render(
            self, target_language=self.target_language, **environ)
