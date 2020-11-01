from setuptools import setup
import sys

required = ['sanic']
long_description = ""
with open('README.md') as f:
    long_description += f.read()

setup(
    name='SanicApiKey',
    version='1.0.1',
    description='Basic Sanic API Key plugin.',
    long_description=long_description,
    author='Yusuf Usta',
    author_email='yusuf@fusuf.codes',
    maintainer='Yusuf Usta',
    maintainer_email='yusuf@fusuf.codes',
    url='https://github.com/quiec/SanicApiKey',
    license='GPL3',
    packages=['SanicApiKey'],
    install_requires=required,
    keywords=['sanic'],
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)