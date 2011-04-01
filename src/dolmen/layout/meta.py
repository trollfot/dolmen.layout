# -*- coding: utf-8 -*-

import martian
import zope.component
import grokcore.component
from cromlech.io import directives
from cromlech.browser.interfaces import ILayout
from dolmen.layout import Layout


class LayoutGrokker(martian.ClassGrokker):
    martian.component(Layout)
    martian.directive(grokcore.component.context)
    martian.directive(directives.request)
    martian.directive(grokcore.component.provides, default=ILayout)
    martian.directive(grokcore.component.name)
    
    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        return super(LayoutGrokker, self).grok(
            name, factory, module_info, **kw)

    def execute(self, factory, config, context, request, provides, name, **kw):
        adapts = (request, context)
        config.action(
            discriminator=('adapter', adapts, provides),
            callable=zope.component.provideAdapter,
            args=(factory, adapts, provides, name),
            )
        return True
