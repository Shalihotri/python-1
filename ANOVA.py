from scipy.stats import f_oneway
import itertools
import numpy

a = [2,3,2,3]
b = [4,6,3,5]
c = [4,5,4,5]
d = [6,7,6,7]

variables = [a,b,c,d]
variables_literal = ['a','b','c','d']

combinations = list(itertools.combinations(variables,2))
combinations_literal = list(itertools.combinations(variables_literal,2))

F_compilation = []
p_compilation = []

for i in combinations:
    F, p = f_oneway(i[0],i[1])
    F_compilation.append(F)
    p_compilation.append(p)

conclusion = []

for i in p_compilation:
    if i < 0.05:
        conclusion.append('different mean')
    else:
        conclusion.append('same mean')

final = []

for i, j in zip(combinations_literal, conclusion):
    asd = []
    asd.append(i)
    asd.append(j)
    final.append(asd)