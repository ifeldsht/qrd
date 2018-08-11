def is_substring(s1,s2):
    if len(s1) < len(s2): return False
    if s1[:len(s2)] == s2: return True
    return is_substring(s1[1:],s2)

print is_substring("example","ample")
print is_substring("elephant","cat")

