# -*- coding: utf-8 -*-
"""
Hangulize
~~~~~~~~~

This module provides Korean Alphabet Transcription.
"""
from setuptools import setup


setup(
    name='hangulize',
    version='0.0.1',
    license='BSD',
    author='Lee Heung-sub',
    author_email='heung@sublee.kr',
    description='Korean Alphabet Transcription',
    long_description=__doc__,
    zip_safe=False,
    test_suite="test",
    platforms='any',
    packages=['hangulize'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ]
)

