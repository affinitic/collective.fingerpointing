# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0a2.dev0'
description = 'Keep track of different events and write them down to an audit log.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='collective.fingerpointing',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone events subscribers log audit security',
    author='Héctor Velarde',
    author_email='hector.velarde@gmail.com',
    url='https://github.com/collective/collective.fingerpointing',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'plone.app.registry',
        'plone.directives.form',
        'plone.registry',
        'Products.CMFCore',
        'Products.CMFPlone >=4.2',
        'Products.CMFQuickInstallerTool',
        'Products.GenericSetup',
        'Products.PluggableAuthService',
        'setuptools',
        'zope.globalrequest',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'AccessControl',
            'plone.app.dexterity',
            'plone.app.iterate',
            'plone.app.robotframework',
            'plone.app.testing [robot] >=4.2.2',
            'plone.browserlayer',
            'plone.testing',
            'Products.PlonePAS',
            'robotsuite',
            'testfixtures',
            'zope.component',
            'zope.event',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
