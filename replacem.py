#!/usr/bin/env python3

from contractions import replaceContractions
from pathlib import Path
import sys

"""
This is the master script for applying imported text replacement libraries to transcribed text from whisper.
We set up this project to be modular because different people will want different combinations of text replacements.
This also eases the development of new libraries by users.
The external files or modules we defined reside in the project directory.

In principle, we could install this project on PyPi and then people could pip install it into their local Python library.
However, that seems to be overkill in this case because this is a trivial project.
"""

txt = Path(sys.argv[1]).read_text()
my_file = open(sys.argv[1] + "corrected.txt", "w")

"""Import the text replacement functions.
Note that you have to define a new variable that
is mapped to the returned processed text.
"""

retxt = replaceContractions(txt)
my_file.write(retxt)
my_file.close()
