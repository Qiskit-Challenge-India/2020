
import enum
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import pandas as pd

# replace with training dataset
raw_data = pd.read_csv('full.csv', header=None).to_numpy()

namedparam = []



for i in range(3):
    namedparam.append(f'x[{i}]')
X = raw_data[:, 1:]                             #x,y,z


for i in range(3):
    for j in range(i, 3):
        namedparam.append(f'x[{i}]*x[{j}]')
        X = np.c_[X, (X[:,i]*X[:,j])]

for i in range(3):
    for j in range(i, 3):
        for k in range(j, 3):
            namedparam.append(f'x[{i}]*x[{j}]*x[{k}]')
            X = np.c_[X, ( (X[:,i]*X[:,j])*X[:,k] )]


for i in range(3):
    for j in range(i, 3):
        for k in range(j, 3):
            for l in range(k, 3):
                namedparam.append(f'x[{i}]*x[{j}]*x[{k}]*x[{l}]')
                X = np.c_[X, ( (X[:,i]*X[:,j])*X[:,k]*X[:,l])]


for i in range(3):
    for j in range(i, 3):
        for k in range(j, 3):
            for l in range(k, 3):
                for m in range(l, 3):
                    namedparam.append(f'x[{i}]*x[{j}]*x[{k}]*x[{l}]*x[{m}]')
                    X = np.c_[X, ( (X[:,i]*X[:,j])*X[:,k]*X[:,l]*X[:, m])]



for i in range(3):
    namedparam.append(f'(1.0/x[{i}])')
    X = np.c_[X, 1.0/X[:, i]]


for i in range(3):
    for j in range(i, 3):
        namedparam.append(f'(1.0/(x[{i}]*x[{j}]))')
        X = np.c_[X, (1.0/(X[:, i]*X[:, j]))]

# best submission 0.8325
# upto x^6, x^-2  -> 0.843167 (liblinear)
# upto x^6, x^-3  -> 0.843833 (liblinear)
# upto x^6, x^-4  -> 0.844167 (liblinear)
# upto x^6, x^-5  -> 0.844167 (liblinear)
# upto x^6, x^-4  -> 0.843667 (lbfgs)
# upto x^6, x^-5  -> 0.844667 (lbfgs)
# upto x^6, x^-5  -> 0.844667 (newton-cg)

Y = np.array(raw_data[:, 0], dtype=int)

logreg = LogisticRegression(C=1e5, max_iter=10000, solver='liblinear')

# Create an instance of Logistic Regression Classifier and fit the data.
logreg.fit(X, Y)
score = logreg.score(X, Y)

print(logreg.coef_, logreg.intercept_)

Z = (np.sum(logreg.coef_[0]*X, axis=1) + logreg.intercept_)
print(f'min, max = {Z.min()}, {Z.max()}')
delta_max = max(abs(Z.min()), abs(Z.max()))
maxoff = 3.1
coef = logreg.coef_ * maxoff/delta_max
intercept = logreg.intercept_ * maxoff/delta_max


# store the generated expression in expression.txt file
with open('expression.txt','w') as fp:
    fp.write(f'{intercept[0]:10f} ')
    for i,p in enumerate(namedparam):
        fp.write(f'{coef[0][i]:+.10f}*{p} ')

print('\n'+'-'*60+'\n')
print("\n\nscore = ", score)
 



"""
You can use these recursive functions to avoid the pain of writing so many for loops.
"""

def combinations(n, begin=0):
    res = []
    if n == 1:
        return [[x] for x in range(begin, 3)]
    else:
        for i in range(begin, 3):
            for ch in combinations(n-1, i):
                ch.append(i)
                res.append(ch)
    return res

def addparamprod(nterms):
    literal = combinations(nterms)
    global X
    for lit in literal:
        s = '*'.join(map(lambda i: f'x[{i}]', lit))
        namedparam.append(f'({s})')
        tX = X[:,lit[0]]
        for c in lit[1:]:
            tX = tX * X[:, c]
        X = np.c_[X, tX]

def addinvparamprod(nterms):
    literal = combinations(nterms)
    global X
    for lit in literal:
        s = '*'.join(map(lambda i: f'(1.0/x[{i}])', lit))
        namedparam.append(f'({s})')
        tX = np.ones(X.shape[0], dtype=float)
        for c in lit:
            tX = tX * (1.0 / X[:, c])
        X = np.c_[X, tX]

