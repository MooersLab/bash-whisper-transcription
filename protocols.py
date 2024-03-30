import re

def replaceProtocols(txt):
    txt = re.sub("insert equation", r" - \n - \n \\item $\\phi = 1 + 4$ \n - \n", txt, flags=re.IGNORECASE)
    coresubmit =r"""\\subsection{Protocol for article resubmission for (co-)authors}
\\begin{itemize}
    \\item Decide how to address the reviews
    \\item Do the revisions
    \\item Write response to reviewers
    \\item Write cover letter for the resubmission
    \\hrule
    \\item Check your affiliation
    \\item Check your grant numbers
    \\item Check for consistent capitalization of X-ray
    \\item Check for proper verb tense after data
    \\item Check reference formatting
    \\item Check that all acronyms are defined
    \\item Check that keywords are not used in title (Store a private list of keywords for later suggestions.)
    \\item Check the figure legends.
    \\item Check the match of figure numbers in reference and legend
    \\item Proofread the manuscript (1000 words per hour)
    \\item Proofread the response to reviewers
    \\item Proofread the cover letter
\\end{itemize}"""
    txt = re.sub("protocol for article resubmisson", coresubmit, txt, flags=re.IGNORECASE)
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

    return txt