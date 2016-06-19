"""Wrappers for several pre-processing scripts from the Moses toolkit.

This package provides wrappers for the following Perl scripts:

``tokenizer.perl``
    class `mosestokenizer.tokenizer.MosesTokenizer`

``split-sentences.perl``
    class `mosestokenizer.sentsplitter.MosesSentenceSplitter`

``normalize-punctuation.perl``
    class `mosestokenizer.punctnormalizer.MosesPunctuationNormalizer`

"""

from .tokenizer import MosesTokenizer
from .sentsplitter import MosesSentenceSplitter
from .punctnormalizer import MosesPunctuationNormalizer

__version__ = "0.2.0"

"""Semantic versioning (major.minor.patch)

Increment the:

- *major* version when you make incompatible API changes,
- *minor* version when you add functionality in a backwards-compatible manner, and
- *patch* version when you make backwards-compatible bug fixes.

"""
