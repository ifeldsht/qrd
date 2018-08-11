from math import sqrt

def eq_roots(a,b,c):
    det = b*b - 4*a*c
    if det >= 0:
       root1 = (-b+sqrt(det))/2/a
       root2 = (-b-sqrt(det))/2/a
       # returning two roots as pairs of real part and 0 for imaginary part
       # to have the same format for det>=0 and det<0
       return ( (root1,0), (root2,0) )
    else:
       re = -b/2/a
       im = sqrt(-det)/2/a
       return ( (re,im), (re,-im) )

print eq_roots(1.0,0.0,4.0)
print eq_roots(1.0,0.0,-4.0)
print eq_roots(1.0,3.0,0.0)

