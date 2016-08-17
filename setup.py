from setuptools import setup, find_packages
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='mosestokenizer',
    version=get_version('src', 'mosestokenizer', '__init__.py'),
    description='Wrappers for several pre-processing scripts from the Moses'
                ' toolkit.',
    long_description=read('README.rst'),
    url='https://bitbucket.org/luismsgomes/mosestokenizer',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='LGPLv2',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: GNU Lesser General Public License v2'
            ' or later (LGPLv2+)',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='text tokenization pre-processing',
    install_requires=[
        "docopt",
        "openfile",
        "toolwrapper",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'mosestokenizer': [
            '*.perl',
            'nonbreaking_prefixes/*.*'
        ],
    },
    entry_points={
        'console_scripts': [
            'moses-tokenizer=mosestokenizer.tokenizer:main',
            'moses-punct-normalizer=mosestokenizer.punctnormalizer:main',
            'moses-sent-splitter=mosestokenizer.sentsplitter:main'
        ],
    },
)
