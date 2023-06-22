def reverseString(str: str) -> str:
    l=list(str.split())
    s=""
    l=l[::-1]
    s+=" ".join(l)
    return s
    