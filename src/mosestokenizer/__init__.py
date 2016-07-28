"""Wrappers for several pre-processing scripts from the Moses toolkit.

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

__version__ = "0.2.5"

__all__ = [
    "MosesTokenizer",
    "MosesSentenceSplitter",
    "MosesPunctuationNormalizer",
]
