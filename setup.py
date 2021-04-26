import os
import re

import setuptools

with open(os.path.join("ms_login", "__init__.py"), encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name="ms-login",
    version=version,
    author="Zeke Marffy",
    author_email="zmarffy@yahoo.com",
    packages=setuptools.find_packages(),
    url='https://github.com/zmarffy/ms-login',
    license='MIT',
    description='Library that allows logging into Microsoft accounts via requests',
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
        install_requires=[
        'requests',
        'bs4'
    ],
)
