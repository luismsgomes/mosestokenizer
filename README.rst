mosestokenizer
==============

This package provides wrappers for some pre-processing Perl scripts from the
Moses toolkit, namely, ``normalize-punctuation.perl``, ``tokenizer.perl``,
``detokenizer.perl`` and ``split-sentences.perl``.

Sample Usage
------------

All provided classes are importable from the package ``mosestokenizer``.

    >>> from mosestokenizer import *

All classes have a constructor that takes a two-letter language code as
argument (``'en'``, ``'fr'``, ``'de'``, etc) and the resulting objects
are callable.

When created, these wrapper objects launch the corresponding Perl script as a
background process.  When the objects are no longer needed, you should call the
``.close()`` method to close the background process and free system resources.

The objects also support the context manager interface.
Thus, if used within a ``with`` block, the ``.close()`` method is invoked
automatically when the block exits.

The following two usages of ``MosesTokenizer`` are equivalent:

    >>> # here we will call .close() explicitly at the end:
    >>> tokenize = MosesTokenizer('en')
    >>> tokenize('Hello World!')
    ['Hello', 'World', '!']
    >>> tokenize.close()

    >>> # here we take advantage of the context manager interface:
    >>> with MosesTokenizer('en') as tokenize:
    >>>     tokenize('Hello World!')
    ...
    ['Hello', 'World', '!']

As shown above, ``MosesTokenizer`` callable objects take a string and return a
list of tokens (strings).

By contrast, ``MosesDetokenizer`` takes a list of tokens and returns a string:

    >>> with MosesDetokenizer('en') as detokenize:
    >>>     detokenize(['Hello', 'World', '!'])
    ...
    'Hello World!'

``MosesSentenceSplitter`` does more than the name says.  Besides splitting
sentences, it will also unwrap text, i.e. it will try to guess if a sentence
continues in the next line or not.  It takes a list of lines (strings) and
returns a list of sentences (strings):

    >>> with MosesSentenceSplitter('en') as splitsents:
    >>>     splitsents([
    ...         'Mr. Smith is away.  Do you want to',
    ...         'leave a message?'
    ...     ])
    ...
    ['Mr. Smith is away.', 'Do you want to leave a message?']


``MosesPunctuationNormalizer`` objects take a string as argument and return a
string:

    >>> with MosesPunctuationNormalizer('en') as normalize:
    >>>     normalize('«Hello World» — she said…')
    ...
    '"Hello World" - she said...'


License
-------

Copyright ® 2016-2021, Luís Gomes <luismsgomes@gmail.com>.

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
