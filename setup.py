__version__ = '1'

from setuptools import setup, Extension, find_packages
import sys, os
import textwrap


setup(
    name="SchevoCookbook",

    version=__version__,

    description="Recipes and complete meals for the Schevo DBMS",

    long_description=textwrap.dedent("""
    SchevoCookbook provides database schema and database usage examples
    showing specific patterns ("recipes") and mini-apps ("complete meals").

    You can also get the `latest development version
    <http://getschevo.org/hg/repos.cgi/schevocookbook-dev/archive/tip.tar.gz#egg=SchevoCookbook-dev>`__.
    """),

    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database :: Database Engines/Servers',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    keywords='database dbms',

    author='Orbtech, L.L.C. and contributors',
    author_email='schevo@googlegroups.com',

    url='http://getschevo.org/schevocookbook/',

    license='LGPL',

    platforms=['UNIX', 'Windows'],

    packages=find_packages(exclude=['doc', 'tests']),

    include_package_data=True,

    zip_safe=False,

    install_requires=[
    'Schevo >= 3.1a1',
    ],

    tests_require=[
    'nose >= 0.10.1',
    ],
    test_suite='nose.collector',

    extras_require={
    },

    dependency_links = [
    ],

    entry_points = """
    """,
    )
