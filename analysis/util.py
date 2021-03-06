import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib as mpl
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = [8, 6]

DATA_DIR = os.path.abspath('../data')
ANALYSIS_DIR = os.path.abspath('../analysis')
PLOT_DIR = os.path.abspath('../tex/plots/dis')

RAW_DATASET = os.path.join(DATA_DIR, 'combined_dataset_raw.csv')
DATASET_SUBSET = os.path.join(DATA_DIR, 'combined_dataset_subset.csv')
DATASET_SUBSET_FINAL = os.path.join(DATA_DIR, 'combined_dataset_subset_final.csv')
DATASET_ALL = os.path.join(DATA_DIR, 'combined_dataset_all.csv')
DATASET_ALL_FINAL = os.path.join(DATA_DIR, 'combined_dataset_all_final.csv')

RAFIQ2016_COUNTRIES = ['AGO', 'BGD', 'CHN', 'CRI', 'ETH', 'GHA', 'IND', 'IDN', 'JOR', 'LBN', 'MYS', 'MNG', 'MOZ', 'NAM', 'NGA', 'PAN', 'SGP', 'SDN', 'TZA', 'THA', 'VNM', 'ZMB']
TIBA2018_MID_COUNTRIES = ['ARG', 'BRA', 'BGR', 'CHL', 'CHN', 'COL', 'MYS', 'MEX', 'THA', 'TUR']
TIBA2018_HIGH_COUNTRIES = ['AUS', 'CAN', 'FRA', 'DEU', 'JPN', 'NLD', 'PRT', 'ESP', 'SWE', 'CHE', 'GBR', 'USA']
SUBSET_COUNTRIES = TIBA2018_MID_COUNTRIES + TIBA2018_HIGH_COUNTRIES
ALL_COUNTRIES = ['ALB', 'ARG', 'ARM', 'AUS', 'AUT', 'AZE', 'BEL', 'BGD', 'BGR', 'BLR', 'BRA', 'CAN', 'CHE', 'CHL', 'CHN', 'COL', 'CYP', 'CZE', 'DEU', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GEO', 'GRC', 'GTM', 'HKG', 'HND', 'HRV', 'HUN', 'IDN', 'IND', 'IRL', 'IRN', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KOR', 'LKA', 'LTU', 'LVA', 'MAR', 'MDA', 'MEX', 'MKD', 'MLT', 'MOZ', 'MYS', 'NLD', 'NOR', 'NZL', 'PAK', 'PAN', 'PER', 'PHL', 'POL', 'PRT', 'PRY', 'ROU', 'RUS', 'SAU', 'SGP', 'SVK', 'SVN', 'SWE', 'THA', 'TJK', 'TUN', 'TUR', 'TZA', 'UKR', 'URY', 'USA', 'UZB', 'VEN', 'VNM', 'ZAF', 'ZMB']

def save_table(table, file, save=False, **kwargs):
    if save:
        path = os.path.join(PLOT_DIR, file)
        with open(path, 'w') as fd:
            fd.write(table.to_latex(**kwargs))
        
def save_fig(file, save=False, **kwargs):
    if save:
        path = os.path.join(PLOT_DIR, file)
        plt.savefig(path, metadata={'CreationDate': None})

def reindex_Rdata(r_data):
    return dict(
        (k, v.set_index('index'))
        if isinstance(v, pd.DataFrame) and 'index' in v.columns
        else (k, v)
        for (k, v) in r_data.items()
    )