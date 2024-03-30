import re

def replaceXtalEq(txt):
    structureFactorEquation=r"""$$\\mathbf{F}(\\mathbf{S})=\\sum_{j=1}^n f_j \\exp \\left[2 \\pi i \\mathbf{r}_j \\cdot \\mathbf{S}\\right]$$"""
    txt = re.sub("insert the structure factor equation", structureFactorEquation, txt, flags=re.IGNORECASE)
    return txt