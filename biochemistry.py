import re

def replaceBiochemistry(txt):
    txt = re.sub("expand IDR", "intrinscially disordered region", txt, flags=re.IGNORECASE)
    txt = re.sub("expand CTE", ",C-terminal extension", txt, flags=re.IGNORECASE)
    txt = re.sub("expand LLPS", "liquid-liquid phase separation", txt, flags=re.IGNORECASE)
    txt = re.sub("expand GEO", "Gene Expression Omnibus", txt, flags=re.IGNORECASE)
    txt = re.sub("expand AD", "Alzheimer's Disease", txt, flags=re.IGNORECASE)
    


    return txt
    
def replaceVirology(txt):
        txt = re.sub("expand LPS", "lipopolysacharide", txt, flags=re.IGNORECASE)
        txt = re.sub("expand HRDR", ",host range determining regions", txt, flags=re.IGNORECASE)
        txt = re.sub("expand LLPS", "liquid-liquid phase separation", txt, flags=re.IGNORECASE)
        txt = re.sub("expand GEO", "Gene Expression Omnibus", txt, flags=re.IGNORECASE)
        txt = re.sub("expand AD", "Alzheimer's Disease", txt, flags=re.IGNORECASE)
    
    return txt
    
    
    
    
def replaceProgramming(txt):
    txt = re.sub("expand CFI", "C-Fortran Interoperability", txt, flags=re.IGNORECASE)
 
 
    return txt
    
    
    
def replaceProgramming(txt):    
    
    txt = re.sub("expand MCDM", "multiple criteria decision-making", txt, flags=re.IGNORECASE)
 