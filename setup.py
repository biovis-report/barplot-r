#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from barplot.version import get_version

setup(
    name='barplot-r',
    version=get_version(),
    description='An biovis plugin to draw an interactive bar plot.',
    long_description='The barplot plugin will draw an interactive bar plot by using ggplot2 library.',
    keywords='biovis-plugin, barplot, interactive',
    url='https://github.com/biovis-report/barplot-r',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.5',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'biovis.plugins': [
            'barplot-r = barplot.barplot:BarPlotRPlugin'
        ]
    }
)
