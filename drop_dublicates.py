import pandas as pd
import numpy as np

data_to_clean = pd.read_csv('delfiout.csv', sep='\t')

good_data_set = data_to_clean.drop_duplicates()

good_data_set.to_csv('clean.csv', sep='\t', encoding='utf-8', mode='a')