# -*- coding: utf-8 -*-

from cromlech.browser.interfaces import ILayout, IRenderer
from zope.interface.interfaces import IInterface
from zope.component import getMultiAdapter


def query_layout(request, context, interface=ILayout, name=''):
    return getMultiAdapter((request, context), interface, name=name)


class layout(object):

    def __init__(self, interface=None, layout=None, name=""):
        if not (interface is None) ^ (layout is None):
            raise AssertionError(
                "You must pass in an interface or a component, not both.")

        if interface is not None:
            assert IInterface.providedBy(interface)
            assert interface.isOrExtends(IRenderer)
        elif layout is None:
            assert ILayout.implementedBy(layout)
        
        self.interface = interface
        self.layout = layout
        self.name = name
 
    def __call__(self, func):
        
        def render(view, *args, **kwargs):

            if self.interface is not None:
                layout = query_layout(
                    view.request, view.context, self.interface, self.name)
                return layout.render(func(view, *args, **kwargs))

            return self.layout(view.request, view.context).render(
                func(view, *args, **kwargs))

        return render
