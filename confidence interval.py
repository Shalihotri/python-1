import numpy as np
import scipy.stats as stats

data=np.array([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])

def CI(data, level_of_confidence):
    n=len(data)
    mean=np.mean(data)
    sem=stats.sem(data)
    z = stats.t.ppf((1 + 0.95)/2, n-1)
    h = sem*z
    return (mean-h, mean+h)