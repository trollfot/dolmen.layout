# -*- coding: utf-8 -*-

from cromlech.io.directives import request
from grokcore.component import provides, name, context
from dolmen.layout.components import Layout
from cromlech.browser.interfaces import ILayout
from dolmen.layout.decorator import layout, query_layout

# Import this module so that it's available as soon as you import the
# 'dolmen.view' package.  Useful for tests and interpreter examples.
import dolmen.layout.testing
