import pandas as pd
import numpy as np


chat_id = 1676035524 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from scipy.stats import ttest_ind
    stat, p = ttest_ind(x, y, equal_var=False)
    if stat < 0 and p <= 0.05:
        b = True
    else:
        b = False
    return b  # Ваш ответ, True или False
