x = int(input("number: "))



try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = x # set number of digits
print(mp.pi)   # print pi to a thousand places