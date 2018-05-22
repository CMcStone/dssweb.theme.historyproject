# -*- coding: utf-8 -*-
"""
This module contains the tool of dssweb.theme.histproj
"""
import os
from setuptools import setup, find_packages

version = '1.0.0'

setup(name='dssweb.theme.histproj',
      version=version,
      description="plone theme based on Quintagroup.theme.sunrain",
      long_description=open(os.path.join("dssweb", "theme", "histproj", "README.txt")).read() + "\n\n" +
                       open(os.path.join("docs", "INSTALL.rst")).read() + "\n\n"+
                       open(os.path.join("docs", "HISTORY.rst")).read(),    

      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='web zope plone theme diazo ',
      author='dssweb',
      author_email='cbeck@ucdavis.edu',
      url='http://tbd',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb', 'dssweb.theme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'plone.app.theming',
                        'plone.app.themingplugins',
                        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
