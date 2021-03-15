#!/usr/bin/env python

import flog

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    "flog",
]

requires = []

setup(
    name="flog",
    version=flog.__version__,
    description=flog.__description__,
    long_description=open("README.rst").read(),
    author="Chris McGraw",
    author_email="mitgr81+flog@mitgr81.com",
    url="https://github.com/mitgr81/flog",
    test_suite="flog.tests",
    packages=packages,
    package_dir={"flog": "flog"},
    package_data={"": ["LICENSE", "README.rst"]},
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    # classifiers=(
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: System Administrators',
    #     'Natural Language :: English',
    #     'License :: OSI Approved :: MIT License',
    #     "Operating System :: OS Independent",
    #     "Development Status :: 4 - Beta",
    #     "Topic :: System :: Logging",
    #     'Programming Language :: Python',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3.5',
    # ),
)
