# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from ga_app import VERSION
 
setup(
    name='ga-mobile-python',
    version='.'.join(map(str,VERSION)),
    description='Google Analytics Python Module',
    author='b1tr0t',
    author_email='',
    url='https://git@github.com:matinfo/ga-mobile-python.git',
    packages=['ga_app',],
    py_modules=['ga',]
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
