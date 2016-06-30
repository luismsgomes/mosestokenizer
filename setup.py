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
    version=get_version('mosestokenizer', '__init__.py'),
    description='Wrappers for several pre-processing scripts from the Moses toolkit.',
    long_description=read('README.rst'),
    url='https://bitbucket.org/luismsgomes/mosestokenizer',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='Other/Proprietary License',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='text tokenization pre-processing',
    install_requires=[
        "docopt",
        "toolwrapper",
    ],
    packages=['mosestokenizer'],
    package_dir={
        'mosestokenizer': 'mosestokenizer'
    },
    package_data={
        'mosestokenizer': [
            'tokenizer-v1.0.perl',
            'tokenizer-v1.1.perl',
            'split-sentences.perl',
            'normalize-punctuation.perl',
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
