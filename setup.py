# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(
        os.path.join(
            os.path.join(os.path.dirname(__file__), 'docs'),
            *rnames)).read()

version = 0.1
long_description = read('README.txt') + '\n' + read('CHANGES.txt')

install_requires = [
    'cromlech.io',
    'cromlech.browser',
    'grokcore.component >= 2.4',
    'martian >= 0.14',
    'setuptools',
    'zc.buildout',
    'zope.component',
    'zope.interface',
    ]

tests_require = [
    'WebOb',
    'zope.configuration',
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
    long_description=long_description,
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
