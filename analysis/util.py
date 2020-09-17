import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = [9, 6]

DATA_DIR = '../data'
PLOT_DIR = '../tex/plots/dis'

RAW_DATASET = os.path.join(DATA_DIR, 'combined_dataset_raw.csv')
DATASET_SUBSET = os.path.join(DATA_DIR, 'combined_dataset_subset.csv')
DATASET_FINAL = os.path.join(DATA_DIR, 'combined_dataset_final.csv')

RAFIQ2016_COUNTRIES = ['AGO', 'BGD', 'CHN', 'CRI', 'ETH', 'GHA', 'IND', 'IDN', 'JOR', 'LBN', 'MYS', 'MNG', 'MOZ', 'NAM', 'NGA', 'PAN', 'SGP', 'SDN', 'TZA', 'THA', 'VNM', 'ZMB']
TIBA2018_MID_COUNTRIES = ['DZA', 'ARG', 'BRA', 'BGR', 'CHL', 'CHN', 'COL', 'MYS', 'MEX', 'THA', 'TUR', 'VEN']
TIBA2018_HIGH_COUNTRIES = ['AUS', 'CAN', 'FRA', 'DEU', 'JPN', 'NLD', 'PRT', 'ESP', 'SWE', 'CHE', 'GBR', 'USA']

ALL_COUNTRIES = set(TIBA2018_MID_COUNTRIES + TIBA2018_HIGH_COUNTRIES)

def save_table(table, file, save=False, **kwargs):
    if save:
        path = os.path.join(PLOT_DIR, file)
        with open(path, 'w') as fd:
            fd.write(table.to_latex(**kwargs))
        
def save_fig(file, save=False, **kwargs):
    if save:
        path = os.path.join(PLOT_DIR, file)
        plt.savefig(path, metadata={'CreationDate': None})