import pandas as pd
import numpy as np


import seaborn as sns
import matplotlib.pyplot as plt

import env
import os
import wrangle as w

def check_file_exists(fn, query, url):
    """
    check if file exists in my local directory, if not, pull from sql db
    return dataframe
    """
    if os.path.isfile(fn):
        print('csv file found and loaded')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df 

import os

def get_curr_log(filename='curr_log.csv'):
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col='date')
    else:
        url = env.get_db_url('curriculum_logs')

        query = '''
        select *
        from logs
        join cohorts on cohorts.id = logs.cohort_id;
        '''

        df = pd.read_sql(query, url)

        # drop columns
        df = df.drop(columns=['cohort_id', 'slack', 'created_at', 'updated_at', 'deleted_at'])

        # rename columns
        df = df.rename(columns={'path': 'viewed', 'id':'cohort_id'})

        # Drop rows with values 1 and 4
        df = df[~df['program_id'].isin([1, 4])]
        
        # Drop rows where 'viewed' column contains '/'
        df = df[df['viewed'] != '/']

        # Drop rows where 'viewed' column contains 'toc'
        df = df[df['viewed'] != 'toc']

        # Replace values 2 with 'web_dev' and 3 with 'data_science'
        df['program_id'] = df['program_id'].replace({2: 'web_dev', 3: 'data_science'})

        # Set date column from an object to proper datetime dtype format
        df['date'] = pd.to_datetime(df['date'])

        # Set start date column to proper datetime dtype format
        df['start_date'] = pd.to_datetime(df['start_date'])

        # Set end date column to proper datetime dtype format
        df['end_date'] = pd.to_datetime(df['end_date'])

        # Set the index as the date column
        df = df.set_index('date')

        # Sort the dates (index)
        df = df.sort_index()

        # Drop null values
        df = df.dropna()

        # Save to csv
        df.to_csv(filename)

    return df
