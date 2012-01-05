# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = "0.2a1"
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.browser >= 0.3a2',
    'cromlech.i18n',
    'cromlech.io',
    'grokcore.component >= 2.4',
    'martian >= 0.14',
    'setuptools',
    'zope.component',
    'zope.interface',
    ]

tests_require = [
    'cromlech.browser [test]',
    ]

setup(
    name='dolmen.layout',
    version=version,
    author='Grok & Dolmen Teams',
    author_email='',
    url='http://gitweb.dolmen-project.org',
    download_url='http://pypi.python.org/pypi/dolmen.layout',
    description='Layout components for View rendering',
    long_description=readme + '\n\n' + history,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data = True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        },
    )
