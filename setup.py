#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages
from bar_plot.version import get_version

setup(
    name='bar-plot-r-plugin',
    version=get_version(),
    description='An choppy plugin to draw an interactive bar plot.',
    long_description='The bar plot plugin will draw an interactive bar plot by using ggplot2 library.',
    keywords='choppy, plugin, bar-plot, interactive',
    url='https://choppy.3steps.cn/go-choppy/bar-plot-r-plugin/',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.5',
    include_package_data=True,
    install_requires=[
        'mk-media-extension>=0.1.0'
    ],
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
        'choppy.plugins': [
            'bar-plot-r = bar_plot.bar_plot:BarPlotRPlugin'
        ]
    }
)
