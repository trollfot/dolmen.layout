"""
Layout
******

Let's first grok the meta module to define some basic grokkers::

  >>> import dolmen.layout
  >>> dolmen.layout.testing.grok('dolmen.layout.meta')


Define a model and a request
============================

  >>> mammoth = object()
  >>> request = object()


Define a layout
===============

  >>> from zope.interface import Interface
  >>> from grokcore.component import testing

  >>> class DefaultLayout(dolmen.layout.Layout):
  ...     dolmen.layout.context(Interface)
  ...     
  ...     def render(self, content):
  ...         return u"I am the layout for %r. This is easy" % content

  >>> testing.grok_component('default', DefaultLayout)
  True

Define a view
=============

  >>> class SimpleView(object):
  ...
  ...     def __init__(self, context, request):
  ...         self.context = context
  ...         self.request = request
  ...
  ...     @dolmen.layout.layout(dolmen.layout.ILayout)
  ...     def render(self):
  ...         return u"a simple view rendering %r" % self.context

  >>> print SimpleView(mammoth, request).render()

"""
