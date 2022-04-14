import numpy as np
import pandas as pd
from datetime import timedelta, datetime
import warnings
warnings.filterwarnings('ignore')
import matplotlib as plt

def date_to_index (df, col_date):
    '''
    takes in a df and a name of the column that is a date. 
    return a df with the selected column in datetime format  as Index 
    '''
    #convert sale_date to datetime format
    df[col_date]= pd.to_datetime(df[col_date])
    #set date as index
    df = df.set_index(col_date).sort_index()
    return df

def prep_sales (df, col_date):
    '''
    takes in a df and the name of the column (date),
    return df  with the selected column in datetime format  as Index, new columns:
    month, day of week and sales_total
    '''
    
    #set date to index
    df = date_to_index (df, col_date)
    
    #create new columns
    df['month '] = df.index.month
    df['day_of_week' ] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    #drop a column
    df = df.drop(columns ='Unnamed: 0')

    return df

def distribution (df):
    '''
    takes in a df and plot individual variable distributions excluding object type
    '''
    cols =df.columns.to_list()
    for col in cols:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.xlabel('values')
            plt.ylabel('Counts ')
            plt.show()
