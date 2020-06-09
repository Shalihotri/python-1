import pandas as pd
import numpy as np

series = pd.Series([1,2,3,4,5,4,3,2,1,2,3,4,5,10,20,50])

q1 = series.quantile(0.25)
q3 = series.quantile(0.75)
iqr = q3 - q1

upper_limit = q3 + 1.5*iqr
lower_limit = q1 - 1.5*iqr

series_clean = series[(series > lower_limit) & (series < upper_limit)]