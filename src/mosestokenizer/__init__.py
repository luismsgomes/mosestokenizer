"""
Wrappers for several pre-processing scripts from the Moses toolkit.

Copyright ® 2016, Luís Gomes <luismsgomes@gmail.com>

This package provides wrappers for the following Perl scripts:

``tokenizer.perl``
    class `mosestokenizer.tokenizer.MosesTokenizer`

``split-sentences.perl``
    class `mosestokenizer.sentsplitter.MosesSentenceSplitter`

``normalize-punctuation.perl``
    class `mosestokenizer.punctnormalizer.MosesPunctuationNormalizer`

"""

from mosestokenizer.tokenizer import MosesTokenizer
from mosestokenizer.sentsplitter import MosesSentenceSplitter
from mosestokenizer.punctnormalizer import MosesPunctuationNormalizer

__version__ = "0.3.0"

__all__ = [
    "MosesTokenizer",
    "MosesSentenceSplitter",
    "MosesPunctuationNormalizer",
]
