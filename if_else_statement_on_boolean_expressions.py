'''
Logical operators have different priorities and therefore are executed at different times.

The order is as follows:
Logical complements (not) are executed first,
logical conjunctions (and) are executed next,
and logical disjunctions (or) are executed at the end.

_____________________________________________________________
        (∧) (∨)  (~∧) (~∨)  (⊻)  (⇒)          (⇔)
p   q   and  or  nand  nor  xor  conditional  Bi-conditional 
_____________________________________________________________
T	T	 T	 T	 F	   F	F	     T	             T
T	F	 F	 T	 T	   F	T	     F	             F
F	T	 F	 T	 T	   F	T	     T	             F
F	F    F   F	 T	   T	F	     T               T
_____________________________________________________________

'''
a, b, c = True, False, True

if a or b and c:
    print("True")
else:
    print("False")