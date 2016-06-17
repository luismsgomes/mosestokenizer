"""A module for interfacing with Philipp Koehn's ``tokenizer.perl``.

Command line::

    Usage:
        mosestokenizer [options] <lang> [<inputfile> [<outputfile>]]

    Options:
        --selftest  Run selftests.

2016, Luís Gomes <luismsgomes@gmail.com>
"""

__version__ = "0.1.0"

"""Semantic versioning (major.minor.patch)

Increment the:

- *major* version when you make incompatible API changes,
- *minor* version when you add functionality in a backwards-compatible manner, and
- *patch* version when you make backwards-compatible bug fixes.

"""


from docopt import docopt
from doctest import testmod
from os import path
from toolwrapper import ToolWrapper
import sys


class MosesTokenizer(ToolWrapper):
    """A wrapper for the Philipp Koehn's tokenizer.

    This class communicates with tokenizer.pl process via pipes. When the
    MosesTokenizer object is no longer needed, the close() method should be
    called to free system resources. The class supports the context manager
    interface. If used in a with statement, the close() method is invoked
    automatically.

    >>> tokenize = MosesTokenizer("en")
    >>> tokenize("Hello World!")
    ["Hello", "World", "!"]
    """

    def __init__(self, lang="en"):
        self.lang = lang
        program = path.join(path.dirname(__file__), "tokenizer.perl")
        argv = ["perl", program, "-l", self.lang]
        super().__init__(argv)

    def __str__(self):
        return "MosesTokenizer(lang=\"{lang}\")".format(lang=self.lang)

    def __call__(self, sentence):
        """Tokenizes a single sentence.

        Newline characters are not allowed in the sentence to be tokenized.
        """
        assert isinstance(sentence, str)
        sentence = sentence.rstrip("\n")
        assert "\n" not in sentence
        if not sentence:
            return []
        self.writeline(sentence)
        return self.readline().split()


def main():
    args = docopt(__doc__)
    if args["--selftest"]:
        testmod()
    tokenize = MosesTokenizer(args["<lang>"])
    inputfile = open(args["<inputfile>"]) if args["<inputfile>"] else sys.stdin
    outputfile = open(args["<outputfile>"]) if args["<outputfile>"] else sys.stdout
    with inputfile, outputfile:
        for line in inputfile:
            print(*tokenize(line), file=outputfile)
