import os
from setuptools import setup
from distutils.core import Command


setup(
    name='mlbcolors',
    version='0.0.1',
    description="Easy access to the official colors of every team in Major League Baseball",
    author='Ben Welsh',
    author_email='ben.welsh@gmail.com',
    url='http://www.github.com/datadesk/mlbcolors',
    license="MIT",
    packages=("mlbcolors",),
    include_package_data=True,
    zip_safe=False,  # because we're including static files
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
