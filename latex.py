import re

def replaceLaTeX(txt):
    itemizedList=r"""\\begin{itemize}
    \\item
    \\item
    \\item
    \\item
\\end{itemize}"""
    txt = re.sub("insert itemized list", itemizedList, txt, flags=re.IGNORECASE)
    txt = re.sub("new itemized list", r"""\\begin{itemize}
    \\item
    \\item
    \\item
    \\item
\\end{itemize}""", txt, flags=re.IGNORECASE)
    txt = re.sub("%.","\%", txt, flags=re.IGNORECASE)
#    txt = re.sub("\","\\", txt, flags=re.IGNORECASE)
    return txt