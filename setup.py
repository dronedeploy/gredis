#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function, division

from gredis import version

from setuptools import setup

setup(
    name="gredis",
    version=version,
    packages=["gredis"],
    package_data={
    },
    author="cold,dd",
    author_email="",
    url="https://github.com/dronedeploy/gredis",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description=("gRedis is an asynchronous client library of Redis written with Tornado coroutine."),
    long_description=open("README.rst").read(),
    install_requires=["tornado==5.1.1", "redis==2.10.6"],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        ],
)
