from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read() + '\n')

setup(
    name='robotframework-jsonschemalibrary',
    version=version,
    description="A Robot Framework library for JSON Schema validation.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Web Environment',
        'Framework :: Robot Framework',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='robotframework test json schema',
    author='Johannes Staffans',
    url='https://github.com/jstaffans',
    license='Apache License 2.0',
    packages=find_packages(
        exclude=['ez_setup', 'examples', 'tests']
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'robotframework',
        'jsonschema',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
