def is_substring(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    if n2>n1: return False
    for i in range(n1-n2+1):
        if s1[i:(i+n2)] == s2: return True
    return False

print is_substring("example","ample")
print is_substring("elephant","cat")

